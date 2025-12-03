# Security Hardening Log

Date: 2025-12-03
Branch: audit-gha-hardening

Summary of changes:
- Pinned GitHub Actions to immutable commit SHAs:
  - actions/checkout@v4 → 34e114876b0b11c390a56381ad16ebd13914f8d5
  - actions/upload-artifact@v4 → ea165f8d65b6e75b540449e92b4886f43607fa02
  - actions/setup-python@v5 → a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@v4 → 38f3f104447c67c051c4a08e39b64a148898af3a
- Added minimal top-level permissions to `test.yml` (`contents: read`).
- Added fork-safety guards to PR workflows that use secrets or write to PRs:
  - `code-review.yml`, `visual-testing.yml`, `translate-keys.yml`, `update-docs.yml`
    - Guard: `github.event.pull_request.head.repo.fork == false`

Secret exposure scan:
- No obvious secrets found in tracked files.
- No candidate secrets found in recent git history for common patterns (AWS keys, GitHub tokens, private keys, Slack tokens).
- No `.gitleaks.toml` allowlist detected.

Remediation guidance:
- Continue to pin actions to SHAs for any new workflows.
- Keep `permissions:` minimally scoped; prefer `contents: read` unless writes are required.
- Avoid using `pull_request_target` unless strictly necessary; when used, gate execution and avoid running untrusted code.
- If secrets must be used in PR contexts, ensure jobs are guarded against forked contributions.

Compare link to propose PR:
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-gha-hardening
