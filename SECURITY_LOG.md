# Security Audit Log

Date: 2025-10-29
Branch: audit-hardening

Summary
- No candidate secrets found in tracked files or the last 50 commits (patterns checked: AWS AKIA, ghp_ tokens, PEM private keys, inline password literals).
- Proposed GitHub Actions workflow hardening with minimal, safe changes. Some proposals require repository workflow permissions to apply.

Proposed workflow hardening (not applied due to workflow permission restrictions on this token)
- Add explicit least-privilege permissions where missing; for test-only workflows, set:
  - `permissions: { contents: read }`
- Skip PR jobs that need secrets/write on forks:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Replace deprecated `apt-key` usage with keyring-based installation (e.g., Google Chrome keyring under `/etc/apt/keyrings`).
- Pin third-party actions to immutable SHAs. Example pins to consider (verify latest upstream SHAs before applying):
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - `astral-sh/setup-uv@e4db8464a088ece1b920f60402e813ea4de65b8f`

Compare and create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening

Allowlist
- No `.gitleaks.toml` allowlist detected. If false positives arise in future scans, add a targeted allowlist with clear owner review.

Operational guidance
- Review and pin action SHAs, then enable Dependabot or a scheduled check to refresh pins regularly.
- Consider adding a periodic secret scan (e.g., gitleaks) in CI to block new exposures.

Attribution
- Automated hardening performed by a scheduled security audit task.