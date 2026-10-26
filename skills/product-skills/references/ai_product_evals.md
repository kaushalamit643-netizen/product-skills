# AI Product Evals — the new PRD quality contract

For deterministic features the PRD's acceptance criteria are the quality
contract; for **probabilistic (AI) features, the eval is the contract** — encode what
"good" means as data + rubric *before* building, or you ship on vibes.

## Evals are the new PRD

The PM owns three artifacts per AI feature:

1. **Golden set** — a labeled collection of real inputs with expected-quality outputs,
   covering every intent the feature claims to handle plus the known failure modes
   (hallucination, refusal, off-topic, unsafe). Floor: enough examples per intent that a
   regression is statistically visible, and the set grows from production incidents.
2. **Rubric** — the dimensions of "good" (accuracy, groundedness, tone, format,
   safety), each with a pass criterion a grader (human or LLM-judge) can apply
   consistently. Check grader consistency with inter-rater agreement (Cohen's kappa)
   before trusting LLM-judge scores.
3. **Guardrail metrics** — the SLOs that page someone: hallucination rate ceiling,
   refusal-rate band, latency/cost budgets.

Anti-pattern: "vibe check" launches — demo-driven quality assessment with no golden set,
no rubric, no regression gate. It is the AI equivalent of shipping without tests.

## Model/system cards

Enterprise and regulated buyers expect a model card documenting intended use,
out-of-scope use, eval data and results (disaggregated where bias matters), and
limitations (Mitchell et al.'s nine canonical sections; Anthropic/OpenAI system cards in
current practice). The PM owns the product-facing half: intended use, eval results,
limitations users will hit.

## The loop connection (evaluator-optimizer)

The same generator/critic loop that powers agent harnesses is what PM-owned evals feed:
the golden set + rubric become the evaluator's criteria, and Anthropic's guidance is
explicit that the evaluator-optimizer pattern pays off exactly "when there are clear
evaluation criteria and iterative refinement provides measurable value." Practically:

- Use the eval specification as an acceptance criterion for work on an AI feature.
- Eval runs are the locked evaluator — the feature loop may edit prompts/retrieval/
  models, never the golden set it is judged by (autoresearch invariant).
- Choose analysis appropriate to the eval metric and paired or independent samples;
  the bundled binary-conversion calculator does not analyze arbitrary rubric deltas.

## Where this lands in the domain today

- `experiment-designer` — extend hypothesis gates to eval-delta hypotheses.
- `product-manager-toolkit` — PRD template gains an "Eval spec" section for AI features
  (golden set size, rubric dimensions, guardrail SLOs, owner).
- `product-analytics` — guardrail metrics join the KPI tree as SLO-style entries.

## Sources

1. Lenny's Newsletter, "Beyond vibe checks: A PM's complete guide to evals" —
   
2. Braintrust, "Evals for PMs" — 
3. Aakash Gupta, "AI Evals" — 
4. Mitchell et al., "Model Cards for Model Reporting" (FAT* 2019) —
   
5. Anthropic, "Building Effective Agents" (evaluator-optimizer applicability) —
   
6. Jacob Cohen, "A Coefficient of Agreement for Nominal Scales" (1960) — kappa as the
   inter-rater agreement statistic
