---
name: apple-hig-expert
description: "Audit or design Apple-platform interfaces against current Human Interface Guidelines. Use for iOS, iPadOS, macOS, watchOS, tvOS, or visionOS navigation, accessibility, contrast, and interaction review."
---

# Apple HIG Expert

Establish the platform, OS version, interface evidence, and requested audit or design scope. Verify version-sensitive guidance against current official Apple documentation rather than treating stored references as current rules.

For design, select platform navigation and layout conventions, semantic colors, typography, and interaction states. For audits, tie each finding to an observed element, applicable guidance, user impact, and a concrete fix.

Use `scripts/hig_checker.py` for contrast and target-size calculations or a JSON batch report. Its fixed thresholds and weighted score are heuristics, not Apple certification or a complete accessibility audit. Check platform and input context before applying target dimensions; test actual rendered compositing for translucent backgrounds.

Read `references/platform-specifics.md`, `references/visual-design.md`, and `references/accessibility.md` for relevant details. Use `templates/hig-audit-template.md` for a structured report. Separate measured failures, visual concerns, and checks that need runtime access.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/hig_checker.py](scripts/hig_checker.py)
- [references/accessibility.md](references/accessibility.md)
- [references/platform-specifics.md](references/platform-specifics.md)
- [references/visual-design.md](references/visual-design.md)
- [templates/hig-audit-template.md](templates/hig-audit-template.md)
