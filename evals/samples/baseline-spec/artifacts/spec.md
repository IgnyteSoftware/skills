# Appointment scheduling spec

Status: draft for human review. Ordinary scheduling has enough evidence for a concrete design proposal. Product rules listed in the decision tickets remain unresolved. This document does not authorize implementation or release.

## Problem statement

Operations coordinators need to schedule customer visits without double-booking technicians. Technicians need to see their assignments and record arrival and completion. Cancellation, rescheduling, concurrent edits, and emergency requests must leave an accurate appointment history.

## Sources and local research

- [Brief](../brief.md) supplies the requested workflows and unresolved emergency behavior.
- [Domain](../domain.md) defines actors, appointment fields, states, stable identity, retention, and audit requirements.
- [Implementation notes](../implementation.md) establish the existing read/create/update service, revision concurrency, durable audit, and time storage. They explicitly say technician UI, permissions enforcement, and displacement do not exist.
- [Decisions](../decisions.md) settle visibility, coordinator assignment, no customer login or billing, no silent overwrites, stable IDs, and human release approval.
- [Repository workflow](../repository-workflow.md) supplies the client/environment profile available in this fixture: Azure hosting, manual work intake, local Git with no remote, human review, and no PR workflow. No separate client profile was supplied.
- [Interval rules](../README.md), [helper](../scheduler.py), and [existing checks](../checks.py) establish positive intervals, half-open endpoints, and independent resources. The helper currently uses inclusive comparisons. Running `python -B checks.py` exited 1 at the first assertion, `adjacent later interval must be accepted`. Subsequent assertions were not reached. This confirms the reported defect without changing production code.

Research was local and performed directly because this task forbids delegation and external access. Service capabilities above are documented facts, not independently verified runtime behavior; the fixture only includes the small overlap helper.

## Solution

Build coordinator and technician workflows over the existing appointment service. Preserve its revision and audit guarantees. Enforce visibility and mutation permissions at the service, including direct appointment lookup. Make scheduling conflicts visible before confirmation and enforce the same rule atomically when changes commit.

Keep emergency displacement unresolved. An emergency label must not imply permission to move or cancel a confirmed appointment. Product approval must choose the behavior before that branch can be delivered. Ordinary scheduling can be designed and delivered independently once its own lifecycle and reservation questions are answered.

## Domain and invariants

Use the existing terms: customer receives service, operations coordinator manages scheduling, technician performs the visit. An appointment retains its ID across rescheduling, plus customer ID, technician ID, local start/end, IANA zone, status, and revision. Existing statuses remain draft, confirmed, in_progress, completed, and cancelled. Do not add an emergency status or a displaced status without an approved domain decision.

Established requirements:

- Only coordinators assign technicians. Technicians see only their current assignments; coordinators see all appointments.
- No customer login and no billing.
- Never delete a visit after confirmation. Preserve audit history of who changed what and why.
- Rescheduling preserves appointment identity. A stale revision never silently overwrites newer work.
- Appointments have positive intervals. Half-open intervals permit an appointment ending exactly when the next begins.
- A technician cannot have overlapping appointments that consume their availability. Which statuses consume availability still needs a product answer.

The helper's `room` field is a resource key, not a new appointment-domain concept. A scheduling integration must use technician identity for that key and preserve independence between technicians. Two technicians serving the same customer are not a resource conflict under the supplied technician rule; any customer-level restriction needs separate approval.

## User stories

1. As a coordinator, I want to create a draft for a customer so I can prepare a visit.
2. As a coordinator, I want to assign a technician so the visit has a responsible worker.
3. As a coordinator, I want to see appointments across technicians so I can manage the schedule.
4. As a coordinator, I want to confirm an eligible appointment so the visit can proceed under agreed lifecycle rules.
5. As a coordinator, I want an explanation of a scheduling conflict so I can choose another technician or interval.
6. As a coordinator, I want back-to-back visits to be accepted so a shared endpoint does not waste availability.
7. As a coordinator, I want to reschedule a visit without changing its ID so its history stays together.
8. As a coordinator, I want to cancel an eligible visit with a reason so the record explains why it will not happen.
9. As a coordinator, I want a concurrent-edit warning so I can review newer work before trying again.
10. As a technician, I want a list and details of my own assignments so I can plan my work without seeing other technicians' customers.
11. As a technician, I want to record arrival on an eligible assigned visit so the coordinator can see that work has started.
12. As a technician, I want to record completion on an eligible assigned visit so the coordinator can see that work is finished.
13. As a technician, I want a stale or reassigned visit to be rejected when I submit an update so I do not alter someone else's current assignment.
14. As a coordinator, I want the appointment zone and unambiguous time shown so I can review visits across daylight-saving changes.
15. As a coordinator, I want to inspect changes and their reasons so I can explain a cancellation, reschedule, or status change.
16. As a coordinator, I want emergency requests handled under an explicit policy so urgency does not silently erase existing commitments. This story remains blocked.

## Proposed behavior and implementation decisions

The existing read/create/update interface is the preferred seam. Extend it only where required to support role checks, lifecycle operations, and conflict enforcement. No new persistence architecture or hosting change is justified by this fixture. The following design details are proposals for review, not newly settled business policy.

### Access and entry points

The service derives the actor and role from trusted identity, never from caller-supplied technician identity alone. Filter technician lists and enforce the same restriction on detail reads and mutations. On every mutation, recheck current assignment as well as revision. Hide other technicians' appointment/customer details in denied responses. Coordinator access includes all appointments, while allowed state transitions still follow the eventual lifecycle policy. How deployment identity maps to these roles needs confirmation; do not select an identity provider from the Azure hosting fact alone.

