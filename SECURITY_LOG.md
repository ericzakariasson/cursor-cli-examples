# Security Hardening Log

Date: 2025-10-13
Branch: audit

Summary
- Reviewed repository and last 180 days of history for common secret patterns; no findings.
- Proposed workflow hardening (pins and fork guards). Workflow edits were not pushed because this automation lacks the repository "workflows" permission. The concrete recommendations are listed below for maintainers to apply via a regular PR.

Proposed workflow updates (not yet committed)
1) Pin actions to SHAs
- actions/checkout@v4 -> actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955 (v4.3.0)
- actions/setup-python@v5 -> actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 (v5.6.0)
- actions/upload-artifact@v4 -> actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 (v4.6.2)
- astral-sh/setup-uv@v4 -> astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a (v4.2.0)

2) Guard PR-triggered jobs against forked contexts (secrets are not available on forks)
- Add to `visual-testing.yml`, `translate-keys.yml`, `update-docs.yml`, and `code-review.yml`:
  if: github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false

3) Modernize apt key usage
- In `visual-testing.yml`, replace deprecated `apt-key` with signed-by keyring for Chrome.

Secrets scanning
- Checked tracked files and recent history for AWS keys, GitHub fine-grained tokens, generic private keys, and common key/password literals; no matches found.
- If a `.gitleaks.toml` is added, future scans will honor its allowlist.

Maintenance guidance
- Continue pinning new actions to immutable SHAs; review pins quarterly.
- Prefer least-privilege `permissions:` at workflow/job level; grant write only when necessary.
- Avoid `curl | bash` installers; prefer checksums/signatures and pinned versions.

Change attribution
- Automated scheduled audit.
