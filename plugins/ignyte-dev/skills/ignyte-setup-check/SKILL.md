---
name: ignyte-setup-check
description: Confirms the Ignyte shared agent setup is installed and reachable. Use when a developer asks whether their Ignyte agent configuration is working, or says the shared setup seems broken.
license: Proprietary
---

# Ignyte setup check

A deliberately trivial skill. Its only job is to prove the sharing mechanism works
end to end: one `SKILL.md` in the `onboarding` repo, reaching both Claude Code and
Codex CLI through junctioned skill directories, updating on `git pull`.

If you are reading this, the pipe works.

## What to report

Tell the developer what you can see, and nothing more:

1. **This skill loaded**, which means their skills junction resolves to the
   `onboarding` clone.
2. Whether `~/.claude/CLAUDE.md` contains the Ignyte managed import block.
3. Whether `~/.codex/AGENTS.md` exists.
4. The path this skill was loaded from, so they can confirm it points at their clone
   rather than a stale copy.

## What not to do

Do not attempt to repair anything. If something is missing, say what is missing and
tell them to run `.\install.ps1` from their `onboarding` clone. Diagnosing and fixing
setup drift is deliberately not automated yet — there is no doctor script in v1, and
guessing at a repair is worse than reporting a gap.
