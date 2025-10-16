# Security Hardening Log

Date: 2025-10-16

This automated run audited repository secrets exposure and GitHub Actions workflow hardening. Minimal, safe improvements are proposed below. Note: pushing workflow-file edits requires the token to have the `workflows` permission; this run pushed a report branch and proposes exact changes to apply.

## Findings

- No high-confidence secrets detected in tracked files or recent history using common patterns (GitHub tokens, AWS keys, Slack tokens, private keys).
- Several workflows use version tags for actions and installer patterns that can be safer.

## Proposed minimal fixes

Apply the following edits:

- Pin reusable actions to immutable SHAs:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
- Replace `curl | bash` installers with: download to file, then execute.
- Replace deprecated `apt-key add` with signed keyring (`/etc/apt/keyrings/...gpg`) and `signed-by` source entry.
- Guard secret-using PR steps from running on forks (example):
  - `if: ${{ !github.event.pull_request.head.repo.fork }}`

Files to update:
- `.github/workflows/visual-testing.yml`: pin actions, safer installer, modern Chrome key install, add fork guard to the step that uses secrets.
- `.github/workflows/{fix-ci,translate-keys,fix-conflicts,improve-pr-description,update-docs,secrets-audit,code-review}.yml`: pin actions and safer installer.
- `.github/workflows/test.yml`: pin `checkout` and `setup-python`.

## Recommendations

- Keep least-privilege `permissions` at the workflow or job level and elevate only when needed.
- Verify downloaded installer checksums when available.
- Re-run this audit on a schedule to keep pins fresh.

---
This file is maintained by automated security hardening runs on branch `audit/hardening`.
