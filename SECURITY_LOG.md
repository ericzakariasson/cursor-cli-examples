Date: 2025-08-17

Summary of automated workflow hardening (proposed)

Proposed changes (not pushed due to missing `workflows` permission on token):

- Pin reusable actions to immutable SHAs:
  - Replace `actions/checkout@v4` with `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` in all workflows.
  - Replace `actions/setup-python@v5` with `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` in `test.yml`.
- Add least-privileged `permissions:
  contents: read` to `test.yml`.
- Add fork-PR safety guards to PR-triggered jobs to avoid using elevated permissions on contributions from forks:
  - `auto-improve-pr-description.yml`, `auto-update-docs.yml`, `auto-update-docs-split.yml`, `auto-translate-keys.yml` add `if: ${{ !github.event.pull_request.head.repo.fork }}`.

Observations

- All workflows already declare explicit permissions; no `pull_request_target` usage found.
- No potential secrets detected in tracked files for common patterns; consider adding `.gitleaks.toml` for allowlists and enabling scanning in CI.

Next steps

- Approve these changes or run the audit with a token that has `workflows` permission to allow automatic updates.
