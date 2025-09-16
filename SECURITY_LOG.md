# Repository Security Hardening Log

## 2025-09-14 (Branch: audit-hardening)

Summary
- Proposed scheduled workflow `docs/proposed-security-audit.yml` to run weekly and on-demand. Maintainers must move this file to `.github/workflows/security-audit.yml` due to GitHub App workflow creation restrictions.
- Suggested `step-security/harden-runner` (egress audit mode).
- All GitHub Actions pinned to full commit SHAs in the proposal.
- Least-privilege permissions defined in the proposal.
- Configured Gitleaks with redaction to reduce secret exposure in logs.

Findings
- No secrets detected in working tree or the last 365 days of commit history using heuristic patterns (AWS keys, GitHub tokens, Slack tokens, private keys, generic credential assignments).
- No existing workflows were present at that time; proposed one with safe defaults.
- Prior audit notes: avoid floating action tags; ensure `permissions:` blocks exist; avoid insecure installers (`apt-key`, curl without TLS flags).

Recommendations
- If using an organization account, add `GITLEAKS_LICENSE` as a repository secret for Gitleaks-Action.
- If false positives arise, add a `gitleaks.toml` allowlist at repo root and re-run.
- Review Gitleaks artifacts when the workflow runs; rotate any discovered secrets.
- Keep actions pinned and permissions minimal in future workflows. Avoid `pull_request_target` unless required and properly guarded.

---

## 2025-09-16 (Branch: audit-hardening)

Summary
- Scanned tracked files and last 180 days of git history for common secret patterns. No findings.
- Proposed workflow hardening changes (pin actions to SHAs, add fork guards, and least-privilege permissions). Note: pushing workflow file edits is restricted for GitHub Apps without `workflows` permission; maintainers should apply these hardening edits from a trusted environment or grant the required permission.
- Maintained persistent branch `audit-hardening` for audit artifacts.

Findings
- No secrets detected in working tree or last 180 days of history.
- Risky patterns detected:
  - Floating action tags (unpinned) in multiple workflows.
  - Use of deprecated `apt-key` in `visual-testing.yml` for Google Chrome install. This should be replaced with signed-by keyrings.

Recommendations
- Replace `apt-key` usage with the keyring approach:
  1) `curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /usr/share/keyrings/google-linux.gpg > /dev/null`
  2) `echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list`
  3) `sudo apt-get update && sudo apt-get install -y google-chrome-stable`
- Continue to avoid `pull_request_target` unless strictly needed and properly sandboxed.
- Consider adding a scheduled Gitleaks workflow gated to push/PR with redaction and an allowlist file if needed.

Compare
- To review these changes: compare `main...audit-hardening` and fast-follow with a PR if acceptable.
