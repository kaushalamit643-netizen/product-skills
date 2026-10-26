---
name: product-strategist
description: "Define product strategy, measurable OKRs, and company-to-product-to-team alignment. Use for vision, strategic tradeoffs, quarterly planning, and OKR cascades."
---

# Product Strategist

Establish the target customer, differentiated value, constraints, strategic horizon, and current baseline. State the few choices and tradeoffs that determine where to compete and how to win.

Translate strategy into outcome objectives and measurable key results with baseline, target, owner, and horizon. Map team contributions to parent outcomes and identify conflicting incentives or capacity assumptions.

Use `scripts/okr_cascade_generator.py` for an illustrative cascade and alignment calculations. Replace generated organizations, targets, and wording with supplied evidence; alignment scores describe the model and do not validate strategy.

Read `references/strategy_types.md` for strategy options and `references/okr_framework.md` for cascade mechanics. Return strategy rationale, OKR hierarchy, dependencies, and the decisions that would change the plan.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/okr_cascade_generator.py](scripts/okr_cascade_generator.py)
- [references/examples/sample_growth_okrs.json](references/examples/sample_growth_okrs.json)
- [references/okr_framework.md](references/okr_framework.md)
- [references/strategy_types.md](references/strategy_types.md)
- [assets/okr_template.md](assets/okr_template.md)
