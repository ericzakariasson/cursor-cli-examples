# Security Hardening Log

Date: 2025-10-17
Branch: audit

Summary
- Reviewed tracked files and recent history for common secret patterns; no findings.
- Proposed workflow hardening (pins and fork guards). Workflow edits were not pushed because this automation lacks the repository "workflows" permission. Concrete recommendations are listed below for maintainers to apply via a regular PR.

Proposed workflow updates (not yet committed)
1) Pin actions to SHAs
- actions/checkout@v4 -> actions/checkout@44c2b7a8a4ea60a981eaca3cf939b5f4305c123b
- actions/setup-python@v5 -> actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
- actions/upload-artifact@v4 -> actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
- astral-sh/setup-uv@v4 -> astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a

2) Guard PR-triggered jobs against forked contexts (secrets are not available on forks)
- Add to `visual-testing.yml`, `translate-keys.yml`, `update-docs.yml`, and `code-review.yml`:
  if: ${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.full_name == github.repository }}

3) Modernize apt key usage
- In `visual-testing.yml`, replace deprecated `apt-key` with signed-by keyring for Chrome.

4) Least-privilege permissions
- Add job-level permissions where missing, e.g. in `test.yml`:
  permissions:
    contents: read

Secrets scanning
- Checked tracked files and recent history for AWS keys, GitHub tokens, private keys, and common literals; no matches found.
- If a `.gitleaks.toml` is added, future scans will honor its allowlist.

Maintenance guidance
- Continue pinning new actions to immutable SHAs; review pins quarterly.
- Prefer least-privilege `permissions:` at workflow/job level; grant write only when necessary.
- Avoid `curl | bash` installers; prefer checksums/signatures and pinned versions.
- Avoid `pull_request_target` unless strictly necessary and fully guarded.

Change attribution
- Automated scheduled audit.