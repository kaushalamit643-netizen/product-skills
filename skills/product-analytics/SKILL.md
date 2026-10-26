---
name: product-analytics
description: "Define product KPIs and tracking plans, analyze cohorts, retention, funnels, and feature adoption, and translate metric changes into product decisions."
---

# Product Analytics

Define the unit of analysis, population, events, eligibility, time window, timezone, and observation cutoff. Check missing dates, duplicate events, and identity consistency before calculating metrics.

Choose AARRR, North Star, or HEART according to the decision. Give each KPI a definition, owner, baseline, target, and decision rule. Distinguish acquisition volume from activation, value delivery, and retained use.

Use `scripts/metrics_calculator.py` for CSV retention, cohort, or funnel calculations. Inspect its definitions: the funnel helper counts stage membership without timestamps, so it cannot establish ordered conversion. Exclude immature periods or label incomplete cohorts before interpreting retention.

Segment results and compare like windows. Report denominators and uncertainty, distinguish correlation from causal evidence, and connect findings to a specific investigation or action. See `references/metrics-frameworks.md` and `references/dashboard-templates.md`.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/metrics_calculator.py](scripts/metrics_calculator.py)
- [references/dashboard-templates.md](references/dashboard-templates.md)
- [references/metrics-frameworks.md](references/metrics-frameworks.md)
