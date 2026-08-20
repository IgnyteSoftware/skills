---
name: wayfinder
description: Plan a huge chunk of work, more than one agent session can hold, as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear.
disable-model-invocation: true
---

A loose idea has arrived in fog. It is too big for one agent session, and the way from here to the **destination** is not visible yet. Wayfinding charts that route instead of charging at the destination. The skill records the route as a **shared map** on the repo's issue tracker. It then works through **decision tickets**, questions that resolve decisions rather than slices of a build, one at a time until the route is clear.

The destination varies per effort, and naming it is the first act of charting because it shapes every ticket. It might be a spec to hand off, a decision to lock before planning starts, or a change made in place such as a data-structure migration. The map works for any domain that fits this shape, including engineering work and course content.

## Plan, don't do

Wayfinder is **planning** by default. Each ticket resolves a decision, and the map is done when nothing remains to decide before execution. The pull to do the work usually means you have reached the edge of the map and should hand off. An effort can override this in its **Notes** and carry execution into the map itself. Without that override, produce decisions, not deliverables.

## Refer by name

Every map and ticket is an issue, so its title is its **name**. Use that name in narration and in the map's Decisions-so-far section. Never substitute a bare id, number, or slug. A wall of `#42, #43, #44` is illegible, while names read at a glance. Keep the id and URL inside the linked name.

## The Map

The map is the canonical artifact: a single issue on this repo's issue tracker, labelled `wayfinder:map`. Its tickets are child issues of the map.

The map is an **index**, not a store. It lists the decisions made and points at the tickets that hold their detail. A decision lives only in its ticket, so the map links to a short gist instead of restating it.

**Where the map, its child tickets, blocking, and frontier queries physically live is tracker-specific.** Consult the repository's tracker documentation for how _this_ repo expresses them. If no tracker has been provided, default to the local-markdown tracker.

### The map body

The whole map is a low-resolution view loaded once per session. Open tickets are **not** listed because a query finds them as open child issues.

```markdown
## Destination

<what reaching the end of this map looks like: the spec, decision, or change this effort is finding its way to. Keep it to one or two lines. Every session orients to it before choosing a ticket.>

## Notes

<domain; skills every session should consult; standing preferences for this effort>

## Decisions so far

<!-- the index. One line per closed ticket, with enough detail to judge relevance before following the link -->

- [<closed ticket title>](link): <one-line gist of the answer>

## Not yet specified

<!-- see "Fog of war": in-scope fog you can't ticket yet; graduates as the frontier advances -->

## Out of scope

<!-- see "Out of scope": work ruled beyond the destination; closed, never graduates -->
```

### Tickets

Each ticket is a **child issue** of the map; the tracker's issue id is its identity. Its body is the question, sized to one 100K token agent session:

```markdown
## Question

<the decision or investigation this ticket resolves>
```

