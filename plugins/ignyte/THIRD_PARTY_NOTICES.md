# Third-party notices

Ignyte adapts these MIT-licensed sources into compact, agent-invocable skills.
The files are modified derivatives, not verbatim upstream snapshots. Original
copyright and permission notices remain in the linked license files.

| Author / source | Reviewed revision | Current derived skills | License |
|---|---|---|---|
| [Matt Pocock](https://github.com/mattpocock/skills) | `8b78b531ab965735c5dc74f6f7a219e1e37326df` | `codebase-design`, `code-review`, `diagnosing-bugs`, `domain-modeling`, `grilling`, `improve-codebase-architecture`, `prototype`, `research`, `project-setup`, `tdd`, `to-spec`, `to-tickets`, `triage`, `wayfinder`, `writing-for-agents` | [MIT](licenses/matt-pocock-skills-MIT.txt) |
| [Lauren Tan / PStack](https://github.com/cursor/plugins/tree/fd6dd6f7276956a532bb78a748a8d2818b6eb5f4/pstack) | `fd6dd6f7276956a532bb78a748a8d2818b6eb5f4` | `unslop` | [MIT](licenses/pstack-MIT.txt) |

Ignyte's modifications shorten the instructions, align them with repository and
session authorization, enable agent invocation, and remove redundant examples and
templates. `project-setup` replaces `setup-matt-pocock-skills`. The former
`implement` and `grill-with-docs` wrappers are folded into workflow routing.

`work` is Ignyte-authored, informed by the documented session audit and PStack's
playbook organization. `babysit` is Ignyte-authored and adapted from Hounddog.
The PStack source review is in [the research note](../../docs/pstack-routing-research.md).
