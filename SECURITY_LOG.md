# Security Hardening Audit (automated)

Date: 2025-10-03
Branch: audit/hardening

## Summary of proposed changes
- Pin actions to immutable SHAs (checkout, setup-python, upload-artifact, setup-uv).
- Add fork PR guardrails to avoid secret exposure in PR contexts.
- Declare least-privilege permissions where missing (e.g., contents: read in tests).
- Replace deprecated apt-key with signed APT source for Chrome.

Note: Workflow file updates could not be pushed by this automation due to repository permissions on workflow edits. See compare link in the PR comment below to quick-create a PR from this branch, or apply the same changes directly.

## Secret exposure review
- Scanned tracked files and recent history for common secret patterns (PATs, AWS keys, PEMs, JWTs): no findings.
- No `.gitleaks.toml` found; consider adding one to centralize allowlists if needed.

## Pinned SHAs (for reference)
- actions/checkout@v4 → 08eba0b27e820071cde6df949e0beb9ba4906955
- actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
- actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
- astral-sh/setup-uv@v4 → 38f3f104447c67c051c4a08e39b64a148898af3a

## Guidance / next steps
- Rotate any secrets if ever committed; add targeted allowlist patterns only when necessary.
- Keep actions pinned; update pins with Dependabot or a scheduled job after reviewing releases.
- Maintain least‑privilege workflow permissions; avoid write scopes unless required.
