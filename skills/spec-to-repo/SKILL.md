---
name: spec-to-repo
description: "Turn a product specification into working local application code with configuration, documentation, and verification. Use for building from a spec or PRD, across the user-selected stack."
---

# Spec To Repo

Read the specification and inspect the destination repository. Identify the acceptance criteria, user flows, data contracts, integration boundaries, and explicit technology choices. Resolve only material ambiguities; state routine assumptions and proceed within the authorized scope.

Map requirements to a compact architecture and implementation plan. Read `references/spec-parsing-guide.md` for requirement extraction and `references/stack-templates.md` only for relevant stack examples. Check current official dependency documentation when implementing version-specific APIs.

Implement complete behavior for the agreed scope. Include configuration examples, appropriate secret/build ignores, and setup instructions. Do not present placeholder functions or simulated integrations as finished features.

Run `scripts/validate_project.py` for structural checks, then the project's applicable build and behavior tests. The structural checker does not establish functional correctness. Verify acceptance criteria and report real limitations or missing credentials. Continue through the authorized deliverable; do not impose an arbitrary MVP approval stop.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/validate_project.py](scripts/validate_project.py)
- [references/spec-parsing-guide.md](references/spec-parsing-guide.md)
- [references/stack-templates.md](references/stack-templates.md)
