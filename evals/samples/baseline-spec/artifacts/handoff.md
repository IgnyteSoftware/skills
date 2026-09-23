# Scheduling handoff

Created [spec](spec.md) and [dependent ticket drafts](tickets.md). They cover coordinator scheduling, technician visibility and progress, rescheduling/cancellation, half-open intervals, time zones, concurrency, audit, and failure behavior. Production code and existing domain decisions are unchanged.

The business owner must decide emergency displacement. Ordinary scheduling remains independent of that answer, but needs explicit lifecycle/reservation rules. Identity mapping and ambiguous-time entry also need human answers. The ticket map records these questions, conditional follow-ups, and the work each blocks. Recommendations are proposals, not decisions. The artifacts are not ready-for-agent issues and have not been published.

Local research confirmed the inclusive-endpoint defect in the existing overlap helper. `python -B checks.py` failed at the first assertion, `adjacent later interval must be accepted`, exit 1. Later assertions were not reached. No fix or new tests were written because this is a planning task. The service architecture is supported by implementation notes rather than runnable service code in the fixture.

Next, review the named decision frontier and the proposed service verification seam. Approve or revise ticket sizes and dependencies before manual intake. After the answers, update the spec and replace the emergency placeholder if that behavior is selected. Human release approval remains required. Hosting is Azure; this work creates no GitHub or PR workflow.

Supplied skills used:

- `.agents/skills/wayfinder/SKILL.md`
- `.agents/skills/grilling/SKILL.md`
- `.agents/skills/domain-modeling/SKILL.md`
- `.agents/skills/research/SKILL.md`
- `.agents/skills/to-spec/SKILL.md`
- `.agents/skills/to-tickets/SKILL.md`
- `.agents/skills/unslop/SKILL.md`

Task constraints override skill defaults for live interviews, delegation, publication, separate issue files, and automatic readiness labels. No human answers were invented, no ADR records a new accepted tradeoff, and all writes remain within this fixture.
