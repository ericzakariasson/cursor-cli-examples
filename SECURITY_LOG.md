# Security Hardening Log

Date: 2025-09-29
Branch: audit-security-hardening

Summary of proposed changes (not applied by bot due to workflow permission limits)
- Pin GitHub Actions to immutable commit SHAs for reproducibility
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
- Add step-security/harden-runner with `egress-policy: audit` to observe external network access
- Add minimal permissions blocks where missing (e.g., `contents: read` for CI-only)
- Add fork guards to steps that use secrets or write to PRs

Secret scan results
- No obvious credentials found in tracked files or recent history.
- No `.gitleaks*` allowlist found. Consider adding `.gitleaks.toml` if needed.

Note
- This runner cannot push workflow file edits without the `workflows` permission. Please apply the above changes via PR or grant the permission for automated updates.
