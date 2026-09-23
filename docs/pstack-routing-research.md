# PStack routing research

Reviewed 2026-09-22. This is a source review and design recommendation, not a runtime evaluation or implementation.

PStack main resolved to `86ecc82055e4d3cb567e72c56f390800a4978c9b`, plugin version `0.15.2`. I also read the router, manifest, and license at Ignyte's vendored revision `fd6dd6f7276956a532bb78a748a8d2818b6eb5f4`, version `0.14.1`. GitHub page fetch failed; the GitHub API and raw source downloads succeeded. All links below pin the reviewed source.

## What PStack actually does

`poteto-mode` is a front door. It classifies the request, opens a matching playbook, and calls other skills when steps require them. The guide explicitly tells users to describe the goal rather than enumerate skills. Its diagram shows branches for investigation, bugs, features, refactoring, performance, and bespoke work. This is an agent interpreting written routing rules. The reviewed entrypoint is not a standalone graph execution engine. [Routing guide](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/docs/guide/02-poteto-mode.md).

The router layers three things: task playbooks, cross-cutting triggers such as design review or prose editing, and principle skills read when needed. A helper agent reads the same router before work. The plugin still exports the whole skills directory. One front door does not mean one installed skill, one available capability, or one loaded description. The sources do not measure startup context savings. [Router](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/SKILL.md), [agent](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/agents/poteto-agent.md), [manifest](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/.cursor-plugin/plugin.json).

Planning has its own deliverable and stops before implementation. The feature playbook delegates implementation, verifies behavior, and opens a PR. Babysit distinguishes one status check, comment handling, background triage, and driving to merge-ready. It separates readiness from authorization to merge. Those distinctions are useful graph edges for Ignyte. [Planning](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md), [feature](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/playbooks/feature.md), [babysit](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/playbooks/babysit.md).

## Approaches for Ignyte

These are design judgments drawn from the source, not measured routing results.

| Approach | Advantages | Costs and failure modes |
|---|---|---|
| One user-callable router, specialist playbooks underneath | Explicit opt-in; one command to remember; consistent transitions and completion rules. | A forgotten invocation bypasses the workflow. Making it callable changes the earlier policy that every skill is agent-only. Router mistakes affect every task. |
| Automatically selected router, specialist playbooks underneath | Ordinary requests are enough; fits the earlier agent-only policy; one place to define workflow decisions. | Selection remains model behavior. An overly broad trigger adds ceremony to simple questions; an overly narrow trigger misses work. Needs a rule for the active task and user steering. |
| Directly discoverable specialist skills | Small tasks can reach the relevant instructions directly; specialist descriptions carry precise triggers. | Overlapping descriptions compete. Transitions and permission rules get duplicated. Users and agents can enter halfway through a workflow. |
| Automatic router plus directly discoverable specialists | Preserves specialist usefulness while providing a normal entrypoint. Existing skills can stay intact during migration. | Both router and specialist can trigger; ownership must be explicit. Retaining all descriptions does not establish context savings. |

My preference is a small automatic router with selected specialist skills retained. It should own task state and transitions, while specialists own their actual work. After observing selection behavior, move trivial wrappers into router references. A single public command can be an optional convenience if the user wants to revise the earlier no-user-invocation policy. It need not be the only way normal language enters the workflow.

A conceptual path is request -> inspect context -> choose investigation, planning, diagnosis, or implementation -> verify -> review -> PR preparation -> babysit when delivery scope calls for it. Verification failure returns to the relevant work. A planning-only request stops at its plan. A PR status question gets one check unless continued monitoring is requested. Merge remains a separate authorization boundary. This graph describes intent and evidence; it does not itself switch the host application's actual Plan mode.

## What to adopt and what to leave behind

Adopt conditional loading, explicit stop conditions, reuse of the same routing contract in delegates, and evidence-driven transitions. Preserve the user's current scope while new messages steer the task. Give simple work a short path.

Do not copy the entire PStack policy. Its feature playbook mandates delegation; its planning template mandates a large verification program. Those choices add machinery to small Ignyte tasks. The router also broadly authorizes external actions such as team messages. Ignyte must retain session authorization and the host's rules. Its named Cursor tools, agent types, pinned model defaults, and `mode` metadata are source-specific integration details. [Router](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/SKILL.md), [feature](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/playbooks/feature.md), [planning](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md).

Invocation needs a separate compatibility decision. PStack's router declares `disable-model-invocation: true` and Cursor-specific `mode: true`. Copying that metadata would conflict with the proposed automatically selected entrypoint. PStack source alone cannot establish how Claude Code and Codex load, hide, select, or invoke that configuration. Verify discoverability and explicit selection separately on the installed versions of both CLIs. Do not describe one visible command as proof that all other skill descriptions disappear, or that users cannot explicitly select helpers. [Reviewed frontmatter](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/skills/poteto-mode/SKILL.md).

## Authorship and reuse

Lauren Tan is the named PStack author in both reviewed plugin manifests. Both licenses carry `Copyright (c) 2026 Lauren Tan`. This corrects the earlier claim that no individual author was recorded for the source of `unslop`. Ignyte's existing `licenses/pstack-MIT.txt` already preserves that notice. MIT requires preserving its copyright and permission notice in copies or substantial portions. If Ignyte copies more text, update the third-party notice to identify the added material and revision. An independently written router can cite the inspiration without claiming to be PStack. [Current manifest](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/.cursor-plugin/plugin.json), [pinned manifest](https://github.com/cursor/plugins/blob/fd6dd6f7276956a532bb78a748a8d2818b6eb5f4/pstack/.cursor-plugin/plugin.json), [license](https://github.com/cursor/plugins/blob/86ecc82055e4d3cb567e72c56f390800a4978c9b/pstack/LICENSE).
