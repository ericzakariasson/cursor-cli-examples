# Security Hardening Log

Date: 2025-08-18
Branch: audit

Summary
- Performed repository secrets exposure and workflow hardening audit.
- No hard-coded secrets detected in tracked files or common patterns.
- Found unpinned actions and one workflow missing explicit minimal permissions.

Recommended minimal fixes (not auto-applied due to workflow write restrictions on this token):
- Pin third-party actions to immutable SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4)
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5)
- Guard PR-triggered jobs that write or use secrets to avoid running on forks:
  - Add: `if: ${{ !github.event.pull_request.head.repo.fork }}` to PR jobs in `auto-translate-keys.yml`, `auto-update-docs.yml`, `auto-update-docs-split.yml`, and `auto-improve-pr-description.yml`.
- Ensure least-privilege permissions in CI:
  - In `test.yml`, add at job-level: `permissions: { contents: read }`.

Notes
- Pushes that modify `.github/workflows/*.yml` are blocked by the current token’s `workflows` permission. Maintainers can apply the above edits in a single PR.
- Consider adding `.gitleaks.toml` to maintain allowlists for future scans.
