Security Hardening Log

Date: 2025-09-11

Summary of proposed changes

- Pin GitHub Actions to immutable commit SHAs in workflows:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a

- Add or tighten permissions:
  - Add minimal `permissions: contents: read` to `test.yml`.
  - Ensure workflows that push branches retain `contents: write` and other least-privilege scopes.

- Guard secret-using steps on forked PRs:
  - Add conditional guards to steps that use `${{ secrets.* }}` in PR-triggered workflows.

- Replace deprecated apt-key usage in `visual-testing.yml` with a signed-by keyring.

Secret exposure audit

- Scanned tracked files and recent history for common secret patterns; no matches found in the last 200 commits.
- No `.gitleaks.toml` found. Consider adding one to codify allowlists and custom rules.

Notes

- Some workflow edits could not be pushed by the automation token due to repository workflow modification restrictions. The items above are proposed for review.

Remediation guidance

- Continue pinning all third-party actions to SHAs; review monthly.
- Prefer job-level `permissions` with least privilege; avoid repository-wide write unless necessary.
- Avoid using secrets on `pull_request` from forks. Use `pull_request_target` only with strict checkout of trusted refs and no write tokens.
- Consider enabling GitHub Advanced Security secret scanning and push protection.
