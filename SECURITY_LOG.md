# Security Audit Log

Date: 2025-11-17
Branch: \

## Summary
- No plaintext secrets detected in tracked files or last 50 commits.
- Recommended: Pin reusable Actions to immutable commit SHAs.
- Recommended: Add explicit minimal permissions to CI test workflow.
- Recommended: Guard secret-using steps from running on forked pull requests.

Note: Applying workflow file changes requires \ permission for the token pushing changes.

## Proposed Changes

### Workflow pinning (replace tags with SHAs)
- actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4)
- actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5)
- actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (v4)
- astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (v4)

Affected workflows:
- .github/workflows/visual-testing.yml
- .github/workflows/code-review.yml
- .github/workflows/fix-ci.yml
- .github/workflows/translate-keys.yml
- .github/workflows/fix-conflicts.yml
- .github/workflows/improve-pr-description.yml
- .github/workflows/update-docs.yml
- .github/workflows/secrets-audit.yml
- .github/workflows/test.yml

### Permissions tightening
- .github/workflows/test.yml: add \.

### Fork PR guardrails
Add \ to secret-using steps:
- Visual Testing: "Run visual testing with Cursor Agent"
- Code Review: "Perform automated code review"
- Translate Keys: "Propose i18n updates"
- Update Docs: "Update docs"

## Secret scan
- Checked tracked files and recent history (last 50 commits) for common token patterns (AWS keys, GitHub PATs, Slack webhooks, private keys). No findings.
- No .gitleaks.toml allowlist present.

## Recommendations
- Keep Actions pinned; update SHAs intentionally during dependency refreshes.
- Prefer least-privilege permissions per workflow; add explicit blocks for new workflows.
- Avoid exposing repository secrets to jobs that can run on forked PRs; keep fork guards in place.
