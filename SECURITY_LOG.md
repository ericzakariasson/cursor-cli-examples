# Security Hardening Audit (2025-11-07)

Note: Workflow file updates require elevated `workflow` permission to push from automation; proposed workflow edits are documented below and should be applied by a maintainer.

## Summary of Proposed Changes
- Pin GitHub Actions to immutable commit SHAs
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4.3.0)
  - `actions/setup-python@v5` → `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5.6.0)
  - `actions/upload-artifact@v4` → `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4.6.2)
  - `astral-sh/setup-uv@v4` → `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4.2.0)
- Add least-privilege permissions block where missing
  - `.github/workflows/test.yml`: `permissions: contents: read`
- Replace deprecated `apt-key` usage with a signed-by keyring for Chrome install
  - `.github/workflows/visual-testing.yml`
- Add guardrails to steps requiring repository secrets
  - Add `if: ${{ secrets.CURSOR_API_KEY != '' }}` to steps that use `secrets.CURSOR_API_KEY` so forked PRs do not fail and secrets are never assumed present

## What We Checked
- Secrets in tracked files and recent history: none detected
- Risky workflow patterns: unpinned actions (proposed fix), missing permissions (proposed fix), unsafe `apt-key` (proposed fix), `pull_request_target` usage (none found), secrets on forks (guarded via proposal)

## Guidance
- Keep actions pinned to SHAs; update periodically by bumping to the latest release SHA
- Prefer adding explicit `permissions:` blocks to all workflows; start with `contents: read` and elevate per-need
- Avoid `pull_request_target` unless strictly necessary and gated
- Continue to avoid checking secrets into history; consider adopting `gitleaks` pre-commit/hooks for continuous scanning

Audit branch: `audit/hardening-2025-11-07`.
