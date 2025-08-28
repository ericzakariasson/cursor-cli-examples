# Security Hardening Log

Date: 2025-08-28
Branch: `audit-workflows`

Summary of changes:
- Pinned GitHub Actions to commit SHAs for reproducibility and supply-chain safety.
- Added/normalized least-privilege `permissions` blocks; ensured `contents: read` where appropriate.
- Set `persist-credentials: false` for checkout in jobs that do not push.
- Added fork-PR guardrails to PR-triggered workflows to avoid secret exposure.
- Replaced deprecated `apt-key` in Chrome install with signed-by keyring method.

Details:
- `.github/workflows/test.yml`: pin `actions/checkout` and `actions/setup-python`; add `permissions: contents: read`; set `persist-credentials: false`.
- `.github/workflows/code-review.yml`: pin `actions/checkout` and `astral-sh/setup-uv`; add fork guard; set `persist-credentials: false`.
- `.github/workflows/visual-testing.yml`: pin `actions/checkout`, `astral-sh/setup-uv`, and `actions/upload-artifact`; add fork guard; set `persist-credentials: false`; modernize Chrome apt install.
- `.github/workflows/fix-ci.yml`: pin `actions/checkout`; set `persist-credentials: false`.
- `.github/workflows/fix-conflicts.yml`: pin `actions/checkout`; set `persist-credentials: false`.
- `.github/workflows/improve-pr-description.yml`: pin `actions/checkout`; add fork guard; set `persist-credentials: false`.
- `.github/workflows/update-docs.yml`: pin `actions/checkout`; set `persist-credentials: false`.
- `.github/workflows/translate-keys.yml`: pin `actions/checkout`; set `persist-credentials: false`.
- `.github/workflows/secrets-audit.yml`: pin `actions/checkout`; fixed minor indentation and spacing.

Secret exposure scan:
- Scanned tracked files and recent history for AWS keys, GitHub tokens, private keys, and common credential patterns; no hits found.

Remediation guidance:
- For any workflows needing write access, explicitly set minimal required permissions per job.
- Prefer pinning all third-party actions to immutable SHAs and periodically refresh pins.
- Avoid using `pull_request_target` unless strictly necessary and safeguard with `if: github.event.pull_request.head.repo.fork == false`.
- Keep secrets usage restricted to trusted contexts and avoid exposing them in logs.
