---
name: experiment-designer
description: "Plan product experiments and A/B tests with explicit hypotheses, metrics, sample size, stopping rules, and interpretation. Use for experimental design or product-test results."
---

# Experiment Designer

Write the intervention, eligible population, expected behavioral mechanism, primary metric, and decision threshold. Specify randomization unit, guardrails, exposure rules, and instrumentation checks before launch.

Use `scripts/sample_size_calculator.py` for approximate two-arm binary conversion tests. State baseline rate, absolute or relative MDE, alpha, power, required sample per arm, expected traffic, and runtime. Do not apply the binary-rate calculator to continuous metrics, cluster designs, or sequential tests.

Predefine the stopping and analysis method. Check sample-ratio mismatch, contamination, missing events, multiple testing, and novelty effects. Interpret effect size and interval against practical value; a non-significant result does not prove no effect.

Read `references/experiment-playbook.md` for design and `references/statistics-reference.md` for statistical details. Produce a decision-ready test plan or result interpretation with limitations.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/sample_size_calculator.py](scripts/sample_size_calculator.py)
- [references/experiment-playbook.md](references/experiment-playbook.md)
- [references/statistics-reference.md](references/statistics-reference.md)
