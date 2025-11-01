# Security Hardening Audit

Date: 2025-11-01
Branch: audit/workflow-hardening

## Summary
- No secrets detected in the working tree or recent history (last 1 year, common patterns).
- Hardened GitHub Actions by pinning actions to immutable SHAs, adding minimal permissions, and guarding secret-using steps from running on forked PRs.

## Changes
- Pinned actions to commit SHAs with version comments:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 # v4
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a # v4
- Added workflow-level minimal permissions:
  - .github/workflows/test.yml ? permissions: contents: read
- Added fork-safety guards to steps that consume secrets or write to PRs:
  - visual-testing.yml ? guard the Cursor Agent step
  - code-review.yml ? guard the code review step
  - translate-keys.yml ? guard the i18n update step
  - update-docs.yml ? guard the docs update step

## Recommendations
- Avoid using deprecated apt-key; migrate to keyrings with signed-by.
- Keep actions pinned; periodically refresh SHAs to the latest secure tags.
- For any future workflows using pull_request events with secrets or write scopes, apply the same fork guard: `if: ${{ github.event.pull_request.head.repo.fork == false }}`.
- If introducing secret scans, consider adding a repository-wide allowlist (e.g., .gitleaks.toml) for expected patterns to reduce false positives.
