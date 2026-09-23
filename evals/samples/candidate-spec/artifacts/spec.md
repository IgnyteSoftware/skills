# Appointment scheduling specification

Status: reviewed planning draft, with business decisions open. Settled slices can be developed once implementation is authorized; the full feature is not implementation-ready. No production change or release is authorized by this document.

## Outcome and evidence

Operations coordinators can arrange, cancel, and reschedule a customer's technician visit without double-booking a technician. Technicians can find their assignments and record arrival and completion. Failed requests and concurrent edits must leave a clear, recoverable result.

Sources: [brief](../brief.md), [domain](../domain.md), [implementation notes](../implementation.md), [decisions](../decisions.md), [interval rules](../README.md), and [client workflow](../repository-workflow.md). The workflow is the supplied client profile: Azure hosting, local Git without a remote, manual intake, no PR workflow, local human review, and human approval before release. There is no separate client-profile file in this fixture.

Local evidence distinguishes implementation notes from executable behavior:

- The notes report existing read/create/update services, revision-based optimistic concurrency, durable audit, and local time/IANA zone/UTC storage. These service implementations are absent here; their transaction guarantees and contracts still need inspection when implementing.
- `scheduler.py:1-2` exposes `available(bookings, room, start, end)` with inclusive comparisons. `checks.py` and README require half-open intervals and independent rooms. `python -B checks.py` fails at the first adjacency assertion. Evaluating all five existing examples independently yields two failures (earlier/later adjacency) and three matches (overlap, containment, separate room).
- Room isolation is evidence for the helper's current resource key, not a requirement to add room booking to technician scheduling. Integration must pass a technician resource identity or use an explicit adapter; different technicians must remain independent.

## Scope and vocabulary

Customer receives service and has no login. Coordinator assigns technicians and can see all appointments. Technician sees only their current assignments. Appointment retains a stable ID, customer ID, technician ID, local start/end, IANA zone, UTC instants, status, and revision. Status values remain `draft`, `confirmed`, `in_progress`, `completed`, and `cancelled`. Arrival is the transition to `in_progress`; completion is the transition to `completed`.

The audit retains actor, change, and reason. A reschedule changes the existing appointment's scheduled interval or assignment, retaining its ID and history. Emergency displacement means changing an existing confirmed appointment to make space for emergency work; its policy is undecided.

In scope: coordinator scheduling and recovery, technician assignment list/detail and progress recording, server permissions, overlap enforcement, concurrency, and durable audit. Out of scope: customer accounts, billing, automated intake, production implementation during this task, ticket publication, commits, pushes, and deployment. No calendar, notification provider, route planning, travel buffer, room UI, or external integration is introduced. Unresolved emergency behavior is not excluded scope.

## Permissions and interfaces

Enforce permissions in the service on every read and write, including direct-ID access; hiding controls is insufficient. Use the authenticated actor for authorization and audit, never a client-provided actor. Recheck current assignment at mutation time so a reassigned technician cannot update a stale page.

| Actor | Read | Mutations covered by settled scope |
|---|---|---|
| Coordinator | All appointments | Create/edit draft, confirm, cancel/reschedule before arrival, assign technician |
| Assigned technician | Own assignments only | Record arrival for confirmed appointment and completion for in-progress appointment |
| Other technician/customer/unauthenticated caller | No access to that appointment | None |

Coordinator overrides of progress and changes after arrival are Q3. Do not grant those rights implicitly. Authorization failures disclose no other customer's appointment contents.

Reuse existing service contracts where possible. Reads return the current revision and time/zone information. Mutations carry appointment ID (except create), expected revision, requested action/values, and a reason for user-directed schedule changes. Progress actions record the authenticated actor and actual event time; their action is the audit reason. Each response distinguishes success, validation error, forbidden access, stale revision, unavailable technician interval, and unexpected failure. Exact transport paths and error codes are implementation details, not new product APIs required by this draft.

## Workflows and states

