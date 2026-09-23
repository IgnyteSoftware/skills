---
name: to-tickets
description: Break an accepted plan into implementable issues with acceptance criteria and dependencies. Use for requested ticket breakdowns; unresolved planning belongs to Wayfinder.
user-invocable: false
---

# To tickets

Read the accepted plan or specification and inspect relevant project conventions. Use project-setup only if a needed tracker decision is unresolved. Organize milestones by the user's intended outcomes or versions when requested.

If material scope decisions remain, use [wayfinder](../wayfinder/SKILL.md) to resolve them or label dependent drafts blocked. Do not convert an unresolved choice into an implementation requirement. Separate development prerequisites from integration and release gates so independent work remains available.

Prefer independently verifiable slices of behavior. Make blockers explicit and avoid arbitrary ticket counts. For changes that cannot land independently, use a safe expand, migrate, remove sequence or explain the required integration boundary. Include preparatory work only when the accepted change needs it.

Give each ticket a deliverable, acceptance criteria, exclusions, and dependencies. Make material scope choices explicit and keep decision-dependent tickets blocked. Publish only within the authorized scope, reusing approval already given, with native dependency links where supported; otherwise include explicit references. Verify created issues and links against the installed tracker tooling; identifiers and dependency APIs differ by platform. Keep a local draft when publication is not authorized.

Return the ordered breakdown and what is unblocked. Do not close or rewrite a parent issue unless that action is part of the request.
