---
name: wayfinder
description: Turn an incomplete idea into a coherent specification and actionable plan, or create and resume shared decision maps. Use for product discovery, interconnected decisions, release milestones, and planning that needs research or prototypes.
user-invocable: false
---

# Wayfinder

Own the whole specification, not just its task list. Establish the users, desired outcomes, scope, client constraints, and requested stopping point. Inspect the current implementation and prior decisions. Identify interconnected choices and the uncertainties that block useful progress.

Use [research](../research/SKILL.md) for facts, [prototype](../prototype/SKILL.md) for observable behavior, [grilling](../grilling/SKILL.md) for consequential user choices, and [domain-modeling](../domain-modeling/SKILL.md) for terms and rules. Answer discoverable questions from evidence before asking the user. Work through independent decisions while blocked choices remain open. Record decisions and their implications; when evidence changes one, update every affected part of the plan.

Keep technical inspection separate from human product decisions. Reuse behavior entailed by settled requirements instead of asking the user to approve it again. Attach each open question only to work it actually blocks; distinguish implementation prerequisites from later integration or release gates.

Use [to-spec](../to-spec/SKILL.md) to assemble requested specifications. Cover the relevant end-to-end workflows, domain states and rules, permissions, integrations, failure/recovery behavior, constraints, and observable acceptance. Review the document as a whole against the original outcomes and decisions: find contradictions, missing behavior, and unsupported assumptions. Label unresolved choices and their affected sections; a polished draft with blocking decisions is not implementation-ready.

Only then use [to-tickets](../to-tickets/SKILL.md) for requested issue breakdowns. Map slices to acceptance criteria, expose dependencies, and mark decision-dependent work blocked. Organize milestones or versions when requested. Keep artifacts in existing project conventions; a new tracker or issue hierarchy is not a prerequisite.

When several agents share a tracker, follow its claim convention to avoid duplicate work. Keep unresolved questions distinct from excluded scope.

When creating or continuing a shared decision map, including an existing `wayfinder:map`, follow [the map lifecycle](references/decision-maps.md). Preserve its canonical decisions and tracker relationships rather than replacing it with a disconnected spec. Ordinary planning does not require a map.

Continue through unblocked decisions rather than stopping after an arbitrary number of tickets. Finish with the plan, decisions, unresolved questions, and the next actionable work. Planning alone does not authorize implementation; when implementation is already authorized, proceed once the relevant decisions are settled.
