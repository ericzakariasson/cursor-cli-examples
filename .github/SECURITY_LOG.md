Security hardening summary (automated)

Date: 2025-09-20
Branch: audit-workflow-hardening

Findings
- No plaintext secrets found in tracked files using pattern scans.
- Could not complete history scan due to missing ripgrep on runner; recommend enabling Gitleaks or Code Scanning for full history.
- Workflows reference unpinned actions and lack fork guards in PR contexts.
- Minimal permission missing in test workflow.

Proposed minimal edits
- Pin actions to immutable SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4)
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5)
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (v4)
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (v4)
- Add fork guard to PR-triggered jobs:
  - if: ${{ github.event.pull_request.head.repo.full_name == github.repository }}
- Add minimal permissions to CI:
  - test.yml: permissions: { contents: read }
- Replace apt-key with keyring-based approach for Chrome install.

Next steps
- Review and apply the above edits via a PR from this branch.
- Optionally add Gitleaks: gitleaks/gitleaks-action@ff98106e4c7b2bc287b24eaf42907196329070c7 (v2) as a scheduled job.
