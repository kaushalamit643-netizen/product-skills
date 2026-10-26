---
name: agile-product-owner
description: "Write user stories and acceptance criteria, split epics, refine backlogs, and plan sprints from actual team capacity. Use for product ownership and Scrum delivery planning."
---

# Agile Product Owner

Start from the intended user outcome and existing backlog. Preserve the team's estimation units, workflow, and definition of done.

Write stories as actor, goal, and benefit. Check INVEST, split by independently valuable behavior, and specify observable Given/When/Then acceptance criteria, including failure paths, permissions, and relevant accessibility behavior.

For sprint planning, calculate available capacity from historical completion, leave, support work, and dependencies. Show assumptions and proposed load; do not treat story points as hours or impose generic velocity targets.

Use `assets/user_story_template.md` and `assets/sprint_planning_template.md` as starting points. `scripts/user_story_generator.py` produces examples and capacity suggestions, not a source of real team or user data.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/user_story_generator.py](scripts/user_story_generator.py)
- [references/sprint-planning-guide.md](references/sprint-planning-guide.md)
- [references/user-story-templates.md](references/user-story-templates.md)
- [assets/sprint_planning_template.md](assets/sprint_planning_template.md)
- [assets/user_story_template.md](assets/user_story_template.md)
