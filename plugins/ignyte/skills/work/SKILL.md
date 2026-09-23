---
name: work
description: Coordinate engineering requests across research, planning, prototypes, implementation, review, and PR delivery. Use for new work or changes to an ongoing task; preserve every requested outcome.
user-invocable: false
---

# Work

Identify every requested outcome, the accepted scope, and where the user wants work to stop. Use the conversation and repository instructions as the contract. A combined request selects multiple actions; it does not choose just one label. Answer simple questions directly.

Read the repository's delivery rules or linked client workflow before choosing a publication path. Hosting, source control, tracker, and review policy are separate facts: Azure does not imply PRs or Azure Boards. Reuse established instructions; use project-setup only for material gaps. Carry the resolved rules into delegates and recheck them when switching repositories. Missing delivery authority does not block authorized local work.

Choose the next action by what is still unknown or unfinished. Respect explicit ordering; otherwise follow dependencies and state the chosen approach briefly. Load only the relevant skills below, through the skill tool or their linked files. Independent work may run together when delegation is available and appropriate. Delegates receive the same scope, stopping point, and completion criteria.

| Need | Skill |
|---|---|
| Facts or external constraints | [research](../research/SKILL.md) |
| Discovery, coherent specifications, decisions, or planning | [wayfinder](../wayfinder/SKILL.md) |
| A product decision needs the user | [grilling](../grilling/SKILL.md) |
| Test an interaction or uncertain behavior | [prototype](../prototype/SKILL.md) |
| A defect or performance regression | [diagnosing-bugs](../diagnosing-bugs/SKILL.md) |
| Small settled spec synthesis or breakdown of an accepted plan | [to-spec](../to-spec/SKILL.md), [to-tickets](../to-tickets/SKILL.md) |
| Issue intake or missing project conventions | [triage](../triage/SKILL.md), [project-setup](../project-setup/SKILL.md) |
| Interfaces or architecture | [codebase-design](../codebase-design/SKILL.md), [improve-codebase-architecture](../improve-codebase-architecture/SKILL.md) |
| Domain terms or decisions | [domain-modeling](../domain-modeling/SKILL.md) |
| Explicitly requested test-first work | [tdd](../tdd/SKILL.md) |
| Validate a change against standards and intent | [code-review](../code-review/SKILL.md) |
| PR status or delivery follow-through | [babysit](../babysit/SKILL.md) |
| Writing or agent instructions | [unslop](../unslop/SKILL.md), [writing-for-agents](../writing-for-agents/SKILL.md) |

For implementation, use the assigned branch or worktree, preserve unrelated changes, make the smallest change that meets the accepted scope, and run the required validation. Distinguish running existing tests from writing new ones; new tests follow the user's request and repository policy. Review at the repository's required gates. Publication, merge, and deployment must stay within authorization already given; do not ask for that authorization again unless the scope or circumstances change.

Local edits, commits, pushes, integration, and deployment have separate authority. A commit request does not authorize a push. Where the client requires human handoff, return the complete changes, exact base revision and any produced commit SHA, verification evidence, and remaining decisions. A requested local commit may itself be the review artifact; honor explicit earlier review checkpoints. Do not substitute an agent review for required human review or create a PR in a no-PR workflow.

After each result, reassess unfinished outcomes. Research may change a prototype; a prototype may change the plan; failed checks or actionable reviews return to implementation. Avoid repeating a failed approach without new evidence. Report a blocker when the next step needs an unavailable resource or a human decision, and continue independent authorized work.

New messages steer the active task. A status question does not cancel implementation. An explicit pause, cancellation, or narrower scope does. Planning and prototypes alone do not authorize production changes. A planning stage does not itself change the host application's Plan mode or permissions.

Finish at the requested boundary with every outcome accounted for: deliver artifacts, explain changes and validation, and name remaining decisions or blockers. State whether work is local, committed, published, or deployed. For authorized PR delivery, follow babysit through readiness. Default to leaving the PR open; merge or deploy only when the task authorizes it and its gates pass.
