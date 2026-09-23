# Ignyte routing source notes

Historical design comparison. The selected review branch retains 18 skills and
Wayfinder rather than adopting the smaller package proposed below. See the
[executed evaluation](../evals/REPORT.md) for the current result.

Reviewed 2026-09-22. Research only. This document compares designs; it does not change skills, configuration, or installed behavior. Recommendations are design judgments, not measured success rates.

## What the primary sources establish

Anthropic distinguishes workflows with predefined code paths from agents that choose their next actions dynamically. Its guidance favors simple, composable designs. Routing is useful when inputs divide into distinct categories that the system can classify reliably; an orchestrator is useful when the required subtasks cannot be predicted in advance. That supports using different instructions for research, planning, and implementation without requiring a graph execution service. [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

Agent Skills load metadata first, instructions when relevant, and supporting files as needed. Splitting a skill into files changes when information is loaded; splitting every concept into a discoverable skill is a separate decision. [Agent Skills design](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

Claude Code uses skill descriptions for automatic selection. `user-invocable: false` leaves a skill available to the model while preventing direct user invocation. Bodies load on use, but listed skill metadata still consumes context. The docs recommend evaluating automatic selection and task results separately in fresh sessions, comparing with a baseline. They also distinguish skill instructions from deterministic enforcement through hooks. These are Claude Code behaviors, not proof that Codex enforces the same invocation restrictions. [Claude Code skills](https://code.claude.com/docs/en/skills).

PStack's reviewed router selects playbooks and applies cross-cutting guidance. Its frontmatter contains `disable-model-invocation: true` and Cursor-specific `mode: true`; copying that frontmatter would defeat Ignyte's automatic-entry goal. This source illustrates one written routing policy, not evidence that a single entry always performs better. Revision reviewed again here: `86ecc82055e4d3cb567e72c56f390800a4978c9b`. [PStack router](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/SKILL.md). The [earlier source audit](pstack-routing-research.md) records the associated playbooks, ownership, and reuse limits.

## Options for Ignyte

These tradeoffs are inferences from those sources and the requested Ignyte workflow.

| Design | Advantages | Costs |
| --- | --- | --- |
| One `work` skill with internal research, plan, and implement playbooks | The developer states a goal. One owner tracks scope, combined outcomes, authorization, and completion. Three playbooks can stay short and load only when needed. | Broad entry selection can miss or over-trigger. A bloated router becomes harder to maintain. The agent must distinguish planning from implementation. |
| Three discoverable skills: research, plan, implement | Distinct descriptions and deliverables; easier to evaluate each mode; explicit wording can reach the relevant instructions directly. | Mixed requests match several descriptions. Handoff rules can drift between files. Generic requests such as "pick up this issue" still need classification, so removing the router does not remove routing. |
| Small `work` router plus three discoverable specialists | Generic requests have one owner; specific requests can enter directly. Each specialist has a clear output and can be evaluated separately. | Four discovery entries and overlapping triggers. Needs an explicit rule that the active task keeps ownership of all requested outcomes. |
| Deterministic state machine | Makes supported transitions and mandatory gates inspectable. Useful when a process must survive detached runs or enforce fixed operational rules. | More code, state, and recovery behavior. Mixed requests and new evidence require many transitions. Written intent still needs interpretation. Excessive machinery for the proposed mockup. |

I recommend one small automatic `work` entry with three custom playbooks first. Keep direct specialist discovery only where actual prompts benefit from it. This preserves the easy user experience while separating the instructions the agent needs. The playbooks are work types, not separate host-application modes or mandatory stages.

## Combined requests and boundaries

The router should record requested outcomes as a set plus any explicit order. It should not classify every request into exactly one bucket.

| Prompt | Expected route and stopping point |
| --- | --- |
| "Research and prototype this" | Gather the evidence needed for the experiment, build a disposable prototype, return findings and observed behavior. |
| "Plan, then prototype" | Produce the initial plan, use the prototype to test its uncertainties, revise the plan when evidence changes it. |
| "Prototype, then plan" | Run the experiment first, then plan from its results. |
| "Pick up issue 123 and work on it" | Read the issue and repository workflow, identify the remaining work, then implement if the requested scope is clear. Ask only for material decisions that cannot be resolved from evidence. |
| "Research this, but don't implement" | Research may include a requested isolated experiment. Stop before production changes. |
| "Implement and get the PR ready" | Implement, verify, satisfy review requirements, publish when authorized, and follow checks and actionable feedback through readiness. |

Research can interrupt implementation when a factual uncertainty blocks progress. An experiment can inform research or planning without becoming production code. Completing one output does not cancel another requested output. These rules belong once in the shared routing contract.

## What to evaluate before replacing the package

Use representative past requests, with sensitive details removed, to compare the three prompt-based options in fresh sessions. Measure the selected instructions, completed deliverables, respected boundaries, avoidable clarification, and accuracy of verification claims. Include combined requests, ambiguous issue pickup, simple fixes, status-only requests, and a user changing the scope mid-task.

The existing loader checks and simulated scenarios do not establish production routing reliability. A smaller word count also does not establish lower total token use. Keep the recommended architecture provisional until the comparison shows whether three separate discovery entries help Ignyte's actual requests.

## Client-specific delivery

The user identified the client as an Azure-hosted client environment with no GitHub or PR process and human review at the endpoint. They clarified that implementation often stops without a commit, a local commit is sometimes requested, and pushing always needs explicit instruction. Commit authority and push authority must therefore be tracked separately. The exact source-control configuration, tracker, and enforcement remain unverified. Treat the following as a proposed profile, not a description of permissions already configured.

The shared implementation path should finish at the client's defined review handoff. PR creation and babysitting are conditional delivery steps for repositories that use them. The client must not inherit an unconditional GitHub or PR requirement. A requested local commit can be the handoff artifact; a universal pre-commit approval pause would contradict that instruction. The same research, plan, and implement entry behavior can serve both environments.

Azure Repos supports both Git and TFVC. Git permits local commits and local branches independently of publication. TFVC uses centralized changesets and different workspace behavior, so a Git branch or worktree recipe cannot be assumed. [Microsoft version-control comparison](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/comparison-git-tfvc?view=azure-devops).

| Confirmed repository type | Proposed human-review handoff |
| --- | --- |
| Git, remote writes not allowed | Local diff or patch with exact base revision, changed files, verification evidence, and unresolved decisions. Local commits or branches only when allowed by the client workflow. |
| Git, agent branch publication explicitly allowed | Named review branch and exact head commit, with the same review evidence. The human performs the restricted integration or release action. No PR is implied. |
| TFVC | Local pending changes and review evidence; a shelveset only when the client allows that server write. The human performs restricted check-in or release actions. |

TFVC shelving stores pending changes on the server without checking them in and supports review and handoff to another person. A shelveset is still an external mutation; it is not a substitute for authorization. [Microsoft shelveset documentation](https://learn.microsoft.com/en-us/azure/devops/repos/tfvc/shelve-command?view=azure-devops).

Put the client workflow in the repository's instruction file, with links to project-specific build and review guidance. Official OpenAI documentation describes Codex's global instructions followed by instructions from the project root to the working directory, with nearer guidance overriding earlier guidance. A client file outside that discovery path needs an explicit loaded pointer; its location in a portfolio directory does not by itself establish that Codex reads it. [Official OpenAI AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

A proposed compact client profile should record:

- Repository type and approved tools.
- Permitted local actions, permitted remote actions, and human-only actions.
- Required verification and the endpoint that counts as agent completion.
- Review artifact location, intended human owner, and what evidence the handoff must contain.

For the client, default to local changes and evidence; create a local commit when instructed and push only when explicitly instructed. Preserve existing scoped authorization without redundant approval requests. Check-in, integration, tracker writes, and deployment each require their own applicable authority; a local-commit request cannot authorize a server-side TFVC check-in. These rules describe the user's requested profile, not verified server enforcement.

## Instructions versus enforced permissions

Written instructions tell the agent how to behave. Azure identity permissions determine which repository actions the server accepts. Repository permissions can be assigned to users or groups and scoped to individual repositories. Effective access includes inherited and group permissions; merely leaving a permission unset does not remove another grant. [Microsoft repository permissions](https://learn.microsoft.com/en-us/azure/devops/repos/git/set-git-repository-permissions?view=azure-devops).

For Git, `Contribute` permits pushing new commits to a branch. `Force push`, `Manage permissions`, `Edit policies`, and policy-bypass permissions are separate capabilities. Branch creators can receive explicit permissions, so restricting a group without checking effective branch permissions can leave unintended authority. These controls allow separating an agent identity's write access from the human integrator's access. [Microsoft branch permissions](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-permissions?view=azure-devops).

Azure branch policies implement checks around PR-based integration. Adding those policies is not a neutral way to enforce the client's existing no-PR process. A human can review a patch or branch and perform integration with their own identity; the instruction profile records that procedure while identity permissions limit the agent's integration authority. This is a proposed design, not a claim that such review is already enforced or audited in the client environment. [Microsoft branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops).

If an agent can use the same unrestricted credential as the human, the server sees that credential's authority; a skill's role label does not create a separate permission boundary. An enforceable separation therefore needs a suitably restricted identity or execution environment, with human credentials unavailable to the agent. Repository permissions also do not control every pipeline, Azure deployment, or local-machine action. Map each confirmed human-only action to the service that actually enforces it. No identities, permissions, policies, or environments were changed during this research.
