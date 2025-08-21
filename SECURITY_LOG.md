# Security Hardening Audit

Date: 2025-08-21
Branch: audit-hardening-2025-08-21

Summary of proposed changes (documentation only in this push):
- Pin `actions/checkout@v4` to commit `08eba0b27e820071cde6df949e0beb9ba4906955` in all workflows.
- Pin `actions/setup-python@v5` to commit `a26af69be951a213d495a4c3e4e4022e16d87065` in `test.yml`.
- Replace `curl ... | bash` installer with a safer download-then-execute pattern using TLS and `set -euo pipefail`.
- Add minimal `permissions` to `test.yml` and ensure permission blocks exist where applicable.
- Add guards to prevent running PR jobs with write permissions on forks.

Note on permissions:
- This run's token lacks the `workflows` permission, so workflow file edits cannot be pushed by automation. The proposed workflow hardening is documented here and should be applied via a follow-up compare/PR.

Findings:
- Unpinned Actions: Present in workflows; propose pinning as above.
- Insecure command usage: Pipe-to-shell (`curl | bash`) detected; propose safer pattern.
- Forked PR context risks: Propose guards to avoid secret exposure.
- No high-confidence secrets found in tracked files; limited recent history sampled.
