# Security Hardening Log

Date: 2025-11-30
Branch: audit-workflow-hardening

Summary of audit (proposed changes)
- Pin GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 → @34e114876b0b11c390a56381ad16ebd13914f8d5
  - actions/setup-python@v5 → @a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@v4 → @e4db8464a088ece1b920f60402e813ea4de65b8f
  - actions/upload-artifact@v4 → @ea165f8d65b6e75b540449e92b4886f43607fa02
- Add least-privilege permissions where missing:
  - `.github/workflows/test.yml`: add `permissions: contents: read`
- Add concurrency guardrails to PR-triggered workflows to avoid duplicate runs:
  - `concurrency: group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}` with `cancel-in-progress: true`
- Prevent secrets usage on forked PRs by gating jobs/steps:
  - Add `&& !github.event.pull_request.head.repo.fork` to jobs that require `secrets.CURSOR_API_KEY`.

Secret exposure scan
- Tracked files: no high-confidence secrets detected using heuristic patterns (AWS keys, GitHub tokens, SSH private keys, common password literals).
- Recent history (last 50 commits): no high-confidence secrets detected in diffs.
- If a `.gitleaks.toml` or other allowlist is added later, this workflow can respect it for future scans.

Notes
- This run’s token lacks `workflows` permission; workflow file edits cannot be pushed directly. The items above are proposed and safe to apply.
- If you’d like, open a PR from this branch that applies the workflow changes.

Quick remediation checklist
- [ ] Pin actions listed above to the provided SHAs
- [ ] Add `permissions: contents: read` to `test.yml`
- [ ] Add the `concurrency` block to PR-triggered workflows
- [ ] Gate secrets-consuming jobs on non-fork PRs
