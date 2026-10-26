---
name: ux-researcher-designer
description: "Plan user research, synthesize interviews, create evidence-based personas and journey maps, and design usability studies. Use for understanding user needs and evaluating experiences."
---

# UX Researcher Designer

Select the research question, target participants, method, and decision the findings should support. Reuse existing research before proposing new collection.

For synthesis, trace each pattern to observations or quotes, preserve contradictions, and explain sampling limitations. For personas, describe behavior, goals, context, and evidence confidence; label hypothetical personas explicitly.

Map journeys by user goal, stage, actions, touchpoints, friction, emotions, and opportunities. Distinguish observed behavior from assumptions. For usability studies, define realistic tasks, success measures, recruitment criteria, and finding severity.

`scripts/persona_generator.py` emits synthetic sample personas. Use it for structure only; never present its sample data, calculated-looking scores, or invented demographics as research evidence. Use `assets/research_plan_template.md` to plan actual research.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/persona_generator.py](scripts/persona_generator.py)
- [references/example-personas.md](references/example-personas.md)
- [references/journey-mapping-guide.md](references/journey-mapping-guide.md)
- [references/persona-methodology.md](references/persona-methodology.md)
- [references/usability-testing-frameworks.md](references/usability-testing-frameworks.md)
- [assets/research_plan_template.md](assets/research_plan_template.md)
