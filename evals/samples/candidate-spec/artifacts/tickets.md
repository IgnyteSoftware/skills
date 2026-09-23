# Local ticket drafts

Source: [specification](spec.md). These are local planning artifacts, not published issues or implementation authorization. Spec acceptance IDs and decision IDs are authoritative. Human review applies to the complete draft. No dates, tracker setup, PRs, or release automation are implied.

## T1 — Correct half-open overlap behavior

Deliverable: a surgical correction to the shared helper that permits touching endpoints while retaining resource isolation. Validate positive intervals at the owning boundary identified in T2; do not add speculative helper responsibilities.

Acceptance: A3; the five existing checks pass, including both currently failing adjacency cases. Demonstrate true overlap and containment still reject and separate rooms remain independent. This ticket can be implemented without emergency, draft, or overrun policy decisions.

Dependencies: none. Integration dependency: technician scheduling consumes this rule through T4. Exclusions: production appointment API, state selection, room UI, and new tests unless requested.

## T2 — Inspect service contracts and define integration boundaries

Deliverable: confirm actual appointment persistence, read/create/update contracts, role/assignment source, revisions, zone conversion, durable audit transaction, and ambiguous-create recovery. Record precise gaps and the smallest changes needed for R1/R4/R5. Preserve domain names and existing endpoints where they fit. Specify the explicit technician-resource adapter to the room-keyed helper. This is needed because only a helper is executable in this fixture.

Acceptance: A1/A4/A7/A8 have a concrete contract and rollback strategy; document how two separate appointment confirmations serialize, how assignment changes protect both resources, and how state/revision/audit commit together. Identify whether creation already supports safe deduplication; if not, include it in T4. Record all unknowns without claiming implementation notes prove transactional behavior.

Dependencies: none; no business choice blocks technical inspection. Exclusions: provider calls from this fixture, production changes during planning, a new database choice without evidence, and deciding Q1-Q3.

## T3 — Enforce coordinator and technician access

Deliverable: server-side role and current-assignment authorization for list, direct read, and settled mutations, using the authenticated actor. Expose only authorized actions to clients.

Acceptance: A2; coordinators see all visits, technicians only current assignments, and direct-ID attempts cannot bypass filtering. Check current assignment on progress writes even after a stale UI read. Unauthorized writes produce no appointment change or successful-change audit. No implicit coordinator override of technician progress is granted.

Development prerequisites: T2 identifies identity and service hooks. Integration: T4/T5 use these checks. Exclusions: customer login, new identity provider, Q3 override permissions. Q1-Q3 do not block settled access enforcement.

## T4 — Atomic ordinary scheduling and coordinator recovery

Deliverable: implement ordinary create/confirm, pre-arrival cancel and reschedule/reassignment, time validation, revision conflict handling, effective audit, and recovery from uncertain responses. Coordinator views support these actions and retain unsaved edits after conflict. Rescheduling retains stable IDs and reserves the new interval atomically with releasing the old one.

Acceptance: A1, A3-A5, A7-A8. Demonstrate adjacent versus overlapping intervals, self-exclusion, two competing confirmations, stale updates, cross-technician reassignment, invalid/DST inputs, audit failure rollback, cancellation freeing capacity, and retry/readback after response loss. All rejected operations preserve prior state.

Development prerequisites: T2 for the persistence contract. Interval enforcement depends on T1; secured integration depends on T3. Independent work on confirmed/in-progress scheduled intervals, UTC validation, transactions, audit, conflict UI, and safe recovery can proceed without Q1-Q3. Complete reservation filtering/draft abandonment integration waits for T6; exceptional/historical occupancy integration waits for T7. These are integration gates for the dependent portions, not reasons to postpone this entire ticket.

Exclusions: emergency displacement, automatic alternative-slot selection, travel buffers, business-hour policy, and unresolved exceptional transitions.

## T5 — Technician assignments, arrival, and completion

Deliverable: technician list/detail and the settled progress actions `confirmed -> in_progress -> completed`. Preserve scheduled time and record actual event time with authenticated actor and audit reason. Show clear success, stale state, unauthorized, and uncertain-response outcomes.

Acceptance: A2/A6/A8. Assigned technician completes the ordinary sequence; premature completion, repeated effective transition, invalid state, and stale assignment do not mutate records. Refetch authoritative state after timeout and prevent silent overwrites. Appointment zone is visible.

