# Security Hardening Log

Date: 2025-09-06 (UTC)

Summary of proposed minimal changes to improve security posture (not pushed due to workflow permissions):

- Pin reusable GitHub Actions to immutable commit SHAs:
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02

- Add fork-PR guards to workflows that post comments or mutate repo state:
  - Gate on `github.event.pull_request.head.repo.fork == false` for code-review, visual-testing, translate-keys, and update-docs.

- Add/adjust least-privilege permissions:
  - `test.yml`: add top-level `permissions: contents: read`.
  - `visual-testing.yml`: explicitly set `id-token: none`.

- Replace deprecated/insecure `apt-key` usage with signed-by keyring method for Chrome install.

Secrets exposure scan results:
- Repository files: no high-confidence secrets detected.
- Recent history (last 200 commits): no high-confidence secrets detected.
- No `.gitleaks.toml` allowlist found; consider adding one if needed.

Next steps for maintainers:
- Grant `workflows: write` permission to the automation account or manually apply the above workflow edits via a PR.
- Optionally add `.gitleaks.toml` to tune allowlists.
- After changes, re-run the scheduled audit to validate.
