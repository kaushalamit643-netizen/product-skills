#!/usr/bin/env python3
"""Validate this bundle's metadata, resources, helper CLIs, and relocated routing.

Uses only the Python standard library; it validates the emitted scalar YAML subset,
not arbitrary YAML. It does not certify generated applications or product methods.
"""
import ast
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'agile-product-owner', 'apple-hig-expert', 'code-to-prd', 'competitive-teardown',
    'experiment-designer', 'landing-page-generator', 'product-analytics',
    'product-discovery', 'product-manager-toolkit', 'product-skills',
    'product-strategist', 'research-summarizer', 'roadmap-communicator',
    'saas-scaffolder', 'spec-to-repo', 'ui-design-system', 'ux-researcher-designer',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run(path, arguments, cwd, expected=0):
    result = subprocess.run([sys.executable, str(path), *arguments], cwd=cwd,
                            text=True, capture_output=True, timeout=30)
    require(result.returncode == expected,
            f'{path.name}: exit {result.returncode}, expected {expected}: {result.stderr[-1500:]}')
    return result.stdout


def main():
    skills = ROOT / 'skills'
    directories = sorted(p for p in skills.iterdir() if p.is_dir())
    require({p.name for p in directories} == EXPECTED, 'Unexpected or missing skills')
    scripts = []
    for folder in directories:
        text = (folder / 'SKILL.md').read_text()
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        require(match, f'Missing frontmatter: {folder.name}')
        fields = dict(line.split(': ', 1) for line in match[1].splitlines())
        require(set(fields) == {'name', 'description'}, f'Invalid fields: {folder.name}')
        require(fields['name'] == folder.name, f'Name mismatch: {folder.name}')
        description = json.loads(fields['description'])
        require(0 < len(description) <= 1024, f'Invalid description: {folder.name}')
        ui = (folder / 'agents/openai.yaml').read_text().splitlines()
        require(ui[0] == 'interface:', f'Missing UI interface: {folder.name}')
        metadata = dict(line.strip().split(': ', 1) for line in ui[1:])
        values = {key: json.loads(value) for key, value in metadata.items()}
        require(25 <= len(values['short_description']) <= 64, f'UI blurb length: {folder.name}')
        require(f'${folder.name}' in values['default_prompt'], f'Invocation mismatch: {folder.name}')
        scripts.extend(sorted((folder / 'scripts').glob('*.py')))
        for path in folder.rglob('*.md'):
            content = path.read_text()
            require(not re.search(r'\.claude/|context: fork', content),
                    f'Source distribution dependency: {path}')
            if any(part in {'expected_outputs', 'assets', 'templates'} for part in path.relative_to(folder).parts):
                continue  # Output examples intentionally link to files the user will create.
            link_text = re.sub(r'(?ms)^```.*?^```[^\n]*', '', content)
            for target in re.findall(r'\]\(([^)]+)\)', link_text):
                if '://' in target or target.startswith(('#', 'mailto:')):
                    continue
                local = target.split('#')[0]
                require((path.parent / local).exists(), f'Broken link in {path}: {target}')
    with tempfile.TemporaryDirectory(prefix='product-skills-validation-') as temp:
        work = Path(temp)
        for path in scripts:
            ast.parse(path.read_text(), filename=str(path))
            run(path, ['--help'], work)
        router = skills / 'product-skills/scripts/product_goal_router.py'
        spec = importlib.util.spec_from_file_location('product_router', router)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for lane in module.SIGNALS.values():
            result = json.loads(run(router, ['--text', ' '.join(lane['keywords'])], work))
            require(result['route_to'] == lane['skill'], f'Routing failed: {lane["skill"]}')
            require(Path(result['skill_path']) == skills / lane['skill'], 'Router path incorrect')
            require((Path(result['skill_path']) / 'SKILL.md').exists(), 'Routed skill missing')
        run(router, ['--text', 'hello'], work, expected=3)
        run(router, ['--text', 'roadmap'], work, expected=2)
        # Reinstall the router and a target in a different location to catch hardcoded roots.
        moved = work / 'relocated'
        shutil.copytree(skills / 'product-skills', moved / 'product-skills')
        shutil.copytree(skills / 'product-discovery', moved / 'product-discovery')
        result = json.loads(run(moved / 'product-skills/scripts/product_goal_router.py', ['--sample'], work))
        require(Path(result['skill_path']) == (moved / 'product-discovery').resolve(), 'Relocated route incorrect')
    print(f'PASS: {len(directories)} skills, {len(scripts)} helper CLIs, resource links, '
          '16 routing lanes, refusal/ambiguity exits, and relocated installation.')


if __name__ == '__main__':
    main()
