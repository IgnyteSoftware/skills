---
name: writing-for-agents
description: Write or revise skills and repository instructions so agents can choose and complete the right work. Use for SKILL.md, AGENTS.md, CLAUDE.md, and their supporting guidance.
user-invocable: false
---

# Writing for agents

Include instructions that change decisions or prevent a demonstrated failure. Trust the agent with ordinary mechanics. Preserve user intent, repository conventions, and the boundary between selecting a skill and authorizing its actions.

Make the description a precise context pointer: what the skill does and when it applies. State the outcome and the decisions that matter in the body. Give uncertain branches explicit triggers and finish conditions; avoid fixed rituals, repeated permission gates, and arbitrary counts.

Keep each rule in one authoritative place. Group related guidance, and move substantial branch-specific material behind a link only when it earns a separate file. Prefer a small self-contained skill over a router for its own sake. Examples should resolve ambiguity, not repeat the rule.

For Ignyte skills, keep a nonempty name and description, set user-invocable to false, and leave model invocation enabled. Set policy.allow_implicit_invocation to true in agents/openai.yaml. Claude Code supports the user-invocation restriction; do not claim Codex enforces an equivalent restriction.

Validate metadata and links, then exercise representative requests when behavior changed. Test combined outcomes, user steering, and stopping points as well as the happy path. Report observed behavior separately from what the instructions merely intend.
