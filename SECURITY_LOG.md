# Security Hardening Log

Date: 2025-10-13
Branch: audit

Summary of actions
- Pinned GitHub Actions to immutable SHAs to prevent supply-chain takeover.
- Added guardrails to PR-triggered workflows to skip on forks where secrets are unavailable.
- Modernized Chrome installation to remove deprecated `apt-key` usage.
- Reviewed repository and recent history for common secret patterns; no findings.

Details
1) Actions pinning
- actions/checkout@v4 -> actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4.3.0)
- actions/setup-python@v5 -> actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5.6.0)
- actions/upload-artifact@v4 -> actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (v4.6.2)
- astral-sh/setup-uv@v4 -> astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (v4.2.0)

2) Workflow guardrails
- `visual-testing.yml`, `translate-keys.yml`, `update-docs.yml`, and `code-review.yml` now skip on forked PRs to avoid leaking secrets.

3) Secrets scanning
- Searched tracked files and the last 180 days of history for AWS keys, GitHub tokens, generic private keys, and common key/password literals.
- No matches were found. If a `.gitleaks.toml` is added, scans will honor its allowlist.

Remediation guidance
- Continue pinning new actions to SHAs.
- Prefer least-privilege `permissions:` at workflow/job level; tighten further as feasible.
- Avoid shelling `curl | bash`; verify checksums or pin installer versions when possible.

Change attribution
- Automated audit run using scheduled hardening task.