Development prerequisites: T2 for contract/actual-event storage and T3 for service access checks. A coordinator UI or emergency policy is not a prerequisite; use existing valid confirmed appointments to develop this slice. Integration dependency: T4's atomic revision/audit behavior, or the equivalent existing service guarantees verified by T2. Q3 blocks only exceptional progress/occupancy behavior, not ordinary arrival/completion.

Exclusions: coordinator progress override, offline sync, reopening, and emergency controls.

## T6 — Decide and integrate draft capacity policy

Status: decision-dependent portion blocked by Q2. Deliverable: business owner records whether drafts reserve, how reservations are released if applicable, and whether/how drafts are abandoned; then update spec R3, draft transitions, acceptance, and T4 reservation filtering/UI.

Acceptance: owner-selected behavior has observable examples for draft save, competing confirmation, abandonment, and any chosen expiry. Confirmation always rechecks capacity atomically. No silent draft policy is inferred from the word draft.

Dependencies: Q2 for policy implementation; T2/T4 for integration. Independent work: document current draft behavior during T2. Exclusions: inventing expiry or assuming deletion permission, and changing confirmed-record retention.

## T7 — Decide and integrate exceptional lifecycle and occupancy policy

Status: decision-dependent portion blocked by Q3. Deliverable: decide after-arrival cancellation/reassignment, correction/reopening authority, overrun capacity behavior, and historical/completed collision rules. Update transitions, authorization, reservation selection, and acceptance together; implement only the accepted exceptional behavior in a later implementation task.

Acceptance: accepted examples cover each allowed/forbidden exceptional action with actor, reason, retained history, revision handling, and occupancy effect. Scheduled-time conflict prevention is not described as guaranteeing absence of physical overruns. No correction deletes confirmed history or silently rewinds state.

Dependencies: Q3 for policy; T3-T5 for integration with ordinary behavior. Independent work: inspect existing constraints in T2. Exclusions: emergency displacement (T8) and using unresolved exceptions to delay ordinary technician workflow.

## T8 — Resolve emergency displacement and draft the selected slice

Status: blocked by Q1. Deliverable: record the business owner's choice. If disallowed, specify visible conflict handling with ordinary alternatives. If allowed, first settle authorized actor, eligible appointments, displaced disposition/placement, contact responsibility, and audit/recovery rules; then revise the spec and this ticket into implementable behavior. Do not presume automatic cancellation or emergency priority bypass.

Acceptance: A9 is replaced with acceptance for the selected policy; ordinary no-double-booking, stable IDs, audit, and concurrency remain true. An allowed displacement needs all affected appointment changes to succeed atomically or preserve prior bookings. A disallowed displacement must not mutate the existing appointment. Any new state or communication obligation requires explicit approval.

Dependencies: Q1 and its conditional follow-ups for design; T3/T4 for eventual integration. T6/T7 are dependencies only if the chosen emergency policy uses their draft or exceptional states. Exclusions: silently deciding the tradeoff, notifications by an unspecified provider, and blocking ordinary scheduling on emergency policy.

## T9 — Integrated evidence and human release review

Deliverable: validate the integrated chosen behavior against A1-A9, record results and limitations, and give the human reviewer the local diff and base revision. No release occurs without human approval.

Acceptance: existing checks pass after T1; actual service evidence covers authorization, atomic collision prevention across appointments, stale revisions, timezone edge cases, rollback, technician sequence, and safe recovery. Document decision answers and any remaining unsupported paths honestly. Human approval is recorded before release.

Dependencies: T1-T5 for standard-path integration; T6-T8 for the full requested feature's unresolved policies. Evidence collection for completed independent slices can begin before those decisions. A narrower release requires explicit owner agreement; it is not chosen by this plan. Exclusions: adding tests without a developer request, PRs, publication, commits, pushes, and deployment from this task.

## Dependency review and next work

T1 and T2 have no product-decision prerequisites. After T2, T3 and the independent parts of T4/T5 can proceed; T1 and T3 are integration requirements for ordinary scheduling. T6/Q2 and T7/Q3 govern only their named draft/exception paths. T8/Q1 governs emergency displacement. T9 collects actual integration evidence and keeps human release approval distinct from development dependencies. All tickets remain local drafts for review.
