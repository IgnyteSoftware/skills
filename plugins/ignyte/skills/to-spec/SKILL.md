---
name: to-spec
description: Draft a specification from settled scope and decisions. Use for small agreed changes or as Wayfinder's drafting step; substantial discovery and interconnected specifications belong to Wayfinder.
user-invocable: false
---

# To spec

Use the conversation, current code, domain vocabulary, and relevant decisions. Preserve unresolved questions as such; use grilling only when a consequential decision blocks a useful specification.

State the problem, desired behavior, acceptance criteria, constraints, and exclusions. Include interfaces, examples, and verification expectations when they make the contract clearer. Scale detail to the change; do not force long user-story lists or invent testing scope.

For a substantial feature, check complete user workflows, domain states, permissions, integrations, and failure/recovery behavior. Trace acceptance back to requested outcomes and accepted decisions. Resolve contradictions across sections before handoff. Keep open decisions visible with their consequences; blocked sections and dependent tickets are not ready for implementation. Use [wayfinder](../wayfinder/SKILL.md) when discovery is still needed rather than inventing decisions to finish the document.

Respect existing issue and document conventions. Use project-setup only for conventions that remain ambiguous after inspection. Draft locally or in the response unless publication is authorized; then publish to the agreed tracker and verify the result.

Done means an implementer can distinguish acceptable behavior from out-of-scope work. Return the spec and any open decisions, and continue with other outcomes the user requested.
