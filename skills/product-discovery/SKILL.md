---
name: product-discovery
description: "Validate product opportunities, map risky assumptions, plan customer discovery, and build opportunity solution trees. Use before committing to a product solution or when evidence is uncertain."
---

# Product Discovery

Anchor discovery to one measurable outcome with baseline and horizon. Separate customer needs and problems from proposed features.

Build an opportunity solution tree linking outcome, evidence-backed opportunities, alternative solutions, and assumption tests. Preserve competing explanations rather than treating a single interview as proof.

Map desirability, viability, feasibility, and usability assumptions by impact if wrong and evidence strength. Use `scripts/assumption_mapper.py` to prioritize the supplied assumptions, then choose the smallest useful test of the riskiest uncertainty.

Create a bounded discovery plan with question, participants or data, method, success/failure criteria, owner, and decision date. Return a proceed, pivot, stop, or gather-more-evidence recommendation tied to actual findings. Read `references/discovery-frameworks.md` for methods.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/assumption_mapper.py](scripts/assumption_mapper.py)
- [references/discovery-frameworks.md](references/discovery-frameworks.md)
