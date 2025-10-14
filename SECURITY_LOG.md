# Security Hardening Log

<<<<<<< HEAD
Date: 2025-10-11
Branch: `audit/security-hardening`

Summary of proposed changes (not applied due to workflow permissions):
- Pin GitHub Actions to immutable commit SHAs (`actions/checkout`, `actions/setup-python`, `actions/upload-artifact`, `astral-sh/setup-uv`).
- Add minimal `permissions: contents: read` to workflows missing a top-level block and scope per-job permissions where write is required.
- Guard Cursor-dependent steps with `if: ${{ secrets.CURSOR_API_KEY != '' }}` to avoid failures/exposure on forks.
- Replace deprecated `apt-key` usage with signed-by keyring flow for Chrome installation.

Rationale:
- Pinning actions mitigates supply-chain risk from tag retargeting.
- Restrictive permissions follow the principle of least privilege.
- Guarding secrets prevents accidental usage in forked PR contexts.
- Removing `apt-key` avoids insecure, deprecated key management.

Recommendations:
- Consider adding `.gitleaks.toml` if you use custom secrets/allowlists; run gitleaks in CI.
- Periodically review repository variables/secrets and workflow permissions.
- Prefer the `pull_request` trigger for untrusted contributions; avoid `pull_request_target` unless strictly necessary with strong safeguards.

Note: Workflow file edits were not pushed because this job lacks the `workflows` permission required by repository rules. You can approve these changes via a PR from this branch.
=======
Date: 2025-10-14
Branch: audit/hardening

Summary of changes:
- Pinned GitHub Actions to immutable commit SHAs for supply-chain safety:
  - actions/checkout@v4 -> 08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/upload-artifact@v4 -> ea165f8d65b6e75b540449e92b4886f43607fa02
  - actions/setup-python@v5 -> a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@v4 -> e4db8464a088ece1b920f60402e813ea4de65b8f
- Added fork-safety guards to PR-triggered jobs that use secrets (skip when PR comes from fork).
- Replaced deprecated `apt-key` usage with keyring-based apt repo setup for Google Chrome.

Risk patterns reviewed:
- Missing or overbroad permissions: existing workflows define permissions; left unchanged if already minimal.
- pull_request_target: not used.
- Secrets in forked PRs: guarded where steps use secrets.
- Deprecated commands: `apt-key` replaced.

Next steps:
- Consider further reducing workflow permissions to least privilege per job where safe.
- Periodically re-run this audit to keep pins current.
>>>>>>> 6b5abb1 (security: add SECURITY_LOG.md with hardening summary and guidance)
