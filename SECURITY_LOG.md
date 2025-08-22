Security hardening audit summary

Date: 2025-08-22

Proposed changes (not applied due to workflow permission restrictions on this token)

- Pin actions to immutable SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (was @v4)
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (was @v5)
- Add least-privilege `permissions` to `.github/workflows/test.yml`:
  - permissions:
    contents: read
- Add fork safety to PR-triggered workflows that push or comment:
  - Add `if: github.event.pull_request.head.repo.fork == false` to publishing/commenting steps.

Findings

- No potential secrets detected in tracked files or recent history scan.
- No usage of `pull_request_target` detected.
- No deprecated `::set-output` commands found.

Remediation guidance

- Prefer least-privilege `permissions` per workflow/job. Expand only when required.
- Pin all third-party actions to specific commit SHAs and review periodically.
- Avoid using `pull_request_target`; if necessary, add strict label/actor checks and disable write tokens.
- Store sensitive values in repository or organization secrets; never commit plaintext tokens.
