# Security Hardening Log

Date: 2025-09-05

Summary of audit:
- No secrets detected in tracked files or recent history (last 180 days).
- Proposed workflow hardening:
  - Pin actions to immutable SHAs (checkout, upload-artifact, setup-uv).
  - Add fork-PR guards to any steps using `GH_TOKEN` or pushing branches.
  - Replace deprecated `apt-key` with apt keyring usage for Chrome install.
- All workflows already declare explicit `permissions`; no `pull_request_target` or `::set-output` usage detected.

Proposed edits (not applied by this job):
- actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
- actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
- astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
- Add `if: ${{ !github.event.pull_request.head.repo.fork }}` to GH_TOKEN-using steps.
- Replace apt-key with keyring-based apt source for Chrome.

Next steps:
- Review and apply via compare: https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit/workflow-hardening
