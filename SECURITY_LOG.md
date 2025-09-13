# Security Audit Log

Date: 2025-09-13
Branch: audit-hardening

Summary of findings
- No high-signal secrets found in tracked files or last 200 commits.
- Workflows use floating action tags; recommend pinning to SHAs.
- One workflow lacked explicit least-privilege `permissions`; recommend adding `contents: read`.
- Insecure installer patterns found (`apt-key`, plain curl without TLS flags); recommend safer equivalents.
- No `pull_request_target` usage detected.
- No `.gitleaks.toml` found (allowlist not configured).

Proposed minimal hardening
- Pin actions: `actions/checkout@<sha>`, `actions/setup-python@<sha>`, `astral-sh/setup-uv@<sha>`, `actions/upload-artifact@<sha>`.
- Add `permissions:` blocks where missing; prefer `contents: read` on CI jobs that only read.
- Harden installers: `curl --proto '=https' --tlsv1.2 -fsS URL | bash`; replace `apt-key` with keyring + signed-by.

Notes
- Pushing workflow file edits was skipped due to missing `workflows: write` permission for this run. Apply the above edits manually or re-run with that permission.

Compare link to review this branch:
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening
