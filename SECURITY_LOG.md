# Security Hardening Log

Date: 2025-11-06
Branch: `audit/hardening`

## Summary
- No secrets detected in tracked files or recent history (last 100 commits scanned).
- Pinned GitHub Actions to immutable commit SHAs.
- Added least-privilege `permissions` where missing.
- Added guardrails to skip secret-using jobs for forked PRs.

## Changes
- Pinned actions:
  - `actions/checkout@v4` ? `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4.3.0)
  - `actions/setup-python@v5` ? `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5.6.0)
  - `actions/upload-artifact@v4` ? `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4.6.2)
  - `astral-sh/setup-uv@v4` ? `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4.2.0)

- Permissions:
  - `.github/workflows/test.yml`: added `permissions: contents: read`.

- Forked PR guardrails (skip when secrets unavailable):
  - `.github/workflows/visual-testing.yml`
  - `.github/workflows/code-review.yml`
  - `.github/workflows/translate-keys.yml`
  - `.github/workflows/update-docs.yml`

- Scheduled audit workflow:
  - `.github/workflows/secrets-audit.yml` already present; ensured action pinning and explicit permissions.

## Findings and Guidance
- Secrets scan: No potential secrets found in tracked files or recent history. If you intentionally commit test tokens or keys, consider adding a `.gitleaks.toml` allowlist.
- Unpinned actions: All workflow `uses:` are now pinned to SHAs to prevent supply-chain drift.
- Overbroad permissions: Default token now explicitly scoped in `test.yml`; other workflows retain only required write scopes for their tasks.
- Forked PRs: Workflows that use repository secrets now skip for forks to avoid failing runs and potential risk if triggers change.
- Deprecated commands: `apt-key add` is deprecated in `visual-testing.yml`. Consider switching to `signed-by` keyring usage for APT sources.

## Next Steps (optional)
- Add `.gitleaks.toml` to tune allowlists if you expect false positives.
- Periodically refresh action SHAs to latest patch releases.
- Consider adding `step-security/harden-runner` for network egress restrictions, pinned by SHA.
