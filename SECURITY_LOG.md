# Security Hardening Log

Date: 2025-12-02

Scope: Scheduled secrets exposure scan and GitHub Actions workflow hardening.

Summary:
- No potential secrets detected in tracked files or in the last 200 commits (common patterns scanned; no `.gitleaks` allowlist configuration found).
- Pinned third-party GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 → 34e114876b0b11c390a56381ad16ebd13914f8d5
  - actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@v4 → e4db8464a088ece1b920f60402e813ea4de65b8f
- Added explicit least-privilege token permissions to `test.yml`:
  - `permissions: { contents: read }`
- Guarded PR-context steps that use secrets to avoid fork leakage/false failures:
  - Added `if: ${{ github.event.pull_request.head.repo.fork == false }}` to steps invoking `cursor-agent` in:
    - `.github/workflows/visual-testing.yml`
    - `.github/workflows/code-review.yml`
    - `.github/workflows/update-docs.yml`
    - `.github/workflows/translate-keys.yml`

Risk notes:
- No `pull_request_target` events detected.
- No deprecated `set-env`/`add-path` usage detected.

Recommendations:
- If secrets scanning should be extended, add a repository-specific `.gitleaks.toml` and enable org-level scanning.
- Continue pinning any new third-party actions by SHA and set default workflow `permissions` explicitly.
- For PR workflows that must run from forks, avoid using repository secrets or gate secret-dependent steps as done here.

Copyright Anysphere Inc.

# Security Hardening Log

Date: 2025-11-04
Branch: audit/gha-hardening

Summary of proposed changes
- Pin reusable GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 ? 08eba0b27e820071cde6df949e0beb9ba4906955
  - astral-sh/setup-uv@v4 ? 38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@v4 ? ea165f8d65b6e75b540449e92b4886f43607fa02
  - actions/setup-python@v5 ? a26af69be951a213d495a4c3e4e4022e16d87065
- Replace deprecated Chrome install (apt-key) with browser-actions/setup-chrome@c785b87e244131f27c9f19c1a33e2ead956ab7ce (v1).
- Add least-privilege workflow permissions to `test.yml` (`contents: read`).

Findings
- No potential secrets detected in tracked files or the last 200 commits.
- No usages of `pull_request_target` found.
- Existing workflows that push changes (docs/translate/fix-ci/conflicts) retain required `contents: write`/`pull-requests: write` permissions.

Notes
- This run lacks `workflows` permission to push changes under `.github/workflows/`. Proposed edits are provided under `proposals/gha-hardening/` for review and application.

Recommendations
- Keep actions pinned to SHAs. When updating versions, resolve the tag to a new SHA and update here.
- Prefer dedicated setup actions over custom package installs where feasible.
- If adding new workflows, include a top-level `permissions:` block with the minimum required scopes.

Verification
- After merging, monitor the next workflow runs for any permission-related errors; widen only where strictly necessary.
