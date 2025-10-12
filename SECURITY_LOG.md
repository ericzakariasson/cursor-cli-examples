# Security Hardening Log

Date: 2025-10-12

Summary of changes:
- Pinned GitHub Actions to immutable commit SHAs for supply-chain safety:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
- Added or tightened workflow permissions to least-privilege (read-only `contents` where write not required).
- Introduced explicit `permissions` block to `Test` workflow.

Findings:
- No secrets detected in tracked files or recent history (90 days) using common signatures (AWS, GitHub tokens, private keys). Consider adding `.gitleaks.toml` if custom allowlists are desired.
- No deprecated `::set-env`/`add-path` commands found.
- No use of `pull_request_target` detected.

Remediation guidance:
- Prefer SHA-pinned actions in all workflows and review pins quarterly.
- Keep `permissions` scoped minimal; grant `write` only when necessary per job.
- Avoid exposing repository or environment secrets to code executed from forks.
- Add `.gitleaks.toml` to codify allowlists if needed.
