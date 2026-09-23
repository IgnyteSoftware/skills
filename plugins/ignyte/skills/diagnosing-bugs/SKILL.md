---
name: diagnosing-bugs
description: Diagnose and fix reported defects or performance regressions using observable evidence. Use when behavior is broken, failing, or slow.
user-invocable: false
---

# Diagnosing bugs

Establish the expected behavior and reproduce the reported symptom in the relevant environment. Choose the smallest useful signal: an existing test, CLI command, UI interaction, request replay, or measurement. For performance, capture a baseline and workload before changing code. Protect secrets and use isolated fixtures for destructive operations.

Trace the failing path and test hypotheses against that signal. Change one explanatory variable at a time. If a reproduction is unavailable, use source and logs to narrow the cause, label uncertainty, and request only the access or evidence needed to proceed. Do not present a plausible theory as a verified fix.

When a fix is authorized, make a focused correction and rerun the original scenario plus the affected checks. Write regression tests only when requested or required by repository policy, and prove they detect the defect. Remove temporary instrumentation.

Finish with the cause, the correction or diagnosis, before/after evidence, and what remains unverified. Escalate a larger architectural change as a separate decision rather than expanding a bug fix silently.
