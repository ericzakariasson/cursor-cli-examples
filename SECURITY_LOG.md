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
