---
name: ui-design-system
description: "Create or refine design tokens, component specifications, responsive rules, and developer handoffs. Use for a reusable UI design system rather than a one-off page."
---

# UI Design System

Inspect the existing token and component system first. Preserve established naming and platform conventions unless the task explicitly changes them.

Generate foundation tokens for color, typography, spacing, radii, elevation, and breakpoints, then map semantic and component tokens to those foundations. Document states, variants, focus behavior, keyboard interaction, and responsive behavior for the components in scope.

Use `scripts/design_token_generator.py` to propose tokens from a brand color; verify actual foreground/background contrast and intended usage rather than assuming every generated pair is accessible.

Read `references/token-generation.md` for algorithms, `references/component-architecture.md` for component structure, `references/responsive-calculations.md` for responsive scales, and `references/developer-handoff.md` for integration. Return the requested token formats and actionable component guidance.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/design_token_generator.py](scripts/design_token_generator.py)
- [references/component-architecture.md](references/component-architecture.md)
- [references/developer-handoff.md](references/developer-handoff.md)
- [references/responsive-calculations.md](references/responsive-calculations.md)
- [references/token-generation.md](references/token-generation.md)
- [assets/design_system_doc_template.md](assets/design_system_doc_template.md)