1. Coordinator opens the appointment list or a customer visit, enters a valid customer, technician, interval, and zone, and saves a draft through the existing service. Required-field behavior for partially entered drafts follows the existing contract after inspection; do not invent partially valid persisted records. Confirmation validates all fields and reserves the technician interval atomically. Availability shown before submit is advisory.
2. Coordinator opens a confirmed visit and changes its time or technician. Save checks permission, revision, and target availability as one operation, excluding the appointment's own ID. Success preserves ID and confirmed status and records old/new values and reason. Failure retains the original reservation; releasing it before obtaining the new one is forbidden.
3. Coordinator cancels a confirmed visit before arrival with a reason. Success sets `cancelled`, releases its reservation, and preserves history. Confirmed visits cannot be deleted. Repeated delivery must not create additional effective cancellations or contradictory audit entries.
4. Technician opens only their assigned visits, sees customer and schedule details returned by the existing appointment read contract, and records arrival. `confirmed -> in_progress` retains the scheduled interval and records actual arrival separately; completion records actual completion and makes `in_progress -> completed`. Do not replace the booked times with actual event times. Reassignment between read and action causes rejection/refetch.
5. On stale revision, show that the record changed and reload the authoritative record with the user's unsaved edits still available for comparison. Do not silently overwrite or automatically reapply changes. On interval conflict, explain that the requested technician/time is no longer available; the coordinator chooses another interval or technician and submits again.
6. On timeout or lost response, fetch current state/revision before retrying an update. A confirmed result is shown as success; an unknown result remains explicitly uncertain. Inspect the existing create contract for duplicate prevention; do not blindly retry creation after an ambiguous result. A request identity/deduplication mechanism is an engineering prerequisite if the existing service lacks one.

| Transition | Meaning / gate |
|---|---|
| draft -> confirmed | Coordinator confirmation; atomic availability check |
| confirmed -> confirmed | Coordinator reschedule/reassignment before arrival; revision check |
| confirmed -> cancelled | Coordinator cancellation before arrival; reason required |
| confirmed -> in_progress | Assigned technician arrival |
| in_progress -> completed | Assigned technician completion |
| draft edit | Coordinator; reservation semantics unresolved in Q2 |
| draft -> cancelled / draft removal | Q2; preserve existing behavior pending decision |
| in_progress -> cancelled or rescheduled | Q3; not implicitly authorized |
| completed/cancelled -> another state | Q3 for correction/reopening; not implicitly authorized |

Unsupported transitions must be rejected, not mapped silently to a supported status. The standard lifecycle is independent of emergency displacement. Actual arrival beyond scheduled end raises an occupancy-policy question under Q3; the system must not claim that scheduled-interval collision checks prevent physical overruns.

## Scheduling, time, concurrency, and audit

R1. A committed interval is positive: start UTC is strictly earlier than end UTC. Convert local time using its IANA zone. Retain both UTC instants and the zone/local representation without inconsistent values. Reject invalid zones and nonexistent local times; ambiguous repeated local times need an explicit offset/occurrence selection before saving. Show the appointment zone so users in different zones can interpret the visit. These checks follow from an unambiguous interval; they do not change business hours or add a scheduling horizon.

R2. Intervals are half-open: two intervals overlap iff `a.start < b.end` and `a.end > b.start`. Thus [10,20) and [20,30) may coexist for one technician, [10,20) and [19,30) may not, and different technicians may share identical intervals. Compare UTC instants. Editing an appointment excludes itself, never other bookings.

R3. Confirmed and in-progress appointments reserve their scheduled interval. Cancelled appointments do not. Draft reservation behavior is Q2; historical/completed occupancy and overrun behavior are Q3. Those choices must be explicit policy inputs before integrating a complete conflict query. They do not block correcting the interval predicate or implementing the confirmed/in-progress checks.

R4. Revision checks prevent stale updates to one appointment but do not prevent two new appointments racing for the same technician. Commit availability, reservation changes, appointment revision, and audit atomically with serialization or equivalent database protection for that technician. Two conflicting confirmations must not both succeed. A cross-technician reassignment protects both resource changes in one transaction. Inspect the real persistence layer before selecting locks or constraints.

R5. Audit contains stable appointment ID, authenticated actor, event time, reason, prior/new values and status, and revision linkage. Successful mutation and its audit commit together; failure cannot leave an unaudited appointment change. Concurrent edit, validation, or permission rejection must not appear as a successful appointment change. Reschedule/cancel require a coordinator reason. Preserve existing durable history and do not delete confirmed records.

## Decisions requiring the business owner

