# Security Hardening Log

Date: 2025-09-23
Branch: audit/workflow-hardening

Summary of changes:
- Pin GitHub Actions to commit SHAs for supply-chain safety:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
- Added default least-privilege permissions in `test.yml`.
- Guarded PR-triggered workflows from running on forks where they would have write permissions:
  - `translate-keys.yml`, `update-docs.yml`, `code-review.yml`, `visual-testing.yml` now skip when PR head repo is a fork.
- Replaced deprecated `apt-key` usage in `visual-testing.yml` with signed-by keyring.

Secret scanning:
- No potential secrets detected in tracked files or last 100 commits using heuristic patterns.
- No `.gitleaks.toml` present; consider adding one if you maintain allowlists/false-positive rules.

Recommendations:
- Consider adding a repository-level `permissions: read-all` default via org/repo settings and granting per-job writes only when needed.
- Periodically validate pinned SHAs and update to latest stable versions.
