# Repository Security Hardening Log

Date: 2025-09-14
Branch: audit-hardening

## Summary
- Proposed scheduled workflow `docs/proposed-security-audit.yml` to run weekly and on-demand. Maintainers must move this file to `.github/workflows/security-audit.yml` due to GitHub App workflow creation restrictions.
- Harden runner suggestion via `step-security/harden-runner` (egress audit mode).
- All GitHub Actions pinned to full commit SHAs in the proposal.
- Least-privilege permissions defined in the proposal.
- Configured Gitleaks with redaction to reduce secret exposure in logs.

## Findings
- No secrets detected in working tree or the last 365 days of commit history using heuristic patterns (AWS keys, GitHub tokens, Slack tokens, private keys, generic credential assignments).
- No existing workflows were present; proposed one with safe defaults.
- Prior audit notes: avoid floating action tags; ensure `permissions:` blocks exist; avoid insecure installers (`apt-key`, curl without TLS flags).

## Recommendations
- If using an organization account, add `GITLEAKS_LICENSE` as a repository secret for Gitleaks-Action.
- If false positives arise, add a `gitleaks.toml` allowlist at repo root and re-run.
- Review Gitleaks artifacts when the workflow runs; rotate any discovered secrets.
- Keep actions pinned and permissions minimal in future workflows. Avoid `pull_request_target` unless required and properly guarded.

## Next steps
- Move `docs/proposed-security-audit.yml` to `.github/workflows/security-audit.yml` on a trusted machine/account.

## Compare
Create a pull request from `audit-hardening` to `main` to merge these changes after review.
