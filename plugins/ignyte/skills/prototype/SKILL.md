---
name: prototype
description: Build a disposable artifact to answer a design or behavior question. Use for UI alternatives, interaction sketches, or experiments before committing to implementation.
user-invocable: false
---

# Prototype

Identify the question the prototype must answer and the evidence that would settle it. Build only enough to compare plausible options or exercise the uncertain behavior. Use realistic inputs when they affect the decision and show relevant state and limitations.

Keep the artifact disposable and separate from production changes. Default to a temporary directory for standalone demos. Use the project's runtime when fidelity requires it, in an isolated location or worktree. Follow the user's requested browser or preview environment; use an existing signed-in session only when authorized.

Make it easy to inspect or run. Stub real UI mutations. For state or logic experiments, provide resettable scenarios including invalid transitions. Avoid persistence, deployment, and production dependencies unless they are necessary to the question and authorized. Do not commit prototypes by default.

Return the artifact, how to view it, observations, and the decision it supports. Feed findings into any requested research or plan. Production implementation requires accepted scope; a prototype request alone does not supply it.
