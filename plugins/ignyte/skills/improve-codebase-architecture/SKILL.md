---
name: improve-codebase-architecture
description: Find and compare structural improvements within a specified codebase area. Use for architecture assessment or demonstrated design friction, not routine opportunistic refactoring.
user-invocable: false
---

# Improve codebase architecture

Inspect the requested area, its callers, and relevant ADRs. Use codebase-design to assess coupling, confusing interfaces, scattered responsibilities, and failure paths. Ground each candidate in an observed maintenance or behavior problem.

Compare doing nothing, a smaller correction, and a structural change when they are credible alternatives. Explain the affected contracts, migration risks, and how behavior would be verified. Distinguish necessary fixes from speculative cleanup.

Present the strongest candidates in the format the user requested. Use a diagram or prototype when it resolves uncertainty; an HTML report is optional. Ask about product tradeoffs only when they block the choice.

Finish with a recommendation and its evidence. An assessment does not authorize a refactor; proceed only within accepted implementation scope and record consequential decisions through domain-modeling.
