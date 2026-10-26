# Validation results

Validated locally on 27 October 2026 with Python 3.9.6.

- All 17 skills pass the bundled skill-creator `quick_validate.py` frontmatter and scaffold checks.
- All 17 have valid Codex interface metadata, invocation prompts, and focused entrypoints.
- All 22 helpers parse and return successful `--help` output from a separate working directory.
- All 24 smoke scenarios pass, covering every helper, including analysis and documentation generation, landing-page output, a local SaaS scaffold, and retention/cohort/funnel calculations.
- A controlled two-user fixture produces 50% day-one retention and 50% signup conversion.
- All 16 router lanes resolve to existing sibling skills; ambiguous and no-signal exit codes are checked. Moving the router and its target to another directory still resolves correctly.
- Local Markdown resource links resolve. Output templates and fenced examples intentionally contain paths for artifacts created later and are excluded from the link check.
- The 17 skills and their functional resources are retained. Saved source snapshots have also been cleaned. The product router no longer requires context forking, an external harness, or other source-repository directories.
- Outdated design-token and interview-analyzer command examples were corrected to use the current bundled CLI flags.

Run `python3 scripts/validate_bundle.py` to repeat the package, helper-entrypoint, and router checks. Run `python3 scripts/smoke_helpers.py` to repeat all 24 smoke scenarios. Smoke scenarios were executed against temporary local fixtures; no application dependencies were installed and no external services were called.

These checks establish packaging and local helper behavior. They do not certify generated applications as production-ready, validate the example research data, confirm current third-party API compatibility, or establish completeness of heuristic source-code and citation analysis.

No global skill installations were performed.
