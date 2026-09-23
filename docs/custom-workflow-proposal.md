# Custom Ignyte workflow proposal

Historical alternatives, not the selected package. Subsequent review retained all
18 skills and Wayfinder as the specification coordinator. The four-skill proposal
below remains here to explain the tradeoffs; it is not a removal or rollout plan.
Repository-specific delivery and the client's separate commit/push authority are retained
in the current implementation.

Research proposal, September 22, 2026. No active skills, onboarding rules, client
settings, or tracker records were changed. The earlier local mockup remains intact.

## Recommendation

Keep one plain-English entry point, `work`, and give it three independently written
Ignyte playbooks: research, plan, and implement. These are composable kinds of work,
not exclusive modes. Keep review, PR babysitting, and unslop as small agent-invocable
specialists. This would leave four installed skills and three internal playbooks.
The agent can read a playbook without it becoming another discoverable skill.

Start from Ignyte's observed decisions and completion conditions. Do not shorten
upstream skills again and call them wholly original. Retaining the current unslop
means retaining a PStack-derived exception and its author/license notice. The other
workflows should be written independently. Preserve notices for retained material.

The words developers need are ordinary ones: “research this,” “plan this,” “pick up
this issue,” or “work on this.” No slash command or exact keyword is required.
Simple questions get simple answers. An issue's state and accepted scope guide the
work; its label alone does not grant publication or deployment authority.

## What the history supports

The earlier [session audit](session-workflow-audit.md) reviewed the available local
history. This follow-up scanned 708 Codex JSONL files and 445 Claude JSONL files and
read selected workflow messages. These include resumed and delegated sessions,
generated reviewer requests, and repeated context. They are not independent human
conversations or usage statistics. Automated candidates were checked for synthetic
content before using the episodes below. Cloud-only and deleted history was not
available. Raw extracts remain outside the repository.

| Observed request pattern | Workflow consequence |
|---|---|
| No PR system; one eventual commit per fix; approval before commit or push. | PR delivery cannot be universal. |
| Pick up an issue while retaining a no-commit/no-push boundary. | Work authorization and publication authority remain separate. |
| Put an unresolved deployment idea into a research backlog. | Research work is not automatically ready implementation work. |
| Proceed by agreed modules and checkpoints; publish earlier work but not subsequent edits. | Authorization stays attached to its scope. |
| Run review, then commit locally without pushing. | A passing review does not expand publication authority. |
| Implement, review, and publish a PR in another project. | Repositories and tasks can have different endpoints. |
| Use separate worktrees and PRs, follow automated reviews, then return for human review. | Readiness can be the endpoint without merge authority. |

