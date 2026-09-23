---
name: domain-modeling
description: Clarify domain terminology, business rules, and durable architectural decisions. Use when the model or shared glossary changes, or an ADR is warranted.
user-invocable: false
---

# Domain modeling

Edit domain documents only within the task's authorized scope. For read-only work, propose terminology and decision-record updates in the requested response or artifact instead of changing project files.

Read the existing glossary and relevant ADRs. Follow a context map when the repository has one. Compare terms with actual behavior and challenge ambiguities using concrete examples; settle product meaning with the user when evidence cannot decide it.

Record agreed terms and relationships in the project's existing glossary. Create documentation only when there is something useful to capture, and follow established locations and formats. Keep implementation plans out of the glossary.

Record an ADR when a consequential choice has real alternatives and a reason a future maintainer would otherwise miss. Include context, decision, consequences, and relevant evidence. Preserve superseded decisions as history according to repository conventions.

Finish with the resolved concepts, any unresolved business decisions, and the documents changed. Reading terminology alone does not require a modeling exercise.
