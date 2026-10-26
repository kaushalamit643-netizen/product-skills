---
name: roadmap-communicator
description: "Write audience-specific roadmap narratives, release notes, changelogs, and stakeholder updates. Use to communicate product direction or delivered changes."
---

# Roadmap Communicator

Identify the audience, source of truth, release or planning scope, and decisions to communicate. Distinguish shipped functionality, committed work, and tentative direction.

Choose now/next/later, themes, or a dated roadmap according to the certainty and commitments already established. Include outcomes, dependencies, risks, and owners without inventing dates or promises.

Use `scripts/changelog_generator.py` for an explicit Git range or supplied commit text. Run it with the target repository as the working directory; resolve real refs first. Review the implementation before claiming a commit is released or user-visible.

For customers, lead with user value and migration impact. For executives, emphasize outcomes, tradeoffs, and decisions. For engineering, give scope, sequencing, dependencies, and rollout considerations. Use `references/roadmap-templates.md` and `references/communication-templates.md`. Drafting does not authorize publication.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/changelog_generator.py](scripts/changelog_generator.py)
- [references/communication-templates.md](references/communication-templates.md)
- [references/roadmap-templates.md](references/roadmap-templates.md)
