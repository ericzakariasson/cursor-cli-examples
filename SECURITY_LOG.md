# Security Hardening Log

## 2025-11-26

- No high-confidence secrets detected in tracked files or in the last 300 commits scanned.
- Proposed hardening captured under `.audit/proposed-workflows/` (non-disruptive):
  - Pin actions to commit SHAs:
    - `actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5`
    - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
    - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
    - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - Add explicit `permissions: contents: read` to `test.yml`.
  - Add fork guards to PR workflows that use secrets (`code-review`, `visual-testing`, `translate-keys`, `update-docs`) to skip on forks.
- Additional recommendations (not applied to avoid breaking changes):
  - Replace `curl | bash` installers with pinned, verified downloads and checksums.
  - Replace deprecated `apt-key add` in `visual-testing.yml` with a keyring + `signed-by=` approach.

Quick-create PR link (compare hardened branch to main):
`https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit`

## 2025-11-10

- No high-confidence secrets detected in tracked files or in the last 100 commits scanned.
- Proposed hardening: pin actions to commit SHAs and tighten default permissions.
- Added recommendation to skip write-capable jobs for forked PRs.

Proposed changes (require `workflows` permission to apply):
- Pin actions:
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
- Reduce default token scope in `test.yml` via `permissions: contents: read`.
- Add fork guards in `update-docs.yml` and `translate-keys.yml`.

Recommendations:
- Replace `curl | bash` installers with pinned, verified sources.
- Replace deprecated `apt-key add` in `visual-testing.yml` with `signed-by=` keyring approach.
- Consider adding a scheduled Gitleaks workflow and an allowlist as needed.

---

## 2025-10-24

Summary of findings and recommendations (no workflow changes pushed due to missing `workflows` permission for that run):

- Recommended pinning third-party actions to commit SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
- Recommended guardrails for PR workflows using secrets: `if: ${{ github.event.pull_request.head.repo.fork == false }}` to avoid exposing secrets to forks.
- Permissions appeared scoped; continue aiming for least privilege per job.
- No plaintext secrets found in working tree; no `.gitleaks.toml` present. Consider adding gitleaks with an allowlist for test keys.
