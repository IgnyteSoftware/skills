---
name: tdd
description: Use a red-green loop when the user explicitly requests test-first development. Do not infer permission to add tests from an ordinary implementation or bug-fix request.
user-invocable: false
---

# TDD

Choose the observable behavior and public boundary from the accepted requirements. Reuse agreed test scope; ask only when the expected behavior or scope is unresolved. Follow repository testing conventions.

Write one test with an independently justified expected result. Run it and confirm it fails for the intended missing or broken behavior, not a setup error. Implement the smallest correction, then run it again and check affected behavior.

Repeat by behavior. Prefer real integrations where practical, and substitute external boundaries rather than mocking internal steps. Avoid tests that repeat the implementation or pass when the behavior is removed.

Refactor only within the accepted scope while keeping the signal meaningful. Finish with the observed red/green evidence, checks run, and coverage limits.
