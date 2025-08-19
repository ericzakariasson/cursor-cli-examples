# Security Hardening Audit

Date: 2025-08-19
Branch: `audit/security-hardening`

Summary
- No potential secrets detected in tracked files; no risky workflow triggers like `pull_request_target` found.
- Proposed hardening: pin third‑party actions to SHAs, add minimal `permissions` to CI, and prefer safer installer flags.

Notes on repo rules
- Workflow file edits require elevated `workflows` permission, so they were not pushed. The proposed changes are documented here for review and can be merged via a compare/PR.

Recommended edits
- `.github/workflows/test.yml`: add `permissions: { contents: read }`; pin `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` and `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`.
- All other workflows using `actions/checkout`: pin to `08eba0b27e820071cde6df949e0beb9ba4906955`.
- Replace `curl https://cursor.com/install -fsS | bash` with `curl -fsSL https://cursor.com/install | bash`.

Operational guidance
- Avoid exposing secrets to jobs that run on forked PRs; scope permissions per job where possible.
- Keep this audit scheduled and re‑review pins periodically for updates.
