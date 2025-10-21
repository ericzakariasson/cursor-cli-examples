# Security Hardening Log

Date: 2025-10-21
Branch: audit

Summary of changes:
- Pinned actions to immutable SHAs: `actions/checkout`, `actions/setup-python`, `actions/upload-artifact`, `astral-sh/setup-uv`.
- Added/normalized permissions blocks to least privilege (primarily `contents: read`; kept `pull-requests: write` where commenting is required).
- Maintained scheduled audit workflow with safer defaults.

Findings:
- No high-signal secrets detected in working tree via regex scan. Consider running gitleaks for comprehensive coverage and add an allowlist (`.gitleaks.toml`) if needed.
- No `pull_request_target` usage detected. No deprecated `::set-env`/`::add-path` found.

Remediation guidance:
- Keep using pinned SHAs; update them periodically.
- Limit default `permissions` at the workflow top-level and elevate per job only when necessary.
- Avoid exposing secrets on forked PRs; prefer token scopes and repo/PR write only where needed.
