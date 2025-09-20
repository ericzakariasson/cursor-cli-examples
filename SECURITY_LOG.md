# Security Hardening Log

Date: 2025-09-20

Scope: Automated secrets exposure scan and GitHub Actions workflow hardening.

Findings:
- No plaintext secrets detected in working tree. History scan skipped (rg unavailable).
- Unpinned actions in multiple workflows; deprecated apt-key; missing fork guards for PR jobs; missing minimal permissions in CI.

Applied edits in `audit-workflow-hardening`:
- Pin actions to SHAs:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4)
- Add fork guards to PR-triggered jobs to avoid forked-context secrets usage.
- Add least-privilege `permissions: { contents: read }` to `test.yml`.
- Replace deprecated `apt-key` with keyring-based installation for Google Chrome.

Compare: https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-workflow-hardening
