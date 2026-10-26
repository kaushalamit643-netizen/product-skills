---
name: product-manager-toolkit
description: "Prioritize product features with RICE, synthesize customer interviews, and write PRDs grounded in evidence. Use for feature ranking, discovery synthesis, or new product requirements; use code-to-prd for documenting existing code."
---

# Product Manager Toolkit

Choose the requested deliverable: prioritization, interview synthesis, or a PRD. Establish the product outcome and reuse supplied context before asking for missing decision-critical inputs.

For RICE, align the reach period and effort units, document confidence assumptions, and calculate reach × impact × confidence / effort. Review dependencies, capacity, deadline sensitivity, and sensitivity to estimate changes before treating the score as a decision. The CSV template is in `assets/rice_input_template.csv`.

For interview synthesis, distinguish quotations, observations, and interpretations. Use `scripts/customer_interview_analyzer.py` as a heuristic aid; verify themes against transcripts and report counterexamples and sample limitations.

For PRDs, use `assets/prd_template.md` or `references/prd_templates.md`. State the problem, audience, scope, non-goals, user flows, acceptance criteria, measurable success, risks, and unresolved decisions. Do not invent customer evidence or success metrics.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/customer_interview_analyzer.py](scripts/customer_interview_analyzer.py)
- [scripts/rice_prioritizer.py](scripts/rice_prioritizer.py)
- [references/frameworks.md](references/frameworks.md)
- [references/input-output-examples.md](references/input-output-examples.md)
- [references/prd_templates.md](references/prd_templates.md)
- [assets/prd_template.md](assets/prd_template.md)
- [assets/rice_input_template.csv](assets/rice_input_template.csv)
