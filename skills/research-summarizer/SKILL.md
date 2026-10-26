---
name: research-summarizer
description: "Summarize supplied papers, articles, reports, and documentation; compare source findings and extract citations. Use for evidence-grounded briefs about identified sources rather than open-ended source discovery."
---

# Research Summarizer

Read the supplied sources, using available file, document, or browser tools for their actual format. For links, retrieve the underlying content; disclose inaccessible sections instead of summarizing from a title or snippet.

Identify thesis, methods, findings, limitations, and implications. Tie claims to source pages or sections, preserve qualifications and conflicting evidence, and distinguish the author's conclusions from your inference. Assess evidence in its field context rather than assigning credibility from age alone.

Use `scripts/format_summary.py` to produce a blank outline if useful; it does not summarize source content. Use `scripts/extract_citations.py` on extracted text as a candidate detector. Review matches and missing metadata manually; regex counts do not prove bibliography completeness.

For comparisons, align questions, methods, populations, and outcomes before synthesizing consensus or disagreement. Read `references/summary-templates.md` and `references/citation-formats.md` as needed. Never invent author, publication, DOI, sample size, or findings.

## Resource use

Resolve this skill directory from the loaded `SKILL.md` path. Read supporting files only when needed. Run bundled helpers with `python3` using their absolute paths and keep the working directory and outputs in the user's target project. Read `--help` before selecting arguments; sample/demo modes are illustrative. The helpers use Python's standard library.

Read [references/workflows.md](references/workflows.md) for detailed domain methods and examples. The workflow above governs scope, evidence handling, and execution.

## Bundled resources

- [scripts/extract_citations.py](scripts/extract_citations.py)
- [scripts/format_summary.py](scripts/format_summary.py)
- [references/citation-formats.md](references/citation-formats.md)
- [references/summary-templates.md](references/summary-templates.md)
