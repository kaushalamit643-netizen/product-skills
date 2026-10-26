---
name: competitive-teardown
description: "Compare competitor products, features, pricing, positioning, and user experience using cited evidence. Use for competitive intelligence, battlecards, market positioning, and product strategy comparisons."
---

# Competitive Teardown

Define the product, comparable competitors, audience, and decision to support. Collect current public facts with the available browsing tools; record source dates and distinguish observations from inferences.

Use `references/data-collection-guide.md` for collection approaches and `references/scoring-rubric.md` for the 12-dimension rubric. Adapt dimensions and weights to the decision, showing missing evidence rather than assigning unjustified scores.

Use `scripts/competitive_matrix_builder.py` to calculate the matrix from reviewed JSON. The helper expects 1–10 inputs; map the reference rubric’s 1–5 scores as `1 + (score - 1) * 9 / 4` before passing them to the helper. Explain weights, uncertainty, and sensitivity; job postings and reviews are signals, not verified market share or product capability.

Use `references/analysis-templates.md` for pricing, SWOT, positioning, and UX outputs. Finish with implications and prioritized opportunities tied to evidence; do not claim a feature is absent merely because it was not visible on a marketing page.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/competitive_matrix_builder.py](scripts/competitive_matrix_builder.py)
- [references/analysis-templates.md](references/analysis-templates.md)
- [references/competitive-analysis-frameworks.md](references/competitive-analysis-frameworks.md)
- [references/data-collection-guide.md](references/data-collection-guide.md)
- [references/scoring-rubric.md](references/scoring-rubric.md)
