---
name: codebase-design
description: Design or assess module interfaces, responsibilities, and test seams. Use when deciding where behavior belongs or comparing alternative designs.
user-invocable: false
---

# Codebase design

Prefer a small interface that hides substantial complexity. Count what callers must know, including ordering, invariants, configuration, and failure behavior, not just methods. Keep behavior that changes together close together and use the project's vocabulary.

Before adding an abstraction, identify the concrete caller or variation it serves. Apply the deletion test: would removing this layer eliminate complexity or merely push it into callers? Avoid speculative adapters and interfaces made only to satisfy a test.

Place tests at the public boundary that exposes the real behavior. Use dependency injection when a dependency actually varies; do not split coherent logic merely to mock it.

For a consequential interface choice, compare plausible designs against actual callers, failure cases, and maintenance cost. A prototype can settle an uncertain behavior. Recommend the smallest design that meets the known requirements and explain the tradeoff; implement only when design changes are in scope.
