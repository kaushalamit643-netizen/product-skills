# Product Skills for Codex

17 local skills for product strategy, discovery, delivery, research, analytics, design, and implementation. Each folder includes a focused `SKILL.md`, Codex interface metadata, and its supporting resources. The 22 Python helpers use the standard library and require Python 3.9 or newer.

## Files

- `skills/`: Codex-ready skills, templates, references, and helpers.
- [Validation results](VALIDATION.md): checks performed and their limits.


## Skills

| Skill | Purpose |
| --- | --- |
| [agile-product-owner](skills/agile-product-owner/SKILL.md) | Write stories, refine backlogs, and plan sprints |
| [apple-hig-expert](skills/apple-hig-expert/SKILL.md) | Audit Apple UI, contrast, targets, and accessibility |
| [code-to-prd](skills/code-to-prd/SKILL.md) | Document implemented product behavior from source code |
| [competitive-teardown](skills/competitive-teardown/SKILL.md) | Compare competitors using evidence and scoring |
| [experiment-designer](skills/experiment-designer/SKILL.md) | Design experiments and estimate required samples |
| [landing-page-generator](skills/landing-page-generator/SKILL.md) | Build responsive landing pages with clear product copy |
| [product-analytics](skills/product-analytics/SKILL.md) | Define KPIs and analyze retention, cohorts, funnels |
| [product-discovery](skills/product-discovery/SKILL.md) | Validate opportunities and prioritize assumptions |
| [product-manager-toolkit](skills/product-manager-toolkit/SKILL.md) | Prioritize features and write evidence-based PRDs |
| [product-skills](skills/product-skills/SKILL.md) | Route product work and review discovery evidence |
| [product-strategist](skills/product-strategist/SKILL.md) | Define product strategy and align measurable OKRs |
| [research-summarizer](skills/research-summarizer/SKILL.md) | Summarize research and compare evidence with citations |
| [roadmap-communicator](skills/roadmap-communicator/SKILL.md) | Write roadmaps, release notes, and stakeholder updates |
| [saas-scaffolder](skills/saas-scaffolder/SKILL.md) | Scaffold SaaS foundations with auth, data, and billing |
| [spec-to-repo](skills/spec-to-repo/SKILL.md) | Implement a product spec as a working local project |
| [ui-design-system](skills/ui-design-system/SKILL.md) | Create tokens, component rules, and design handoffs |
| [ux-researcher-designer](skills/ux-researcher-designer/SKILL.md) | Plan research, synthesize findings, and map journeys |

## Use with Codex

Copy selected skill folders into your target project's `.agents/skills/`, or your user-level `~/.agents/skills/`. Keep each skill folder intact. For the `product-skills` router, copy all 17 sibling folders together. The `skills/` folder in this repository is a distribution source; it does not by itself install these skills.

Invoke a skill by name, for example: `$product-manager-toolkit prioritize this feature list`. Automatic selection remains enabled. Paths to helpers and references are resolved from the installed skill location.


## Validate

```sh
python3 scripts/validate_bundle.py
python3 scripts/smoke_helpers.py
```

This checks the bundle and helper entrypoints; it does not certify generated applications, research conclusions, or statistical methods.

