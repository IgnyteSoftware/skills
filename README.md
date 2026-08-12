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

If a skill would only ever make sense inside one repo, prefer the third layer — a skill
in your user directory fires on every project, including ones where it is wrong.

## What is here

| Plugin | Source | Pinned |
|---|---|---|
| `ignyte-dev` | this repo, `./plugins/ignyte-dev` | tracks `main` |
| `mattpocock-skills` | `github.com/mattpocock/skills` | commit `84fdeff` |

The two are pinned differently on purpose. **Our own skills track `main`** — we wrote
them, we want fixes to reach everyone immediately, and a bad one is ours to fix.
**Third-party skills are pinned to an exact commit**, because that is the case where a
silent upstream change would alter four developers' agent behaviour one morning with no
commit on our side to explain it.

Referencing rather than copying is deliberate: we do not redistribute Matt's work, and
upstream fixes are one pin bump away. (Anthropic's own official marketplace references
that same repo the same way, which is where the current pin comes from.)

## Updating the third-party pin

Deliberate, reviewed, and by pull request:

```bash
git ls-remote https://github.com/mattpocock/skills.git HEAD   # or pick a tag
# edit the sha in .claude-plugin/marketplace.json, open a PR
```

## Adding an Ignyte skill

1. `plugins/ignyte-dev/skills/<skill-name>/SKILL.md`
2. Frontmatter: stick to the `agentskills.io` spec fields — `name`, `description`,
   `license`, `compatibility`, `metadata`, `allowed-tools`. Non-spec fields are what
   break cross-CLI compatibility, and the whole point is one file serving both.
3. Write `description` so an agent can tell when the skill applies. It is the only part
   loaded until the skill fires, so it is doing the routing.
4. Open a pull request.

## Manual install

`onboarding`'s `install.ps1` does this for you.

```powershell
claude plugin marketplace add IgnyteSoftware/skills
claude plugin install ignyte-dev@ignyte --scope user
claude plugin install mattpocock-skills@ignyte --scope user

codex plugin marketplace add IgnyteSoftware/skills
codex plugin add ignyte-dev@ignyte
```

Codex needs this run once per machine — unlike Claude Code, it cannot register a
marketplace from repo-level config.
