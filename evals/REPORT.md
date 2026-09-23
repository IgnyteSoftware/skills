# Local workflow comparison

The retained 18-skill package completed the essential outcomes in seven paired
tasks against baseline `cb6d092`. Five additional candidate runs exercised fixes
and unnamed planning requests. All 19 executions pass the final structural
checks. Independent semantic review found no material loss in these exercised
workflows, with planning and handoff caveats below. This is evidence for a review
branch, not a claim that every workflow or installed client is proven.

## Method

Each task ran in a separate disposable local Git repository with a fresh Codex
agent. Both variants received the same task and source fixtures and discovered
relevant instructions from their supplied skill catalog. Workers could not read
the grading rubric or other runs and were instructed to stay offline. Baseline
skills were exported from `cb6d092`; candidate snapshots came from this work.
The [results](results.json) record each actual snapshot and artifact hash.

This tests execution with explicit catalog discovery. It does not measure the
host's unaided automatic selection rate. The installed Codex loader independently
loaded all 18 candidate skills as enabled with no errors. Claude plugin and
marketplace manifests passed validation, but no Claude task-execution comparison
was performed. Display metadata and invocation policies were checked separately.

The evaluator checks actual code behavior, unchanged inputs, Git history and
authorship, canonical map records, and simulated provider events. Its result is
`structural_passed`, with semantic review explicitly pending. A separate agent
reviewed paired artifacts labelled A/B without being told which was the candidate.
A was candidate; B was baseline. Follow-up artifacts were assessed independently
as well. Output similarity means equivalent requested behavior, not matching prose.

## Paired results

| Task | Baseline | Candidate | Evidence |
|---|---|---|---|
| Coherent specification and dependent drafts | Pass with caveats | Pass with caveats | Both covered roles, states, concurrency, audit, recovery, acceptance, and unresolved emergency policy without implementing it. |
| Research, executable prototype, then plan | Pass | Pass | Both passed ten independent reservation-contract assertions and preserved production code. Research and plans distinguished observations from assumptions. |
| No-PR client implementation, no commit | Pass | Pass | Both fixed adjacency, retained overlap/resource isolation, passed the five existing checks, and left changes uncommitted. |
| No-PR client implementation, local commit | Pass | Pass with handoff caveat | Both created valid local commits with the configured human identity and unchanged tests. Initial candidate handoff omitted its commit SHA; a later run corrected this. |
| Staged, unstaged, and untracked review | Pass | Pass | Both found the endpoint defect and the untracked helper's incorrect resource, without modifying source or index. |
| Simulated PR follow-through | Pass | Pass | Both fixed verified feedback, committed and simulated-published a new head, inspected its checks, replied/resolved, and left the PR open. |
| Resume an existing decision map | Pass with scope caveat | Pass | Both preserved prior decisions and another worker's claim, resolved the factual ticket, and kept the unanswered human choice open. |

The final grader was rerun against these outputs after its review fixes. The first
paired PR runs used an earlier simulator that checked the working tree. Their
commits independently contain the verified fix, but those runs are not retroactive
evidence of the new provider implementation. An additional candidate delivery run
exercised the final provider, which checks an exported committed snapshot.

## What changed because of the evaluation

- Restored the conditional lifecycle for existing Wayfinder maps: claim, resolve,
  update the canonical index, reconcile newly clear questions, preserve other workers.
- Routed substantial specifications through Wayfinder while retaining direct small,
  settled specification drafting.
- Clarified technical inspection versus human product decisions, and development
  dependencies versus integration/release gates.
- Required the exact base revision and produced commit SHA in human handoffs.
- Clarified that PR delivery pushes the work branch, not the integration branch.
- Made unmet required review gates block publication; research and domain-document
  edits remain within task authority.
- Tightened the grader for history rewrites, changes hidden in commits, attribution,
  deleted/replaced map records, stale PR events, and uncommitted simulated checks.

The five follow-ups were a repeated spec, an unnamed spec request, an unnamed map
request, a final commit handoff, and final simulated delivery. They passed structural
and independent semantic assessment. The unnamed prompts selected Wayfinder from
the supplied catalog without the task naming that skill.

## Quality differences and remaining limits

Neither variant was uniformly better. The initial candidate used shorter ticket
drafts and explicit acceptance mappings, but bundled some work into broader slices.
The baseline split some slices better but turned technical inspection and time-entry
choices into extra human gates. Both sometimes asked more questions than necessary.
Follow-up guidance reduced those unnecessary dependencies; specification wording
still needs a human to distinguish accepted requirements from proposed ordinary
behavior. The deliberately unanswered business questions remained unanswered.

The candidate map resolved factual retry guidance directly. The baseline opened an
additional interaction/wording question overlapping existing human/prototype work.
Both were usable; the candidate stayed closer to the map's factual destination.
The initial missing commit identifier was a modest handoff regression, corrected
and verified in a fresh run rather than hidden by the overall pass count.

Review [the baseline spec](samples/baseline-spec/artifacts/spec.md) and
[its tickets](samples/baseline-spec/artifacts/tickets.md) beside
[the later candidate spec](samples/candidate-spec/artifacts/spec.md) and
[its tickets](samples/candidate-spec/artifacts/tickets.md). Samples include their
synthetic input documents. Client labels were generalized for publication; original
artifact hashes are retained in the results. Skills themselves are not duplicated
inside these samples.

These are small synthetic tasks distilled from observed workflows. They do not
cover live human interviews, UI/browser prototypes, bulk tracker triage, TDD,
production deployment, every architecture audit, or real Azure/GitHub integration.
The 18-skill inventory remains intact, but that alone is not behavioral proof for
every specialist. No company-wide deployment or cache refresh was performed.

The local provider and its logs are writable fixtures, not a security boundary.
An absent Git remote does not prove that no external push was attempted. Checks
and artifact review support the reported local outcomes; they are not an audited
network sandbox or an adversarially tamperproof agent harness.

## Other checks and publication

- Python evaluator formatted and linted with Ruff; positive controls and deliberately
  failing controls passed. Those include invalid prototypes, unauthorized commits,
  amended history, attribution, unrelated commit content, review mutations, deleted
  maps, invented human resolutions, stale delivery evidence, and unauthorized merge.
- All 18 frontmatters and invocation files validated; runtime references resolve.
  Skill-creator's older core validator required omitting the documented Claude
  `user-invocable` flag from temporary copies only; real flags were checked separately.
- Codex 0.156.0 loader: all 18 enabled. Claude Code 2.1.280 manifests: valid, with
  the intentional versionless-package warning.
- Onboarding suite: 97/99. The same two pre-existing `web_search` assertions fail:
  one expects a currently owned key removed, and one creates a duplicate TOML key.
  No onboarding runtime scripts or configuration changed in this branch.
- Adversarial reviews used gpt-6-sol and Claude Opus 5.5. Both final static reviews
  reported no blockers after corrections. Neither review was represented as a
  substitute for the executed evaluations or required client human review.

The publication commit uses the baseline as its parent so earlier unpublished
drafts containing private session identifiers are not included in branch history.
Only the reviewed feature branch is published; merging and company-wide rollout
remain separate decisions.
