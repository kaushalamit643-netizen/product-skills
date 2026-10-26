---
name: product-skills
description: "Coordinate product work across the bundled product skills and review continuous-discovery cadence or opportunity solution trees. Use for a cross-functional product request or when the right product workflow is unclear."
---

# Product Skills

Choose the narrowest useful workflow from the sibling skills. If the user names a skill or deliverable, follow that intent directly. Read the selected sibling `SKILL.md`; use only resources that are actually available.

`scripts/product_goal_router.py` provides a deterministic keyword-based suggestion. A ROUTE result includes an absolute installed skill path. ASK (exit 2) and NO_SIGNAL (exit 3) indicate weak classifier evidence, not mandatory user approval: resolve with conversation context or ask only if the deliverable remains materially ambiguous.

For a discovery review, use `assets/sample_discovery_log.json` and `assets/sample_ost.json` for input schemas. Run `scripts/discovery_cadence_tracker.py` with an explicit `--as-of YYYY-MM-DD` when assessing current health, because its default uses the newest logged date. Fewer than two dated interviews returns exit 5.

Run `scripts/ost_linter.py` on the opportunity solution tree. It checks a measurable outcome, needs rather than features, alternative solutions, tests, and orphan nodes. Treat a passing check as structural validity, not validation of customer demand.

Return the requested artifact, evidence, assumptions, checks performed, and next decision. Keep discovery work bounded to the current request; ongoing monitoring, booking interviews, contacting people, or scheduling future work requires the user's authorization. No external harness, context forking, or subagents are required.

Read `references/continuous_discovery_canon.md`, `references/product_operating_model.md`, or `references/ai_product_evals.md` for the relevant product methods. For AI features, define evaluation examples, a rubric, and failure cases alongside acceptance criteria.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

## Bundled resources

- [scripts/discovery_cadence_tracker.py](scripts/discovery_cadence_tracker.py)
- [scripts/ost_linter.py](scripts/ost_linter.py)
- [scripts/product_goal_router.py](scripts/product_goal_router.py)
- [references/ai_product_evals.md](references/ai_product_evals.md)
- [references/continuous_discovery_canon.md](references/continuous_discovery_canon.md)
- [references/product_operating_model.md](references/product_operating_model.md)
- [assets/sample_discovery_log.json](assets/sample_discovery_log.json)
- [assets/sample_ost.json](assets/sample_ost.json)
