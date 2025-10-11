# Security Hardening Log

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
