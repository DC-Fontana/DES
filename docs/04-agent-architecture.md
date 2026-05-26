# 04 — Agent Architecture

## Internal specialist agents

- **Architect:** system design and tradeoff decisions.
- **Engineer:** code generation, debugging, implementation plans.
- **Researcher:** external knowledge synthesis and source validation.
- **Creative Director:** UX language, tone, branding, interaction style.
- **Business Analyst:** prioritization, ROI framing, scope management.
- **Planner:** task breakdown and sequencing.
- **Memory Manager:** summarization, storage strategy, retrieval relevance.

## Coordinator pattern

1. User voice/text request enters coordinator.
2. Intent classifier determines required specialists.
3. Specialists run in parallel with shared context snapshot.
4. Conflict resolver merges outputs into one response.
5. Final response includes: recommendation, actions, approvals required.

## Guardrails

- Sensitive tools require policy approval gates.
- Agent outputs are scored for confidence + consistency.
- Hallucination checks on external claims.
