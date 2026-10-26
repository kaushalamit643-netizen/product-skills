---
name: code-to-prd
description: "Reverse-engineer an existing codebase into product requirements, page and endpoint inventories, business rules, and permission documentation. Use for documenting implemented behavior, not proposing a new product."
---

# Code To PRD

Use three phases: global scan, detailed page/endpoint analysis, and structured documentation. Inspect routes, components, APIs, models, state, validation, translations, guards, and middleware.

Use `scripts/codebase_analyzer.py` for a heuristic inventory, then verify it against the code. Use `scripts/prd_scaffolder.py` to create a documentation skeleton. Fill every scaffold section from implementation evidence; generated inventory and placeholders are not completed requirements.

For each page or endpoint, document audience, permissions, entry conditions, layout or request/response fields, required/default/validation rules, interactions, loading/error/empty states, side effects, and related flows. Enumerate actual status and enum values.

Separate implemented behavior, inference, mock behavior, and unknowns; cite source file locations for non-obvious rules. Use `references/framework-patterns.md`, `references/prd-quality-checklist.md`, and `expected_outputs/` for examples and completeness checks. Return a usable inventory, per-page/endpoint docs, and explicit gaps.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/.gitignore](scripts/.gitignore)
- [scripts/codebase_analyzer.py](scripts/codebase_analyzer.py)
- [scripts/prd_scaffolder.py](scripts/prd_scaffolder.py)
- [references/framework-patterns.md](references/framework-patterns.md)
- [references/prd-quality-checklist.md](references/prd-quality-checklist.md)
- [assets/sample-analysis.json](assets/sample-analysis.json)
- [expected_outputs/sample-enum-dictionary.md](expected_outputs/sample-enum-dictionary.md)
- [expected_outputs/sample-page-user-list.md](expected_outputs/sample-page-user-list.md)
- [expected_outputs/sample-prd-readme.md](expected_outputs/sample-prd-readme.md)
