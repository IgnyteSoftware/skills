# Local workflow evaluations

These fixtures exercise complete tasks without external services. They compare outputs and repository effects, not skill names or document headings.

Prepare a fresh directory for each case and variant:

```powershell
python evals/run.py prepare --case research-prototype-plan --dest C:\Temp\ignyte-eval\candidate-research --skills plugins\ignyte\skills
```

Give a fresh worker the generated `TASK.md` and that directory as its workspace. The optional `--skills` directory is copied to `.agents/skills`, Codex's repository discovery location; no production files or personal configuration are changed. Use the same prompts for both variants. Workers must not read this evaluation directory or the adjacent grader state file.

The recorded executions use fresh Codex agents instructed to discover relevant skills from the supplied catalog. This evaluates those workflows when discovered, not automatic host routing or Claude behavior. `.agents/skills` does not establish Claude discovery. `skills_installed` records whether preparation received a skills directory; it is not proof that a worker read or applied a skill. Check the execution trace for that evidence.

After the worker finishes:

```powershell
python evals/run.py check --dest C:\Temp\ignyte-eval\candidate-research
python evals/run.py self-check
```

`check` returns nonzero for failed observable requirements. Its `structural_passed` result leaves the verdict `pending-semantic-review` until independent review; it does not claim complete workflow success. The adjacent `*.evaluation-state.json` file belongs to the evaluator, outside the worker workspace. Keep it with the result directory. All fixtures start with a local Git commit, no remotes, and an explicit fixture-only human identity. No configured remote is not proof that no push was attempted; inspect the trace. Cases requiring code verification include existing executable checks. Run Python without optimization; the harness rejects `-O` and child probes ignore `PYTHONOPTIMIZE`.

The PR case uses `provider.py`, a clearly labeled simulation. It records fake pushes and review operations in local files. It has no network code, authentication, or real provider integration. Its required check executes the committed head's existing checks in a temporary directory after a simulated push. The fixture review gate is local source review and the existing check; it does not exercise the organization's multi-model publication gate. Thread operations must follow the latest push on the final head, followed by a final state inspection.

Provider state and logs are writable by the worker. They are not tamperproof and cannot establish hostile-agent safety. Independently inspect traces, artifacts, and committed source. Earlier runs that used a previous fixture/provider revision must retain that provenance; regrading them cannot retroactively establish that the new provider executed.

Read `rubric.md` for independent semantic review. Mechanical success cannot establish that a specification is coherent, a recommendation is justified, or a handoff is useful. Record those findings separately, with artifact evidence. Compare baseline and candidate on completeness, correctness, unnecessary work, and permission boundaries. Do not equate matching prose with matching quality.

`self-check` includes correct prototypes, local fixes, map resumption, and simulated delivery. Deliberate failures cover missing fixes, broken prototypes, unauthorized commits, rewritten initial history, attribution, wrong committer identity, unrelated intermediate commits, read-only staging/mutations, deleted maps and prior links, falsely closed human decisions, another owner's ticket edits, stale PR events, missing final inspection, dirty-only fixes, simulated merging, and optimized Python. It runs only in newly created temporary directories. Semantic quality remains outside these assertions.
