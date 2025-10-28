# Security Hardening Log

Date: 2025-10-28
Branch: audit-hardening

Summary of audit
- No candidate secrets found in tracked files or the last 90 days of history (patterns checked: AWS AKIA, ghp_ tokens, PEM private keys, inline password literals).
- Multiple workflows reference floating action versions; propose pinning to immutable SHAs.
- Recommend avoiding privileged jobs on forked PRs.

Proposed workflow hardening (not committed due to missing `workflows` permission on this token):
- Pin actions to SHAs:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - `astral-sh/setup-uv@e4db8464a088ece1b920f60402e813ea4de65b8f`
- Add fork-safety guards to jobs that use repo write access:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Ensure explicit least-privilege `permissions:` blocks exist; for test-only workflows: `permissions: { contents: read }`

Compare and create PR:
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening
