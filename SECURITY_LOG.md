# Security Audit Log

This file records the scheduled secrets exposure scan and workflow hardening actions performed by the audit job.

Date: 2025-09-26
Branch: audit/hardening

Findings
- No high-confidence secrets detected in tracked files or last 200 commits based on common token and key patterns. Continue to treat results as advisory; false negatives are possible.
- Several workflows used unpinned action versions and lacked least-privilege permissions or fork guards around steps that use repository secrets.

Changes (proposed)
- Pin Actions to immutable SHAs:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4.3.0)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5.6.0)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4.6.2)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4.2.0)
- Add least-privilege `permissions:` where missing (e.g., `contents: read` in `test.yml`).
- Add fork guards to steps consuming secrets in PR-triggered workflows:
  - Wrap Cursor CLI installation and runs with `if: !github.event.pull_request.head.repo.fork`.
- Replace deprecated `apt-key` with keyring-based `gpg --dearmor` flow for Chrome install.

Application note
- Directly updating workflow files requires the `workflows` permission. This audit run could not push those edits. A unified diff with the proposed changes is attached at `.security/audit-2025-09-26.patch`.
- To apply: review the patch and cherry-pick edits, or run: `git apply .security/audit-2025-09-26.patch`.

Guidance
- If using additional actions, pin them to a commit SHA.
- Avoid using `pull_request_target` unless absolutely necessary; never checkout untrusted code with elevated permissions.
- Keep permissions minimal at both workflow and job level. Only escalate for the specific step that needs it.
- Rotate any credentials if you later discover exposure. Consider enabling push-protection and secret scanning in repository settings.
