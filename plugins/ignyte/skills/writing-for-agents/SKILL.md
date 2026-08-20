---
name: writing-for-agents
description: Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md.
---

Reference for writing any document an agent consumes, including a skill, an `AGENTS.md` or `CLAUDE.md`, and a document reached by a pointer. Packaging differs, but the same levers make the process predictable without forcing the same output every run.

When the document you're writing is a skill, read [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for frontmatter, invocation choice, and router skills.

## Context pointers

A **context pointer** is a reference in the agent's context that names out-of-context material and says when to load it. A skill's description is one. A line in `AGENTS.md` that names another document is the same kind of object. The pointer's _wording_, not its target, determines when and how reliably the agent loads the material. A weak pointer to required material is a variance bug. Sharpen the wording first, and inline the material only if that fails.

A pointer states what the material is and lists the **branches** that should load it. A branch is a distinct case the document handles, so different runs may take different paths. Every word in an always-loaded pointer costs context on every turn, so prune it harder than the body:

- **Front-load the leading word.** The pointer is where it does its triggering work.
- **One trigger per branch.** Synonyms that rename a single branch are one branch written twice; collapse them and keep only genuinely distinct branches.
- **Cut identity the body already carries.**

## The two loads

Every document and pointer you add spends one of two budgets:

- **Context load.** Always-loaded material such as an `AGENTS.md` line or a skill description spends tokens and attention every turn, whether or not it applies.
- **Cognitive load.** The human must remember which documents exist and when to use them. The human is the index. Spend this load where human judgement matters and remove it where it does not.

Material reached only through a pointer escapes context load at the price of the pointer's own line; material with no pointer at all rides entirely on cognitive load.

## Information hierarchy

A document contains **steps**, the ordered actions an agent performs, and **reference**, the definitions, rules, or facts it consults on demand. A document may contain either type or both. The core decision is where each piece sits on the **information hierarchy**, ranked by how soon the agent needs it:

1. **In-file step.** What the agent does, in order. This is the primary tier.
2. **In-file reference.** Material consulted on demand. A flat set of peers, such as every rule in a review, may belong on one tier. That arrangement is not a smell.
3. **Disclosed reference.** Material moved into a separate file and loaded only when a context pointer fires. It may be a sibling file or an external reference available to several documents.

Push too little down and the top bloats; push too much and you hide material the agent actually needs. That tension is the whole decision.

**Progressive disclosure** moves material down the ladder, out of the main file and behind a pointer, so the top stays legible. Its main purpose is to protect the hierarchy, not to save tokens. Branching is the cleanest test. Inline what every branch needs, and disclose what only some branches use. Reference that should be disclosed can bury a document's steps and make the agent miss them. That changes behavior, not just legibility.

**Co-location** is the within-file companion. The ladder decides _how far down_ a piece sits, while co-location decides _what sits beside it_. Keep a concept's definition, rules, and caveats under one heading so reading one part brings its neighbours with it. Grouped material reads like documentation written for the agent; scattered material does not. Duplication repeats one meaning in two places, while scattering breaks one meaning across many.

**Sprawl** is the failure mode here: a document simply too long, even when every line is live and unique. Attention thins across the excess, and every extra line is one more to keep relevant. The cure is the ladder: disclose reference behind pointers, and split by branch or sequence so each path carries only what it needs.

## Steps and completion criteria

Every step ends on a **completion criterion**, the condition that tells the agent the work is done. Two properties make it a lever:

- **Clarity.** Can the agent tell done from not done? A vague bound such as "understanding reached" invites **premature completion**, where attention shifts to finishing before the step is complete. Visible **post-completion steps** pull the agent forward, while a clear criterion resists that pull. First, sharpen the bound. If the bound cannot be made precise and the agent still rushes, split the sequence so later steps cross a real context boundary. A handoff or subagent dispatch clears those steps from view; an inline call does not.
- **Demand.** How much does the criterion require? "Every modified model accounted for" forces more legwork than "produce a change list." Legwork is the investigation demanded by the wording, even when it is not a separate step. Demand also applies to reference. "Every rule applied" gives an all-reference document an exhaustiveness bar.

The strongest criteria are both checkable and exhaustive.

## When to split

Splitting one document into two spends one of the two loads, so split only when the cut earns it:

- **By sequence.** Split steps when later work tempts the agent to rush the current step. Keeping later steps out of view drives more legwork on the current task. Merging sequences has the opposite effect and can invite premature completion.
- **By invocation.** See [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md).

## Leading words

A **leading word** is a compact concept from the model's pretraining that the agent can think with while running the document, such as _lesson_, _fog of war_, or _tracer bullets_. Repeating the token builds a distributed definition and anchors a region of behaviour with few words. An invented term can work if defined clearly, but it brings no useful prior meaning. Prefer an existing term when one fits.

It anchors twice. In the body, _execution_: the agent reaches for the same behaviour every time the word appears, and inside flat reference it focuses attention on a class of thing to look for. In a pointer, _invocation_: when the same word lives in your prompts, your docs, and your codebase, the agent links that shared language to the material and reaches it more reliably.

Look for passages that a leading word can replace. A triad repeated at three sites or a pointer that spends a sentence on one idea may collapse into one token:

- "fast, deterministic, low-overhead" → _tight_ (a _tight_ loop).
- "a loop you believe in" → _red_. A fuzzy gate becomes a binary state: the loop goes _red_ on the bug or it does not.

This saves tokens and gives the agent a sharper concept to think with. Look for restatements that a leading word can retire.

**Negation** is the failure mode beside this lever. A prohibition brings the forbidden behaviour into context and makes it more available. In _don't think of an elephant_, the elephant dominates while the weak negation fades. Prompt the **positive** by stating the target behaviour, such as "write one-line comments." Use a prohibition only for a hard guardrail that cannot be phrased positively, and pair it with the desired behaviour.

## Pruning

- Keep each meaning in a **single source of truth** so changing behaviour is a one-place edit. **Duplication** repeats the same meaning, increasing maintenance and context costs while giving it more prominence than it deserves. A leading word does the inverse: it repeats a token, not the meaning.
- The **environment** is also a source of truth. This includes `package.json` scripts, config files, directory layout, and `--help` output. A document that restates those facts is a **cache** and earns its cost only when the lookup is expensive. Cache what the agent cannot find by looking, such as an unwritten convention or the reason behind a surprising choice. Leave simple lookups to the environment, where they cannot go stale.
- Check every line for **relevance**: does it still bear on what the document does? A line loses relevance by never bearing on the task (mere exposition, or a branch that should be disclosed) or by going stale as the behaviour or world it describes changes. Shorter documents are easier to keep relevant. Without a pruning discipline the default fate is **sediment**: stale layers that settle because adding feels safe and removing feels risky, until you must core down through them to find what is still live.
- Hunt **no-ops** sentence by sentence. An instruction the model already follows by default spends context without changing behaviour. The test is whether the instruction changes behaviour relative to the model's default. Settle disagreements by running the document, not by debating the default. Delete a sentence that fails instead of trimming it. Apply the same test to leading words. A weak phrase such as _be thorough_ may be a no-op where a stronger word such as _relentless_ changes behaviour.
