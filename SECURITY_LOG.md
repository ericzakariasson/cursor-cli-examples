# Security Hardening Log

Date: 2025-11-09

Scope: Repository-wide secrets exposure scan and GitHub Actions workflow hardening.

Summary of changes
- Pinned GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 → 08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@v4 → 38f3f104447c67c051c4a08e39b64a148898af3a
- Added minimal permissions to `.github/workflows/test.yml` (`permissions: contents: read`).

Findings
- No potential secrets found in tracked files (basic patterns: AWS keys, private keys, GitHub tokens).
- No potential secrets found in recent git history (last 200 commits) for the same patterns.
- No usage of `pull_request_target` or deprecated `::set-output` detected.

Recommendations & guidance
- Keep actions pinned to SHAs; update pins only after verifying upstream changes.
- Ensure each workflow declares the least-privileged `permissions:` needed. Prefer `contents: read` unless writes or PR comments are required.
- If you use an allowlist for secret scanning, commit a `.gitleaks.toml` with approved patterns/paths. Scheduled audits can read and honor allowlists.
- Avoid using repository secrets in forked PR contexts. Prefer `pull_request` (not `pull_request_target`) for untrusted contributions, and gate sensitive steps with conditions.

Maintenance
- A scheduled audit workflow is present (`.github/workflows/secrets-audit.yml`) and will continue scanning on a schedule. Review logs and rotate any secrets if newly reported.
