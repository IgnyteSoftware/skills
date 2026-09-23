# Repository workflow

Draft template. Complete and approve this in the client's permitted location before
using it as standing policy. Reference it from the repository's agent instructions.

- Policy owner and approved revision: [person/team and revision]
- Repository identity and delivery endpoint: [approved location; no credentials]
- Source control: [Git / TFVC / other; verify]
- Work source: [tracker/project or local task documents; verify]
- Local workspace rules: [existing checkout, branch, worktree, or TFVC workspace]
- Agent actions permitted: [read, local edit, verification, and any approved writes]
- Human checkpoints: [before commit, publication, integration, or deployment as applicable]
- Review artifact/channel: [patch/package/commit and where the human records a decision]
- Delivery method: [human handoff / branch / PR / other]
- Completion: [what the agent must return at the permitted endpoint]
- Required validation: [link to repository instructions; add only exceptions]
- Enforcement: [runtime/identity/server controls and owner; describe verified controls only]

An individual task can narrow this policy. It can expand scope only through an
authorized decision within the client's rules. A task document cannot grant missing
credentials or bypass host/server controls. Unresolved publication permissions mean
prepare the local handoff and identify the missing decision.

## No-PR human-handoff example

The user described the client's repositories as Azure-hosted with no PR process and required
human review, then clarified these action boundaries:

- Prepare authorized local changes and run the relevant verification.
- Provide findings, full change package, base revision, and verification evidence.
- Leave changes uncommitted unless the task authorizes a commit.
- Commit when explicitly requested, after required verification and review gates.
  The resulting local commit can be the human-review artifact.
- Push only on explicit instruction for the relevant changes and endpoint. Commit
  permission does not grant push permission. Honor approval already given in scope.
- Integration and deployment require their own authority. PR babysitting does not apply.

This example does not establish the configured source-control type, whether Azure
Boards is used, the designated reviewer, or the server permissions. Verify those in
the target repository. Keep local commit and remote publication separate; if a tool's
“check in” writes to the server, do not treat it as a local commit. Review the completed
profile before installing it as client policy.