Each ticket carries one `wayfinder:<type>` label: `research`, `prototype`, `grilling`, or `task` (see [Ticket Types](#ticket-types)).

A session **claims** a ticket by assigning it to the dev driving the map, **first**, before any work, so concurrent sessions skip it. That assignee _is_ the claim: an open, unassigned ticket is unclaimed.

Blocking uses the tracker's **native** dependency relationship. This renders the frontier in the tracker's UI, so the human can see what is available without opening the map. Only a tracker without native blocking falls back to a body convention. A ticket is **unblocked** when every ticket blocking it is closed. The **frontier** is the set of open, unblocked, unclaimed children at the edge of the known.

The answer is recorded on resolution, not in the body (see [Work through the map](#work-through-the-map)). Link assets created while resolving a ticket from the issue instead of pasting them into it.

## Ticket Types

Every ticket is either **HITL** or **AFK**. HITL means human in the loop, worked with a human who speaks for themselves. AFK means driven by the agent alone. A HITL ticket resolves only through that live exchange. The agent never stands in for the human's side of it. A grilling agent that answers its own questions has broken this rule.

- **Research** (AFK): Reading documentation, third-party APIs, or local resources like knowledge bases to surface a fact a decision waits on. Resolved by a `/research` **subagent**. Use when knowledge outside the current working directory is required.
- **Prototype** (HITL): Raise the fidelity of the discussion with a cheap, rough artifact to react to, such as an outline, a stub, or UI or logic code created with the /prototype skill. Link the prototype as an asset. Use this type when the key question is how something should look or behave.
- **Grilling** (HITL): Conversation. The default case. Always invoke the /grilling and /domain-modeling skills.
- **Task** (HITL or AFK): Manual work that must happen before a decision can be made. There is nothing to decide, prototype, or research, but the discussion is blocked until the work is done. Examples include signing up for a service so its API can be judged, provisioning access, or moving data so its shape can be seen. This type acts rather than decides, and it earns its place by unblocking a decision instead of delivering the destination. The agent drives it alone where possible (AFK); otherwise it gives the human a precise checklist (HITL). Resolve the ticket when the work is done. Record what changed and any facts that later tickets depend on, such as credential locations, URLs, or row counts.

## Fog of war

The map is _deliberately_ incomplete: do not chart what you cannot yet see. Beyond the live tickets lies the **fog of war**, the decisions and investigations you can anticipate but cannot define while earlier questions remain open. Resolving a ticket clears the fog ahead. Turn each newly specific question into a ticket until the route to the destination is clear and no tickets remain.

The map's **Not yet specified** section records that dim view: a suspected question or an area to revisit. This is the undiscovered frontier toward the destination. Everything here is in scope but not sharp enough to ticket. Write only as much as the current view supports. The section also shows collaborators where the effort is headed.

**Fog or ticket?** The test is whether you can state the question precisely now, not whether you can answer it now.

- **Ticket when** the question is already sharp, even if it is blocked and cannot be acted on yet.
- **Not yet specified when** you can't yet phrase it that sharply. Don't pre-slice the fog into ticket-sized pieces: it's coarser than a ticket, and one patch may graduate into several tickets, or none, once the frontier reaches it.

**Not yet specified** excludes what's already decided (Decisions so far), what's already a live ticket, and what's out of scope (the next section).

## Out of scope

Fog gathers only toward the destination. Because the destination fixes the scope, work beyond it is **out of scope**, not fog, and does not belong in **Not yet specified**. Record work consciously ruled out of this effort in the map's **Out of scope** section. Scope, not sharpness, determines what belongs there.

Out-of-scope work never graduates because the frontier stops at the destination. It can return only if the destination is redrawn, and then as a fresh effort rather than a resumption.

Ruling something out of scope is a scoping act, not a step on the route. A ticket may turn out to sit past the destination because it was mis-scoped while charting or exposed by a later resolution. **Close it** so it is unambiguously off the frontier. Add one line to **Out of scope** with the gist, the reason, and a link to the closed ticket. Keep it out of **Decisions so far**, which records the route actually walked. A scope boundary is not a step on that route.

## Invocation

There are two modes. In either mode, **never resolve more than one ticket per session**, except for research tickets.

### Chart the map

User invokes with a loose idea.

1. **Name the destination.** Run a `/grilling` and `/domain-modeling` session to define the spec, decision, or change this map is finding its way to. The destination fixes the scope, so settle it first.
2. **Map the frontier.** Grill again, **breadth-first** this time. Fan out across the whole space instead of following one thread deeply. Surface the open decisions and the first steps available now. **If this surfaces no fog**, the route is already clear and the journey fits in one session. You do not need a map. Stop and ask the user how to proceed.
3. **Create the map** (label `wayfinder:map`): Destination and Notes filled in, Decisions-so-far empty, the fog sketched into **Not yet specified**.
4. **Create the tickets you can specify now** as child issues of the map. Wire blocking edges in a **second pass** because issues need ids before they can reference each other. Wiring separates the frontier from the blocked. Keep everything you cannot yet specify in the fog, under **Not yet specified**.
5. **Fire the research subagents.** For each `research` ticket you just created, spin up a `/research` subagent to resolve it in parallel, capturing its findings on a throwaway `research/<name>` branch with a context pointer from the ticket.
6. Stop. Charting is one session's work and resolves nothing by hand.

### Work through the map

The user invokes this mode with a map URL or number. A ticket is **optional**. Without one, you pick the next decision.

1. Load the **map**, the low-resolution view, rather than every ticket body.
2. Choose the ticket. If the user named one, use it. Otherwise take the first frontier ticket in order. **Claim it**: assign it to yourself before any work.
3. Resolve it. **Zoom as needed.** Fetch the full body of any related or closed ticket on demand, and invoke the skills named in the `## Notes` block. If in doubt, use `/grilling` and `/domain-modeling`.
4. Record the resolution: post the answer as a **resolution comment**, **close** the issue, and **append a context pointer** to the map's Decisions-so-far.
5. Add newly surfaced tickets with create-then-wire. Turn any fog the answer has made specific into tickets, and remove each graduated item from **Not yet specified** so it lives only in its ticket. If the answer reveals that this ticket or another sits beyond the destination, **rule it out of scope** instead of resolving it on the route. If the decision invalidates other parts of the map, update or delete those tickets.

The user may run unblocked tickets in parallel, so expect other sessions to be editing the tracker concurrently.