No answer is assumed. Each decision blocks only its listed policy-dependent work. Recommendations below are proposals, not accepted requirements.

| ID | Question and alternatives | Consequences and blocked work |
|---|---|---|
| Q1 | May an emergency displace a confirmed appointment? Recommend explicit coordinator-controlled displacement only if the business accepts disruption; prohibiting displacement protects commitments but may leave emergencies unscheduled. | Blocks emergency displacement semantics and its UI/mutations. Does not block ordinary scheduling or scheduling an emergency into an available interval under ordinary rules. If allowed, obtain authority, eligible visits, displaced status/placement, consent/contact responsibilities, reason requirements, and atomic failure behavior before designing it. No automatic cancellation or bumping is authorized. |
| Q2 | Do drafts reserve capacity, and should abandoned drafts be cancelled or removed? Recommend non-reserving drafts for simpler planning; reserving drafts protect tentative slots but require a release/expiry rule. | Blocks draft inclusion in the reservation query and draft abandonment controls. Does not block interval math, permissions, confirmed transitions, or ordinary technician UI. Confirming any draft still performs the atomic availability check. |
| Q3 | After arrival or completion, may coordinators cancel, reassign, correct, or reopen visits; do overruns extend occupancy; must completed historical intervals reject backdated bookings? Recommend preserving recorded history and making corrections explicit, with no silent status rewind. More flexibility requires override authority and audit rules. | Blocks exceptional lifecycle controls and occupancy policy outside scheduled active reservations. Does not block ordinary arrival/completion, pre-arrival cancellation/rescheduling, or audit groundwork. Standard lifecycle can be implemented separately; complete release needs these boundaries accepted. |

Business-owner answers should be recorded in decisions.md in a later authorized update and propagated into this spec and the dependent ticket drafts. Do not treat elapsed time or lack of response as approval. Q1 follow-up details are conditional on permission to displace, not independent prerequisites for ordinary work.

## Observable acceptance and verification

| ID | Observable acceptance |
|---|---|
| A1 | Coordinator creates and confirms a valid visit; reads return the assigned technician, stable ID, consistent local/zone/UTC times, status, and current revision. |
| A2 | Assigned technician can list/read their appointment; another technician cannot read or mutate it by direct ID. Coordinator sees all. A reassigned technician loses access immediately on the next request. |
| A3 | Adjacent bookings on one technician succeed; real overlaps and contained intervals fail; equal intervals on different technicians succeed. Existing room-isolation behavior remains intact when fixing the helper. |
| A4 | Two racing confirmations for the same technician/interval produce at most one success. Two edits from one revision cannot both silently overwrite each other. |
| A5 | Reschedule retains ID/history and confirmed status; success moves its reservation, while conflict, stale revision, or audit failure leaves the original booking intact. Cancellation retains the record and frees capacity. |
| A6 | Assigned technician records arrival then completion with actor and actual event times, retaining scheduled times. Completion before arrival and actions by a now-unassigned technician fail without mutation. |
| A7 | Invalid/nonpositive intervals and invalid/nonexistent local times fail clearly; repeated local times require disambiguation. Equivalent UTC instants collide even if displayed using different zones. |
| A8 | Every successful mutation has one corresponding effective audit change with reason and prior/new state. Timeout recovery does not silently duplicate a booking or repeat a transition. |
| A9 | Emergency displacement remains unavailable until Q1 and its conditional policy details are accepted. Chosen draft and exceptional lifecycle policies have explicit acceptance scenarios after Q2/Q3 are answered. |

Verification in this planning task: inspected all source documents and helper, ran the existing checks, and compared all five existing examples. No tests or production code were added. The suite is red because of the existing endpoint defect; it is not validation of the proposed service or UI. Future implementation must rerun existing checks and demonstrate A1-A8 against the actual integrated service, including concurrent requests and failure rollback. New automated tests require developer authorization. Human review and approval are release gates, not prerequisites for drafting or other independent planning.

Whole-document review: stable IDs, permission boundaries, half-open UTC intervals, revision recovery, and audit requirements agree across workflows and acceptance. Ordinary lifecycle work does not depend on emergency approval. Room naming is reconciled through an adapter rather than expanding scope. Remaining incompleteness is explicit in Q1-Q3 and persistence-contract inspection, not hidden in tickets.
