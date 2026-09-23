# Ignyte skills

A shared engineering workflow for plain-English requests, installed on Claude Code
and Codex by [Ignyte onboarding](https://github.com/IgnyteSoftware/onboarding).

## Start with the outcome

Describe the work: "research and prototype this," "plan the migration," or "fix
this issue, review it, and open a PR." The `work` skill selects the needed skills,
keeps every requested outcome, and reassesses after each result. Explicit ordering
and stopping points remain part of the task. A plan or prototype alone does not
start production implementation.

`wayfinder` owns substantial discovery and specification work. It coordinates
research, focused questions, prototypes, and domain decisions, then checks the
specification as a whole before breaking it into implementable work. All 18
specialists remain installed; the four-skill consolidation was a research option,
not the selected package.

This is agentic routing, not a workflow engine. Tests, CI, permissions, and
repository controls provide enforcement. No skill guarantees identical model
behavior on every run. See [the mockup and validation](docs/skill-routing-mockup.md).
The [paired workflow evaluation](evals/REPORT.md) records the later 19 local task
executions, sample specifications, review fixes, and rollout limits.

## Invocation and delivery

All 18 skills allow agent invocation. Claude Code uses `user-invocable: false`;
Codex uses `policy.allow_implicit_invocation: true`. No skill disables model
invocation. Claude Code hides direct user invocation; Codex has no documented
equivalent restriction, so explicit selection remains available there.

One normal entry point does not mean only one installed skill or one loaded
description. Specialists remain discoverable and can be used directly by agents.
Bodies are loaded as needed. Onboarding's shared instructions point to `ignyte:work`.

`babysit` is promoted from Hounddog. It distinguishes one PR status check from
sustained delivery, follows current-head checks and reviews, and leaves a ready PR
open unless the task authorizes merging. A local mockup is not a deployment.
Publish the shared package and onboarding change before removing Hounddog's local
copy. Existing sessions may need to restart to discover the new skills.

Delivery follows repository and client rules. A no-PR workflow can finish with
verified local changes or an authorized local commit for human review. Commit
permission does not authorize pushing. The host, tracker, source-control type,
and review policy are resolved separately; Azure hosting does not imply PRs.

## Every skill

Original authors retain their copyrights; Ignyte maintains the adaptations.
Full provenance and licenses are in
[third-party notices](plugins/ignyte/THIRD_PARTY_NOTICES.md).

| Skill | Original author / source | Purpose |
|---|---|---|
| [work](plugins/ignyte/skills/work/SKILL.md) | Ignyte Software | Select and combine actions; track outcomes and stopping points. |
| [babysit](plugins/ignyte/skills/babysit/SKILL.md) | Ignyte Software / Hounddog | Inspect PR status or follow checks and reviews through readiness. |
| [wayfinder](plugins/ignyte/skills/wayfinder/SKILL.md) | Matt Pocock | Resolve planning decisions and sequence milestones and work. |
| [grilling](plugins/ignyte/skills/grilling/SKILL.md) | Matt Pocock | Ask focused questions about consequential product decisions. |
| [research](plugins/ignyte/skills/research/SKILL.md) | Matt Pocock | Establish facts from primary sources and experiments. |
| [prototype](plugins/ignyte/skills/prototype/SKILL.md) | Matt Pocock | Build disposable artifacts to settle design or behavior questions. |
| [to-spec](plugins/ignyte/skills/to-spec/SKILL.md) | Matt Pocock | Capture accepted scope and observable acceptance criteria. |
| [to-tickets](plugins/ignyte/skills/to-tickets/SKILL.md) | Matt Pocock | Break work into verifiable issues with dependencies. |
| [triage](plugins/ignyte/skills/triage/SKILL.md) | Matt Pocock | Assess intake and prepare actionable work. |
| [project-setup](plugins/ignyte/skills/project-setup/SKILL.md) | Matt Pocock, adapted from setup-matt-pocock-skills | Resolve existing tracker, label, and documentation conventions. |
| [diagnosing-bugs](plugins/ignyte/skills/diagnosing-bugs/SKILL.md) | Matt Pocock | Reproduce, diagnose, and verify focused fixes. |
| [tdd](plugins/ignyte/skills/tdd/SKILL.md) | Matt Pocock | Run a red-green loop when test-first work is requested. |
| [code-review](plugins/ignyte/skills/code-review/SKILL.md) | Matt Pocock | Review the actual change against standards and accepted intent. |
| [codebase-design](plugins/ignyte/skills/codebase-design/SKILL.md) | Matt Pocock | Compare interfaces, responsibilities, and test seams. |
| [improve-codebase-architecture](plugins/ignyte/skills/improve-codebase-architecture/SKILL.md) | Matt Pocock | Assess structural improvements and their tradeoffs. |
| [domain-modeling](plugins/ignyte/skills/domain-modeling/SKILL.md) | Matt Pocock | Clarify terminology and record durable decisions. |
| [writing-for-agents](plugins/ignyte/skills/writing-for-agents/SKILL.md) | Matt Pocock | Write compact instructions with clear triggers and outcomes. |
| [unslop](plugins/ignyte/skills/unslop/SKILL.md) | Lauren Tan / PStack | Edit prose for clarity, concrete meaning, and human voice. |

The `implement` and `grill-with-docs` wrappers are folded into `work` routing.
`project-setup` replaces `setup-matt-pocock-skills` and still reads existing project
configuration. Redundant templates and recipes were removed after their useful
constraints were included in the compact skills.

## Packages and ownership

| Plugin | Source | Installed on |
|---|---|---|
| `ignyte` | `./plugins/ignyte` in this repository | Claude Code and Codex |
| `codex` | `openai/codex-plugin-cc`, upstream `main` | Claude Code only |

The separate `codex` plugin drives Codex from Claude Code. Its own skills are
upstream-managed; this invocation policy applies to Ignyte's package. Personal and
repository-specific skills remain independently owned.

Neither plugin pins a version. The Ignyte marketplace follows reviewed commits;
onboarding configures updates. Changes become available after publication and a
successful client refresh, not merely when this checkout changes.

## Maintaining a skill

Use `writing-for-agents`. Keep the description precise, the body focused on useful
decisions, and completion observable. Preserve user scope and existing authority.
Set `user-invocable: false` and `policy.allow_implicit_invocation: true`; leave
`disable-model-invocation` absent or false. Keep links and provenance current.
Evaluate combined outcomes, steering, and stopping points before changing routing.
Open a PR for publication under the repository's review rules.

## Manual installation

Onboarding runs these commands for each machine:

```powershell
claude plugin marketplace add IgnyteSoftware/skills
claude plugin install ignyte@ignyte-software --scope user

codex plugin marketplace add IgnyteSoftware/skills
codex plugin add ignyte@ignyte-software
```

For an already registered marketplace, refresh it instead of blindly re-adding it.
