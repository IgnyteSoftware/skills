---
name: project-setup
description: Discover or establish repository conventions needed by the workflow, including issue tracking, labels, and domain documents. Use for requested setup or genuinely missing conventions.
user-invocable: false
---

# Project setup

Read repository instructions, remotes, existing tracker configuration, labels, and documentation layout. Reuse established conventions, including docs/agents/issue-tracker.md, triage-labels.md, and domain.md when present. Missing skill-specific files alone do not justify a setup interview or new files.

Resolve hosting, source-control type, work source, local workspace rules, human checkpoints, and permitted delivery actions separately. A remote identifies a destination, not permission to write there. For authorized setup, use [the workflow template](references/repository-workflow.md) only for missing conventions; keep client-specific policy in the client's approved location and reference it from loaded repository instructions. Describe enforcement only when verified; instructions alone do not restrict credentials.

When a workflow needs an unresolved choice, infer it from the active issue or repository where possible. Ask only when multiple plausible trackers, label meanings, or documentation locations would change the work. Local drafts remain valid when publication is not requested or available.

For an authorized setup change, record only the agreed conventions in the existing instruction or configuration files. Preserve imports and user-owned sections. Prefer shared AGENTS.md guidance with a CLAUDE.md import where the repository already uses that arrangement.

Finish with the resolved conventions and any files changed. Do not impose a new label state machine, tracker, or domain-document structure merely because a skill could use one.
