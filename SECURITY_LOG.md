# Security Audit Log

Date: 2025-09-30
Repository: ericzakariasson/cursor-cli-examples
Audit branch: audit-hardening

## Scope
- Scanned tracked files for potential secrets (with support for allowlists like `.gitleaks.toml` if present).
- Scanned the last 90 days of commit diffs for common secret patterns.
- Audited GitHub Actions workflows for risky patterns (unpinned actions, overbroad/missing permissions, `pull_request_target` misuse, secrets exposure on forked PRs, deprecated commands like `::set-output`, etc.).

## Findings
- Secrets in working tree: none detected by high-signal pattern checks.
- Secrets in recent history (90 days): none detected.

## Summary of proposed workflow hardening
- Pin GitHub Actions to immutable commit SHAs:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
- Add fork-guard conditions to steps that use repository secrets to avoid exposure on forked PRs.
- Add minimal `permissions` to `test.yml` job (`contents: read`).
- Replace deprecated `apt-key` with `signed-by` keyring pattern when installing Google Chrome.

## Recommendations (minimal, safe defaults)
- When adding or updating workflows:
  - Pin actions to immutable commit SHAs (not moving tags).
  - Add a top-level `permissions:` block; default to least privilege (often `contents: read`). Grant write only where required.
  - Avoid `pull_request_target` for untrusted code paths. Prefer `pull_request` and never expose secrets to untrusted code.
  - Replace deprecated commands (`::set-output`, `::add-path`) with supported alternatives.
  - Optionally add a repo-level `.gitleaks.toml` with allowlists for known test fixtures to reduce false positives.

## Notes
- Workflow edits could not be pushed by this run due to missing `workflows` permission on the token. The above are proposed changes for a follow-up PR.

## Quick link to open a PR
- Compare and create PR: https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening?expand=1
