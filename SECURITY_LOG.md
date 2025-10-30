# Security Hardening Log

Date: 2025-10-30
Branch: `audit/security-hardening`

Summary of changes proposed:
- Pin reusable GitHub Actions to immutable commit SHAs with inline version comments:
  - `actions/checkout@v4`
  - `actions/setup-python@v5`
  - `actions/upload-artifact@v4`
  - `astral-sh/setup-uv@v4`
- Add minimal guardrails to risky shell steps:
  - Prepend `set -euo pipefail` and enforce TLS on install scripts (`curl --proto '=https' --tlsv1.2 -fsS ... | bash`).
  - Replace deprecated `apt-key` usage with keyring-based `signed-by` install for Google Chrome.
- Reduce exposure of secrets in forked PR contexts:
  - Add `if: ${{ github.event.pull_request.head.repo.fork == false }}` to steps that require `secrets.CURSOR_API_KEY` on `pull_request` workflows.

Findings (secrets exposure scan):
- No potential secrets detected in tracked files.
- No potential secrets detected in the last 100 commits' diffs.
- No `.gitleaks.toml` allowlist present.

Workflow notes:
- Permissions blocks are present across workflows and appear appropriately scoped for their functions. No `pull_request_target` usage found.
- `GH_TOKEN` is used in contexts that require repository write/commenting; guard secret-using steps for forks on `pull_request` events.

Remediation guidance:
- Prefer pinning all third-party actions to exact SHAs. Update SHAs deliberately during dependency refreshes.
- Avoid piping remote scripts directly to shells when possible; if necessary, enforce HTTPS/TLS, pin versions, and verify checksums.
- Continue to use minimal `permissions:` for each workflow; only grant `write` where strictly required.

Maintenance:
- When updating action versions (e.g., `v4` ? `v5`), update the pinned SHA accordingly.
- Re-run the scheduled audit to catch drift and new risks.