Repository evidence agrees. Hounddog's `docs/agents/issue-tracker.md` requires reading
the issue, comments, and blockers; its label guide distinguishes ready work from
triage. [Issue 241](https://github.com/IgnyteSoftware/hounddog/issues/241) records a
selected disposable prototype, narrow scope, verification, and explicit release
authorization. [Issue 239](https://github.com/IgnyteSoftware/hounddog/issues/239)
separates release work from feature implementation. Those are examples, not rules
for every client. Repository-specific labels should remain repository-specific.

## One entry point or three?

| Design | Advantages | Costs | Assessment |
|---|---|---|---|
| One large workflow skill | Few files and one trigger. | Every task loads unrelated instructions; mixed responsibilities become harder to maintain. | Avoid a large all-in-one body. |
| Three discoverable skills: research, plan, implement | Clear individual deliverables; each trigger is easy to evaluate; each body stays narrow. | Mixed requests need coordination; handoff rules can drift if repeated; “work on this” still requires classification. | Viable alternative if routing evaluations favor it. |
| Small `work` entry plus three internal playbooks | One familiar interaction; one owner for scope and handoffs; selected instructions load when needed. | An initial routing error can affect the whole task; internal playbooks need precise pointers. | Recommended first design. |
| Router plus three separately discoverable workflow skills | Agents can enter a narrow workflow directly while keeping a common coordinator. | More overlapping triggers and two possible entry paths to evaluate. | Promote playbooks only if real selection failures justify it. |

These are design judgments, not measured superiority claims. Primary-source findings
and links are in [routing source notes](routing-source-notes.md). PStack illustrates
written routing and conditional playbooks; its invocation metadata should not be
copied into an automatic Ignyte entry point. No deterministic graph engine is needed
for this proposal. Tool permissions and hosting controls enforce actions; prose
alone cannot enforce them.

## The three playbooks

| Playbook | Question it answers | Completion |
|---|---|---|
| Research | What is true, uncertain, or worth choosing? | Evidence, options, recommendation, and unresolved facts. A prototype is one possible experiment. |
| Plan | What should change, and in what order? | Accepted scope, decisions, dependencies, observable acceptance, and actionable next work. Tickets only when useful or requested. |
| Implement | Make the accepted change and prove its behavior. | Scoped changes, required verification and review, followed by the delivery endpoint allowed for this repository and task. |

“Research and prototype” produces findings and an experiment. “Plan then prototype”
creates a preliminary plan, tests the risky assumption, then updates the plan.
“Prototype then plan” starts with the experiment. “Pick up this issue” reads the
issue and its dependencies, resolves material unknowns, then implements when scope
permits. “Research only” stops with findings. Small fixes do not require a separate
plan document. A playbook called plan does not switch the host's actual Plan mode.

The router carries only the active outcome, accepted scope, repository profile,
issue/worktree when applicable, authorized endpoint, and evidence needed to finish.
Follow the user's explicit order. Ask about missing decisions only when they block
useful work. A status question updates the user without cancelling the task.

## Client and repository delivery profiles

Separate four decisions: repository host, work tracker, source-control type, and
delivery/review policy. Azure hosting does not imply Azure Boards, Git, PRs, or
permission to push. GitHub hosting likewise does not authorize a PR or merge.

Use a short, version-controlled repository document, referenced by `AGENTS.md`,
for the approved workflow. A client can maintain a common baseline, with each
repository pointing to its applicable revision and recording genuine exceptions.
Keep client-specific content in the client's approved location. A portable local
copy or deployed instruction file is preferable to a broken cross-repository link.
Keep loader-specific imports in the host instruction layer, outside the playbooks.

Resolve the profile from the repository's explicit instructions. Use remotes to
confirm identity, not infer permissions from a domain or folder name. For multiple
remotes, record which endpoint is the delivery target. Pass the resolved profile and
scope into any delegated work. Re-resolve when switching repositories or clients.
Missing or conflicting delivery rules block external delivery, not useful authorized
local investigation. Never manufacture a more permissive profile to complete a task.

| Responsibility | Ignyte repository using PRs | Client requiring human handoff, such as the client |
|---|---|---|
| Agent's useful work | Research, plan, implement, verify, review. | The same local work within approved scope and environment. |
| Remote changes | Only the task-authorized branches, issues, or PRs. | Push only on explicit instruction; commit permission alone never includes push permission. Other remote actions follow their own authority. |
| Review | Required independent review plus repository checks and approvals. | Agent review prepares evidence; a human reviews the exact resulting artifact. |
| Completion | Local change, commit, PR readiness, merge, or deployment as authorized. | A review package by default; the authorized human handles the next restricted action. |
| Babysit | Used when sustained PR delivery is requested. | Skipped when there is no PR workflow. |

For the client, Azure hosting, no PR process, and required human review are user-confirmed.
The user clarified the action rules: sometimes implement without committing,
sometimes commit when requested, and never push without explicit instruction.
Use separate permissions for local edits, commit, push, integration, and deployment.
“Implement this” does not imply commit. “Commit this” does not imply push. An explicit
push instruction covers only the named or clearly understood changes and endpoint.
Do not ask again for an action already authorized within that scope.

Human review does not impose a universal pre-commit pause: the user may request a
local commit as the review artifact. Respect any task-specific earlier checkpoint.
The exact tracker, reviewing authority, source-control configuration, and configured
enforcement remain to be verified. This proposal does not infer them from a client
directory name or claim to have inspected the Azure environment.

Human review must identify the artifact being accepted: base revision plus complete
patch/package digest, or a reviewed commit. Record the decision in the client's
approved channel. Material changes after review return to review. A bot finding,
issue description, or old approval of another change does not replace human review.
Previously given approval remains valid for its unchanged scope and permitted action.

The current shared onboarding instruction says “Always open a PR.” That conflicts
with this client requirement. Before rollout, replace it with the rule “Follow the
repository's approved delivery and human-review policy; use a PR where that policy
requires one.” The current `work` and `babysit` paths also need profile-aware handoff.
This research does not silently change those committed instructions.

### Enforcement

Profiles tell the agent what to do. An identity without remote write permissions
prevents it from pushing. Keep client publication and deployment credentials with
the approved human or gated service; sharing the human's unrestricted credentials
with an agent defeats that separation. Local commit restrictions need local tooling
or a human-operated handoff because a remote permission cannot prevent `git commit`.

Azure PR branch policies are not a solution to a client that does not use PRs.
Use permissions appropriate to the actual Git or TFVC repository and a human-owned
handoff. A no-PR Git workflow can deny the agent remote contribution while the human
reviews and applies the package. Confirm the client's existing controls and roles
before proposing administrative changes. Do not claim server enforcement of patch
review unless the actual integration path verifies it. See the source notes for
Microsoft's documented permission model and the distinction from PR policies.

## Proposed treatment of every current skill

These are recommendations for a later implementation, not deletions in this turn.

| Current skill | Proposed home |
|---|---|
| work | Rewrite as Ignyte's small coordinator with profile-aware stopping points. |
| research | Custom research playbook under work. |
| wayfinder | Custom plan playbook; preserve decisions, sequencing, and checkpoints. |
| grilling | Focused decision questions inside plan, without a separate skill. |
| prototype | Conditional experiment guidance used by research and plan; keep disposable/production boundaries. |
| to-spec | Plan output template only when a specification is needed. |
| to-tickets | Plan's issue preparation rules and the three templates below. |
| triage | Intake decision inside work: research, plan, implement, or blocked. |
| project-setup | Repository/profile discovery inside work; no routine setup interview. |
| diagnosing-bugs | Implement's conditional diagnosis guidance; reproduce before claiming a fix. |
| tdd | Optional implementation reference when explicitly requested; no always-on test mandate. |
| code-review | Custom `review` specialist, usable alone or from implement. |
| codebase-design | Targeted architecture questions in plan; no standalone general vocabulary skill. |
| improve-codebase-architecture | Architecture research/planning task, not another permanent skill. |
| domain-modeling | Project domain documents and relevant planning decisions. |
| writing-for-agents | Maintainer guidance for skill authors; remove from the routine developer skill list. |
| babysit | Custom PR follow-through specialist; only for profiles that use PRs. |
| unslop | Retain compactly, with Lauren Tan / PStack provenance. |

## Issue and handoff templates

Use three optional templates: [research](workflow-templates/research.md),
[plan](workflow-templates/plan.md), and [implementation](workflow-templates/implementation.md).
Use [the review handoff](workflow-templates/review-handoff.md) to finish any of them.
They work as local Markdown, Azure work-item descriptions, or GitHub issue bodies.
They are not installed issue forms and do not assume a particular Azure process.

Do not create three issues for every task. One clear implementation issue is enough
for settled work. Create research work when a factual uncertainty blocks a decision;
planning work when choices or cross-cutting dependencies need resolution. Prototype
work belongs with the question it answers. Add reproduction details to an
implementation issue for a bug. Release work can use the implementation template
with explicit environment, artifact, approval, and recovery details.

Every task needs an outcome, observable completion, and scope. Add dependencies and
delivery exceptions only when relevant. The profile owns standing rules; issue text
links to them instead of repeating them. The agent fills in discoverable information.
An unresolved product decision is a question, not an excluded requirement.

Use existing tracker states and labels. For local tickets, a small index can state
what is ready, blocked, being worked, or awaiting human review. An approval request
or ready-for-agent label is not permission to publish. Avoid introducing a company
label state machine as a dependency of useful work.

## Simple output

Return the outcome first, then the evidence and actual endpoint. For example:

> Implemented the agreed fix locally. Build and existing checks passed. The review
> package is linked below. Awaiting your review; nothing was committed or pushed.

For research: recommendation, strongest evidence, unresolved decision. For planning:
accepted scope, ordered work, remaining decision. For implementation: what changed,
what ran and failed, and whether the result is local, committed, published, or deployed.
Omit empty sections. Avoid long transcripts and do not call blocked work complete.

## What to validate before changing the package

Compare one router with three direct skills using the same realistic prompts on
both supported CLIs. Check invocation separately from outcome, order, stop boundary,
and actual prohibited-action attempts. Include mixed research/prototype/plan tasks,
an unblocked issue, no-commit and commit-only tasks, PR status versus sustained
delivery, Azure no-PR human handoff, missing profiles, multiple remotes, and switching
between clients. Include human approval followed by material changes.

Observe real artifacts and actions, not only the agent's explanation of what it
would do. Record model/client versions and repeat ambiguous cases before concluding
that a design is reliable. Favor the smallest design that completes the requested
outcomes while honoring every client boundary. No new routing design was executed
or benchmarked during this research.
