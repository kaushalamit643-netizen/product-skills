---
name: landing-page-generator
description: "Build a landing page in a local project using product positioning, copy frameworks, responsive sections, and SEO metadata. Use for page implementation or scaffolding, following the existing stack."
---

# Landing Page Generator

Inspect the target project, brand references, product audience, value proposition, and primary CTA. Follow the user's stack and the project's component system; do not replace it with a default framework.

Choose PAS, AIDA, or BAB when useful. Draft accurate benefits and concrete copy, then implement only the sections appropriate to the product. Do not invent testimonials, logos, adoption metrics, guarantees, or pricing.

`scripts/landing_page_scaffolder.py` can generate TSX or HTML from JSON. Inspect generated imports, dependencies, interaction behavior, escaping, and links before integrating. Read `references/landing-page-patterns.md`, `references/copy-frameworks.md`, and `references/conversion-patterns.md` as needed.

Verify keyboard access, responsive layout, CTA behavior, semantic headings, image dimensions/alt text, and applicable metadata. Use `references/seo-checklist.md` for SEO; measure performance before claiming targets are met. Deliver local files and verification results. Publishing requires the user's request.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/landing_page_scaffolder.py](scripts/landing_page_scaffolder.py)
- [references/conversion-patterns.md](references/conversion-patterns.md)
- [references/copy-frameworks.md](references/copy-frameworks.md)
- [references/landing-page-patterns.md](references/landing-page-patterns.md)
- [references/seo-checklist.md](references/seo-checklist.md)
