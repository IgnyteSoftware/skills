# Ignyte Skills

Shared agent skills for Ignyte developers, delivered as a **plugin marketplace** that
both **Claude Code** and **Codex CLI** read from the same manifest.

Installed by [`IgnyteSoftware/onboarding`](https://github.com/IgnyteSoftware/onboarding).
You do not need to clone this repo to use it.

## Why this is a separate repo

Skills change far more often than setup scripts do. Keeping them here means a new skill
reaches everyone without touching the installer, and a developer can contribute one by
pull request without going near PowerShell.

## Three layers of skills

Only the first layer lives here.

| Layer | Where | Who owns it |
|---|---|---|
| **Shared** | this repo, via the marketplace | the team, reviewed by PR |
| **Personal** | `~/.claude/skills`, `~/.agents/skills` | you, never touched by setup |
| **Repo-specific** | `.claude/skills` or `.agents/skills` in a project | committed with that project |

Marketplace skills are cached separately (`~/.claude/plugins/cache/...`) and namespaced
`plugin:skill`, so **they never collide with your own**. If you spend your time on the
frontend and want three extra Blazor skills nobody else needs, put them in
`~/.claude/skills` and they will coexist with everything here.

If a skill would only ever make sense inside one repo, prefer the third layer. A skill
in your user directory fires on every project, including ones where it is wrong.

## What is here

| Plugin | Source | Installed on | Version |
|---|---|---|---|
| `ignyte` | this repo, `./plugins/ignyte` | both | 0.3.0 |
| `codex` | `github.com/openai/codex-plugin-cc` | Claude Code only | tracks upstream `main` |

The `ignyte` plugin vendors one reviewed set instead of installing a second upstream
skills plugin. Ignyte controls when those copies change; upstream attribution, reviewed
revisions, and licenses are recorded in
[`plugins/ignyte/THIRD_PARTY_NOTICES.md`](plugins/ignyte/THIRD_PARTY_NOTICES.md).

Human-invoked workflows stay out of model context until a developer selects them:
`code-review`, `grill-with-docs`, `grilling`, `implement`, `prototype`, `research`,
`tdd`, `to-spec`, `to-tickets`, `triage`, and `wayfinder`.
The remaining engineering skills are model-discoverable from narrow task descriptions:
`codebase-design`, `diagnosing-bugs`, `domain-modeling`, `resolving-merge-conflicts`,
`verify-this`, and `writing-for-agents`. Pstack's `unslop` is the deliberate
exception whose upstream description says it must always apply.

`codex` is OpenAI's official plugin for driving Codex **from** Claude Code.
Use `/codex:review` and `/codex:adversarial-review` for a second opinion from a different
model, and `/codex:rescue`, `/codex:transfer`, `/codex:status`, `/codex:result`,
`/codex:cancel` to delegate work and manage background jobs. Run `/codex:setup` once after
installing.

It is deliberately not installed into Codex CLI, which would point Codex at itself. It
needs Node 18.18+ and a signed-in Codex. `install.ps1` provides both. Its usage counts
against your Codex limits.

Only the Claude-only `codex` integration tracks upstream `main`. Shared engineering
skills change through reviewed commits in this repository.

## Adding an Ignyte skill

1. `plugins/ignyte/skills/<skill-name>/SKILL.md`
2. Write `description` so an agent can tell when the skill applies. It is the only part
   loaded until the skill fires, so it is doing the routing.
3. For a human-invoked skill, set `disable-model-invocation: true` for Claude Code and
   `policy.allow_implicit_invocation: false` in `agents/openai.yaml` for Codex.
4. Preserve source attribution and the applicable license when vendoring.
5. Open a pull request.

## Manual install

`onboarding`'s `install.ps1` does this for you.

```powershell
claude plugin marketplace add IgnyteSoftware/skills
claude plugin install ignyte@ignyte-software --scope user

codex plugin marketplace add IgnyteSoftware/skills
codex plugin add ignyte@ignyte-software
```

Codex needs this run once per machine. Unlike Claude Code, it cannot register a
marketplace from repo-level config.
