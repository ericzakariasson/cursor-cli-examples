# Security Hardening Log

## 2025-09-23 (audit/workflow-hardening)

- Pin GitHub Actions to commit SHAs for supply-chain safety:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
- Added default least-privilege permissions in `test.yml`.
- Guard PR-triggered workflows from running on forks where they would have write permissions (translate-keys, update-docs, code-review, visual-testing).
- Replaced deprecated `apt-key` usage in `visual-testing.yml` with signed-by keyring.

Secrets scan:
- No potential secrets detected in tracked files or last 100 commits using heuristic patterns.
- No `.gitleaks.toml` present; consider adding one if you maintain allowlists/false-positive rules.

Recommendations:
- Consider adding a repository-level `permissions: read-all` default via org/repo settings and granting per-job writes only when needed.
- Periodically validate pinned SHAs and update to latest stable versions.

## 2025-10-08 (audit/workflow-hardening)

- No high-confidence secrets detected in tracked files using heuristic patterns.
- Recommended edits unchanged: pin actions to SHAs, add fork guards for PR workflows using secrets, replace deprecated apt-key with keyrings, and add explicit least-privilege permissions where missing.
- No `.gitleaks.toml` allowlist present; consider adding if false positives arise.

## 2025-10-19 (audit/workflow-hardening)

- Proposed minimal hardening; workflows not modified in this branch due to token restrictions.
- Pin actions to SHAs (maintainers to apply in workflows):
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4.3.0)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5.6.0)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4.6.2)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4.2.0)
- Add minimal job-level permissions where missing (e.g., `contents: read` for CI-only jobs).
- Replace `apt-key` with keyring-based approach in `visual-testing.yml`.
- `pull_request_target` not detected; keep using `pull_request` for untrusted code.
- No obvious secrets found in tracked files; consider enabling Gitleaks with `.gitleaks.toml` for allowlists.

Next steps:
- Apply the above edits in workflows and open a PR. This branch contains only this log for review.
