# Session workflow audit

Historical design evidence, reviewed September 22, 2026. This is an anonymized
summary of local workflow decisions, not an active runtime instruction file.
The current package retains 18 skills, including Wayfinder. The smaller package
discussed in the [custom proposal](custom-workflow-proposal.md) was not selected.

## Coverage

The initial scan covered 696 local Codex JSONL files and 433 local Claude JSONL
files. A follow-up covered 708 and 445 respectively. These files include resumed
conversations, delegated work, generated reviewer prompts, and repeated context;
they are not independent human conversations or preference statistics.

The audit extracted user-role messages, searched for workflow decisions and
corrections, and closely read relevant episodes. Generated prompts were excluded
from preference claims after inspection. This is a broad scan with targeted reading,
not manual review of every transcript. Cloud-only, deleted, and other-machine
history was unavailable. Exact session identifiers, raw excerpts, client names,
and local client paths are excluded from this publishable report.

## Repeated workflow decisions

| Observed pattern | Requirement for the shared skills |
|---|---|
| Explore a product through planning, focused questions, and research before implementing. | Wayfinder owns coherent specifications and unresolved decisions. |
| Organize accepted work around outcomes, milestones, or versions. | Preserve sequencing and dependencies; do not invent one universal release scheme. |
| Prototype locally, select a variant, then authorize production work separately. | Keep experimental artifacts disposable and preserve the selection checkpoint. |
| Implement independently scoped issues in appropriate worktrees. | Follow repository ownership and workspace conventions; avoid duplicate claims. |
| Follow reviewer feedback until a PR is ready. | Distinguish opening a PR from completing delivery, and readiness from merge authority. |
| Other repositories have no PR process and require human review of local changes. | Resolve delivery per repository rather than assuming GitHub or PRs. |
| Some tasks authorize local commits but prohibit pushing. | Separate edit, commit, push, integration, and deployment authority. |
| An instruction authorizes publication of earlier work but leaves subsequent changes local. | Attach authority to its exact scope, not to the whole session forever. |
| A task explicitly authorizes merge when checks and reviews pass. | Preserve that authority without an unnecessary new approval request. |
| Validate agreed changes and avoid unsolicited test expansion. | Run required checks; create new tests only under the task and repository policy. |
| Review all working changes, including new files. | Account for staged, unstaged, and untracked scope. |
| Report failed checks and actual publication state. | Completion includes evidence and a clear handoff, not only artifact links. |

These observations support conditional routing and client-specific endpoints.
They do not support mandatory interviews, specifications, issue creation, commits,
PRs, or merges for every request. Status questions steer ongoing work; explicit
pauses or cancellations change its boundary.

## Decisions from the audit

Use one small `work` entry point. Preserve requested combinations and ordering.
Keep Wayfinder for discovery, shared decision maps, and coherent specifications;
use research for facts, grilling for human choices, and prototypes for experiments.
Keep useful specialists discoverable while evaluating any future consolidation.

Replace author-specific setup assumptions with repository convention discovery.
Preserve existing tracker documents, claims, and decision-map relationships.
Do not resurrect previously retired skills or copy a source's tool restrictions,
model choices, attribution rules, or blanket publication authority.

The [PStack source review](pstack-routing-research.md) distinguishes one entry point
from one installed skill and from a deterministic execution engine. The
[workflow proposal](custom-workflow-proposal.md) records options and client delivery
profiles. Behavioral comparisons belong in the evaluation report; these historical
observations alone do not establish routing reliability.
