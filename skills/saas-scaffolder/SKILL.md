---
name: saas-scaffolder
description: "Scaffold a local SaaS application with the requested authentication, data, billing, and UI stack. Use for SaaS project foundations; use spec-to-repo for general applications."
---

# SAAS Scaffolder

Extract the requested product scope, stack, auth provider, data model, billing model, and tenancy rules. Respect existing code and explicit preferences. Plan a minimal working slice with server-side authorization boundaries.

Use `scripts/project_bootstrapper.py` to preview or generate an initial structure. It produces a starting scaffold, not a complete or production-verified application; inspect and complete generated files. Read `references/tech-stack-comparison.md` for choices and `references/saas-architecture-patterns.md` or `references/architecture-patterns.md` for structure.

Read `references/auth-billing-guide.md` before implementing billing. Validate price selection on the server, verify webhook signatures, handle retries idempotently, and derive entitlements from trusted state. Keep secrets out of source and document required configuration in `.env.example`.

Verify implemented user flows, authorization, dependency/API compatibility, migrations, and relevant build/tests in the available environment. Report setup still required. Do not create live accounts, charge customers, apply production migrations, or deploy without authorization.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/project_bootstrapper.py](scripts/project_bootstrapper.py)
- [references/architecture-patterns.md](references/architecture-patterns.md)
- [references/auth-billing-guide.md](references/auth-billing-guide.md)
- [references/saas-architecture-patterns.md](references/saas-architecture-patterns.md)
- [references/tech-stack-comparison.md](references/tech-stack-comparison.md)