The coordinator flow covers list, detail, create, assignment, confirmation, reschedule, cancellation, and audit inspection. The technician flow covers assigned list/detail, arrival, and completion. Both retain the user's unsaved input when validation or a stale revision prevents saving, then offer reload and review rather than automatic overwrite. Empty lists and unauthorized, missing, or no-longer-assigned records need clear outcomes without disclosing hidden data.

### Lifecycle

| Operation | Proposed transition or effect | Approval boundary |
| --- | --- | --- |
| Create | New draft with stable ID | Required draft fields need confirmation |
| Assign | Coordinator changes technician on an eligible appointment | Eligible states need confirmation |
| Confirm | draft to confirmed after validation | Reservation and lifecycle decisions |
| Arrive | confirmed to in_progress by assigned technician | Early/late arrival and correction rules unresolved |
| Complete | in_progress to completed by assigned technician | Correction and exceptional completion rules unresolved |
| Cancel | Eligible state to cancelled, with reason | Allowed source states and actor exceptions unresolved |
| Reschedule | Same ID, changed interval/zone and possibly technician | Eligible states and whether confirmation persists unresolved |

These transitions express the requested workflow but are not an approved transition matrix. No ticket may infer cancellation of in_progress work, reopening completed work, draft deletion, coordinator completion on behalf of a technician, or retrospective time edits. The lifecycle decision must settle those cases or explicitly defer them from release.

### Scheduling and time

Validate end strictly after start using resolved instants. Resolve the supplied IANA zone and local times consistently with the existing stored UTC instants. Reject invalid zones and nonexistent local times. Proposed handling for an ambiguous local time is to require the actor to select the intended offset, showing it before save. Product review must confirm that interaction; never silently pick an occurrence.

For the same technician, intervals conflict exactly when candidate start is before existing end and candidate end is after existing start. Endpoint equality is allowed. Cross-midnight visits use the same instant comparison. Rescheduling excludes the current appointment ID from its own conflict check. Reassignment checks the destination technician.

Which statuses reserve time is an open decision. Once settled, enforce that status set in both previews and writes. A preview is advisory: concurrent creates, confirmations, reassignments, and reschedules must perform resource conflict checks and commit atomically. Appointment revision checks alone cannot prevent two distinct appointments booking the same technician. Investigate the actual persistence mechanism before selecting how to serialize competing writes.

Reject a conflicting reschedule as a whole. Preserve the original appointment, revision, assignment, and reservation rather than cancelling first and attempting a new booking. Actual arrival/completion must not silently rewrite the planned interval. Whether an overrun affects future availability is a product question in the lifecycle decision.

### Revision, audit, and failure behavior

Reuse the service's expected-revision contract for mutations. A stale revision leaves the appointment unchanged and requires reload/review. Do not resolve by last writer wins. Successful changes advance the revision and durably record actor, before/after change, and reason through the existing audit mechanism. Capture a reason for coordinator cancellation, reassignment, and reschedule. Confirm the required reason entry for normal arrival/completion with the lifecycle owner; an explicit action may supply a reason if approved.

Appointment changes and their audit record must succeed together. A failed audit write cannot leave an unaudited mutation. After an uncertain response, reload to establish the current result before resubmitting. Duplicate arrival/completion submissions must not duplicate transitions; use current revision and state, and investigate existing request identity support before promising stronger retry guarantees.

Do not add notifications, offline synchronization, or external calendar integrations to satisfy the core workflows.

## Testing decisions

No new tests are written in this planning task. Proposed future verification uses the existing appointment read/create/update seam for externally visible behavior. The overlap helper checks are useful narrow prior art, but do not prove service authorization, persistence, or transactional conflict handling. Human review must confirm this seam and the test scope before implementation.

Acceptance scenarios for later verification:

- Adjacent intervals in either order succeed; partial, identical, and contained overlap on the same technician fail. Different technicians remain independent.
- Zero/negative intervals fail. Cross-midnight and daylight-saving examples retain the chosen zone and UTC meaning. Ambiguous times require an explicit choice under the proposed interaction.
- A reschedule preserves ID and audit history, ignores itself during conflict detection, and leaves the original untouched on failure.
- A stale update fails without overwriting newer work. Two distinct appointments racing for the same technician/interval cannot both commit.
- Technicians cannot list, fetch, or change others' assignments, including after reassignment. Coordinators can view all appointments and alone can assign technicians.
- Approved lifecycle transitions succeed; prohibited transitions leave state unchanged. Arrival and completion retain planned times unless a later approved policy explicitly says otherwise.
- Cancellation retains the appointment and history. Its effect on availability follows the approved reservation rule.
- A successful change has its audit record; a persistence or audit failure exposes no partial success. An uncertain response can be reconciled by reload.
- Emergency scenarios are added only after the owner answers the displacement question; they must cover preservation of affected records and competing writes.

Observed check result: the existing suite is red on its first adjacency assertion. There is no service integration suite or production implementation in this fixture to validate the broader design. Release additionally requires human approval.

## Out of scope

Customer login, billing, automated technician assignment, external integrations, production implementation during this task, ticket publication, commits, pushes, and release. Travel buffers, notifications, recurrence, and offline operation were not requested and are not assumed requirements.

## Further notes

[Decision and delivery drafts](tickets.md) are the local map. Its open questions prevent a claim that this specification is fully approved or implementation-ready. Existing domain and decision files remain authoritative and unchanged. Recommendations in this draft must not be copied into those files as accepted decisions without human answers.
