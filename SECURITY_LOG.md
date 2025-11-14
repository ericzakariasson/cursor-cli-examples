# Repository Security Audit (Automated)

Date: 2025-11-14
Branch: audit/gh-hardening

Summary
- No potential secrets were detected in tracked files or in the last 300 commits of git history.
- Pinned reusable GitHub Actions to immutable commit SHAs.
- Added minimal default permissions to workflows missing them.
- Added shell safety guards to network install steps.

Changes
- Actions pinning:
  - actions/checkout@v4 → actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - astral-sh/setup-uv@v4 → astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@v4 → actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - actions/setup-python@v5 → actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065

- Permissions hardening:
  - .github/workflows/test.yml: added `permissions: contents: read`.
  - Other workflows already declare explicit permissions; left as-is because they perform writes (push docs/branches, update PRs).

- Guardrails:
  - Added `set -euo pipefail` to steps that run remote install scripts (`curl | bash`) and package setup in visual testing.

Risky Patterns Reviewed
- pull_request_target: not used.
- Overbroad permissions: kept only where workflows explicitly need `contents: write` / `pull-requests: write` for bot operations.
- Deprecated tooling:
  - `apt-key` usage remains in visual testing setup. Consider migrating to the signed repository keyring method when feasible. Left unchanged to avoid breaking existing runs.

Guidance
- If a pinned action needs an update, bump to a newer tag and re-pin to the new commit SHA.
- For any workflows that only read repository content, prefer `permissions: contents: read` at the workflow (or job) level.
- Avoid `curl | bash` where possible; when necessary, verify checksums or signatures from a trusted channel.

Operational Notes
- This audit is intended to be minimal and non-breaking. If any workflow fails due to pinning, update to the latest tag and re-pin the SHA.
