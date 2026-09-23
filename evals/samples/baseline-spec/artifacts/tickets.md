# Appointment scheduling map and ticket drafts

## Destination

A reviewable scheduling specification and dependent delivery drafts, with consequential product decisions explicit. The current spec is [Appointment scheduling spec](spec.md). The route is not fully clear while the decision tickets below remain open.

## Notes

This combined file is the local draft location expressly requested by TASK.md. It replaces skill defaults for tracker publication, separate issue files, claims, and ready-for-agent labels. Nothing here is published or approved for implementation. There is no live human interview, so HITL decisions remain open. Reviewers should approve the testing seam, ticket granularity, and blocking edges as well as product rules.

Use the supplied Wayfinder, grilling, domain-modeling, research, to-spec, to-tickets, and unslop skills. Local-only research and no delegation override the skills' subagent defaults. Domain terminology comes from the existing domain document; no new glossary or ADR is needed until a decision is actually accepted.

## Decisions so far

No new business decisions were resolved in this session. [Existing decisions](../decisions.md) remain settled. [Interval evidence](spec.md#sources-and-local-research) confirms a defect that can be planned independently of emergency policy. It is a factual finding, not a product-policy resolution.

## Decision frontier

Open and unclaimed human decision tickets currently available for review:

- [Set emergency displacement policy](#set-emergency-displacement-policy)
- [Set appointment lifecycle and reservation rules](#set-appointment-lifecycle-and-reservation-rules)
- [Confirm actor identity and role mapping](#confirm-actor-identity-and-role-mapping)
- [Confirm time-entry behavior](#confirm-time-entry-behavior)

A decision blocks only its dependent work. Emergency policy does not gate ordinary scheduling or access control. No HITL decision is considered answered by this draft.

## Not yet specified

If displacement is allowed, the resulting displaced-customer workflow and recovery experience need elaboration after the owner chooses the policy. The details of deployment identity depend on the selected trusted identity mapping. Record resulting questions as new dependent tickets when they become precise; do not select a provider now.

## Out of scope

Production changes in this planning task, publication, commits, pushes, automated assignment, customer login, billing, and release execution. Azure hosting and manual intake do not imply a GitHub or PR workflow.

## Set emergency displacement policy

Type: wayfinder:grilling, HITL. Status: open, needs business owner. Blocked by: none.

Question: May an emergency job displace an already confirmed appointment? Compare preserving the commitment and requiring a coordinator to find another slot against explicitly allowing displacement with accountable human action. The supplied brief gives no basis for choosing the business priority.

Recommendation: Keep this decision open. Ask the owner to choose using a concrete case: a confirmed visit occupies 10:00 to 11:00 and an emergency request needs that same technician at 10:30. Do not treat preserving the current system's behavior as the approved emergency policy.

Resolution criteria:

- [ ] Owner chooses whether displacement is permitted and records rationale.
- [ ] If permitted, follow up on who authorizes it, which appointments qualify, whether affected visits move or cancel, and who handles the affected customer. These are conditional questions, not assumed answers.
- [ ] The spec and any subsequent emergency delivery draft reflect the answer and preserve IDs, audit, and concurrency guarantees.

Blocks: [Handle emergency requests under approved policy](#handle-emergency-requests-under-approved-policy). Does not block ordinary workflows.

## Set appointment lifecycle and reservation rules

Type: wayfinder:grilling, HITL. Status: open, needs operations/product owner. Blocked by: none.

Questions for the current frontier:

1. Which statuses reserve a technician's time? Recommendation for review: confirmed and in_progress reserve time, cancelled does not; explicitly decide drafts and historical completed intervals. This is not adopted.
2. Which states permit cancellation, rescheduling, or reassignment, and does rescheduling retain confirmation? Recommendation for review: state the permitted transitions explicitly and retain the prior record on any failed change.
3. What are the allowed exceptions for arrival/completion, correction, early or late arrival, and overruns? Can a coordinator act on behalf of a technician? Recommendation for review: preserve planned times and record actual events separately; do not imply exceptions from the UI.
4. What must a draft contain, and how should normal status changes supply the audit reason? Recommendation for review: validate the required fields before confirmation and define reason entry by action.

Resolution criteria:

- [ ] Approved actor/transition matrix covers every existing status, including prohibited transitions and any correction path.
- [ ] Reservation status set and draft requirements are explicit.
- [ ] Rules cover cancel during work, reschedule after completion, reassignment during an open technician screen, overrun, and repeated completion.
- [ ] Approve or revise the spec's proposed transitions and audit reason behavior.

Blocks: ordinary booking, rescheduling/cancellation, technician progress, and emergency delivery. Does not block read-only assignment visibility or the established interval correction.

## Confirm actor identity and role mapping

Type: wayfinder:grilling, HITL with technical fact follow-up. Status: open, needs client identity owner. Blocked by: none.

Question: What trusted identity source supplies the coordinator role and technician identity in the deployed appointment service? The fixture does not contain that implementation. Recommendation: reuse the client's established authenticated identity and enforce roles in the service; do not introduce a provider on the strength of Azure hosting alone.

Resolution criteria:

- [ ] Owner identifies the existing identity mechanism and authoritative mapping to roles and technician IDs.
- [ ] Define denied-access and role-change behavior without exposing hidden appointments.
- [ ] A reviewer approves how the service derives the actor for permission checks and audit.

Blocks: all user-facing delivery drafts. Local overlap correction does not need this decision.

## Confirm time-entry behavior

Type: wayfinder:grilling, HITL. Status: open, needs operations/product owner. Blocked by: none.

Question: Should an ambiguous daylight-saving local time require the coordinator to select the intended occurrence, or should entry be disallowed? Recommendation: require an explicit occurrence/offset choice and show the zone. Reject nonexistent local times and invalid zones. Never choose silently.

Resolution criteria:

- [ ] Owner approves the ambiguous-time interaction and display needed by coordinators and technicians.
- [ ] A concrete ambiguous, nonexistent, and cross-midnight example has an agreed user-visible outcome.

Blocks: ordinary booking and schedule editing. Existing stored appointments can be displayed with their explicit zone and resolved instant without deciding new time-entry policy.

## Correct shared interval boundaries

Type: delivery draft, prerequisite repair. Status: draft, independent work specified; implementation not authorized here. Blocked by: none.

What to build: make the existing scheduling helper accept touching endpoints while still rejecting genuine same-resource overlap. This is a narrow prerequisite repair, not a UI or database layer project.

- [ ] Existing adjacency, overlap, containment, and independent-resource checks pass.
- [ ] The helper uses the established half-open contract without changing the resource-independent behavior.
- [ ] Positive-interval validation responsibility is made explicit at the scheduling entry point; do not claim the existing five checks cover invalid intervals.
- [ ] The review records that the original fixture check failed before the correction.

Verification: run the existing checks. Add no tests without developer request. This repair alone does not prove prevention of concurrent service double-booking.

## Show assignments with enforced visibility

Type: delivery draft. Status: blocked draft.

Blocked by: [Confirm actor identity and role mapping](#confirm-actor-identity-and-role-mapping).

What to build: let technicians read their own appointment list and details, while coordinators read all appointments, using the existing read interface and service-side authorization. This is demoable with pre-existing appointments.

- [ ] List and direct lookup enforce the same access rule.
- [ ] A technician cannot obtain another technician's appointment/customer data by changing an identifier.
- [ ] Reassignment removes the former technician's access on the next request.
- [ ] Empty, denied, missing, and changed-assignment outcomes are usable and disclose no hidden records.
- [ ] Detail views show the appointment's explicit zone and resolved scheduled times.

Verification proposal: exercise reads through the service as coordinator and as two different technicians, then verify the visible UI outcomes. No new tests are authorized by this ticket draft.

## Create and confirm a conflict-safe appointment

Type: delivery draft. Status: blocked draft.

Blocked by: [Correct shared interval boundaries](#correct-shared-interval-boundaries), [Set appointment lifecycle and reservation rules](#set-appointment-lifecycle-and-reservation-rules), [Confirm actor identity and role mapping](#confirm-actor-identity-and-role-mapping), [Confirm time-entry behavior](#confirm-time-entry-behavior).

What to build: let a coordinator create, assign, and confirm an appointment through the service and coordinator UI, with validation, audit, revision feedback, and authoritative technician conflict checks. This slice supplies its own create/detail result and need not wait for technician read UI.

- [ ] Valid input creates an appointment with stable ID and expected domain fields.
- [ ] Only a coordinator assigns a technician; status and required fields follow the approved policy.
- [ ] Invalid intervals or unresolved times cannot commit.
- [ ] Same-technician true overlap is rejected; adjacency and independent technicians are accepted.
- [ ] Competing writes for distinct appointments cannot both reserve overlapping technician time.
- [ ] A durable audit record accompanies a successful change, and failure leaves no partial appointment/audit result.
- [ ] Stale revision and conflict responses preserve unsaved input and support reload/review.

Verification proposal: use the appointment service seam and two competing requests, then demonstrate the coordinator path. Inspect actual persistence support before selecting conflict serialization; per-appointment revision checks are insufficient on their own.

## Reschedule and cancel with retained history

Type: delivery draft. Status: blocked draft.

Blocked by: [Create and confirm a conflict-safe appointment](#create-and-confirm-a-conflict-safe-appointment).

What to build: let a coordinator change or cancel an eligible appointment while preserving identity, history, and the approved reservation policy. Lifecycle, identity, and time-entry decisions are inherited through the blocker.

- [ ] Rescheduling retains ID, excludes itself from conflict checking, and rechecks a newly assigned technician.
- [ ] A conflicting or stale change preserves the original appointment and reservation.
- [ ] Cancellation records the reason, retains the appointment, and affects availability only as approved.
- [ ] No visit can be deleted after confirmation.
- [ ] Revision, actor, changed fields, and reason remain available through the appointment audit view.
- [ ] Unauthorized or prohibited-state attempts leave the record unchanged.

Verification proposal: demonstrate successful and rejected changes, competing edits, and the resulting history through the service and coordinator UI.

## Record technician arrival and completion

Type: delivery draft. Status: blocked draft.

Blocked by: [Show assignments with enforced visibility](#show-assignments-with-enforced-visibility), [Set appointment lifecycle and reservation rules](#set-appointment-lifecycle-and-reservation-rules).

What to build: let the assigned technician record arrival and completion from an existing eligible appointment. It can use existing appointment fixtures and does not depend on the new coordinator booking screen.

- [ ] Approved transitions update status and record actor, reason, and event time under the approved event policy.
- [ ] The service checks current assignment, state, and revision at commit.
- [ ] Reassignment while the screen is open prevents the former technician's update.
- [ ] Repeated, prohibited, or stale actions do not duplicate transitions or silently overwrite work.
- [ ] Audit failure leaves no unaudited status change; uncertain responses support reload.
- [ ] Planned times remain intact unless the owner has explicitly approved different behavior.

Verification proposal: exercise the transition interface as assigned and unassigned technicians, including competing coordinator edits, and demonstrate the visible progress state.

## Handle emergency requests under approved policy

Type: conditional delivery placeholder. Status: blocked and not sized for implementation.

Blocked by: [Set emergency displacement policy](#set-emergency-displacement-policy), [Create and confirm a conflict-safe appointment](#create-and-confirm-a-conflict-safe-appointment).

What to build: cannot be finalized until the owner answers whether displacement is permitted. Keep this named dependency visible without pretending that either branch has been selected.

- [ ] Replace this placeholder with a reviewable vertical slice after the policy decision.
- [ ] If displacement is prohibited, specify the coordinator's emergency-conflict outcome without moving a confirmed appointment.
- [ ] If displacement is allowed, resolve authorization, affected-visit treatment, and recovery before drafting implementation. Add a dependency on schedule editing only if that chosen behavior uses it.
- [ ] Preserve IDs, audit, no silent overwrite, and consistent reservations for every affected appointment.

## Review and authorize release

Type: human gate. Status: blocked draft.

Blocked by: all delivery slices selected for the release, their supporting decisions, and evidence from their acceptance scenarios. Emergency delivery joins this gate only if selected for release; deferring it requires an explicit scope decision from the owner.

- [ ] Human reviews this spec, testing seam, draft granularity, and dependency graph before implementation intake.
- [ ] Requested delivery behavior is verified, including authorization and concurrent booking outcomes.
- [ ] Known check failures are resolved for delivery; a parse or mock demonstration alone is not a release claim.
- [ ] Human approval is recorded before release through the manual Azure/client workflow. No publication, commit, push, or PR follows from this planning document.
