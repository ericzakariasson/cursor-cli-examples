# Security Hardening Log

Date: 2025-09-17
Branch: audit-hardening

Summary of proposed changes (not applied due to permissions)
- Pin GitHub Actions to immutable commit SHAs:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - Replace manual Chrome install with pinned `browser-actions/setup-chrome@c785b87e244131f27c9f19c1a33e2ead956ab7ce`
- Add explicit least-privilege permissions to workflows (e.g., `permissions: contents: read`).
- Add `if:` guards to steps that use `secrets.*` to avoid exposure on forked PRs.

Findings
- No plaintext secrets found in tracked files.
- No high-confidence secrets found in the last 50 commits (limited in-runner tooling).

Actions needed by maintainers
- Grant `workflows: write` permission to the bot token or manually apply the above edits in `.github/workflows/*.yml`.
- Optionally add `.gitleaks.toml` and a CI job to run Gitleaks for deeper scanning.

Compare link to propose PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening
