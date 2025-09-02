# Security Hardening Log

This repository was audited for secrets exposure and workflow risks. Minimal, safe changes are proposed below to harden CI without disrupting behavior.

Proposed workflow changes
- Pin reusable GitHub Actions to immutable commit SHAs
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
- Add explicit, minimal `permissions:` (default read; remove `id-token` where unused)
- Add fork context guard to visual testing to avoid using secrets on forked PRs
- Replace deprecated `apt-key` with signed-by keyring method for Chrome install

Secret exposure scan
- No high-confidence secrets detected in tracked files or recent history.
- Consider adding `.gitleaks.toml` for allowlists if needed in the future.

Follow-up recommendations
- Rotate org/user tokens periodically; validate no long-lived tokens exist in repo history.
- Keep actions pinned; update SHAs periodically or when security advisories are published.
- Add branch protection and required reviews for workflows that write to the repo.

Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
