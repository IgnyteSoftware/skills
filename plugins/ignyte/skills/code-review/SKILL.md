---
name: code-review
description: Review a PR, branch, commit, or uncommitted change against repository standards and the accepted task. Use for requested reviews and required pre-publication review gates.
user-invocable: false
---

# Code review

Establish the requested scope before reviewing. Use the PR or branch merge-base for branch work, the parent for a single commit, and the staged or working-tree changes when requested. Include relevant untracked files in WIP reviews. Inspect actual patches and surrounding behavior; a branch diff alone does not cover uncommitted work. Infer an unambiguous base from context; ask only when the choice changes the review.

Review two independent questions: does the change follow repository standards, and does it satisfy the accepted issue, specification, or conversation? Read the source requirements and relevant callers. An empty diff is an observation, not a review of omitted changes.

Use independent reviewers where required or useful. When policy requires multiple models, use genuinely different available models and identify them. Two agents on the same model do not meet that gate. An unmet required review gate blocks publication; report the missing reviewer or evidence instead of claiming the gate passed.

Prioritize reproducible defects, missing behavior, scope expansion, and maintainability problems with a concrete consequence. Separate pre-existing issues and uncertain suspicions from findings in this change. A review-only request stays read-only.

Return actionable findings with severity, location, failure mechanism, and suggested correction, or state that none were found. Include the reviewed base/head or working-tree scope, verification performed, and limitations. Recheck fixes and any changed head before giving a final verdict.
