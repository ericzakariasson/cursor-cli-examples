# Security Hardening Log

This repository was scanned; minimal hardening is proposed below.

Date: 2025-10-02
Branch: audit-security-hardening

## Summary of Proposed Actions
- Pin reusable GitHub Actions to immutable commit SHAs.
- Replace deprecated `apt-key` usage with signed-by keyring for Google Chrome repo.
- Convert `curl | bash` installer pattern to a download-then-execute flow.
- Add conditional guards to steps that rely on `secrets.CURSOR_API_KEY` to avoid secret exposure on forks.
- Add a `permissions: contents: read` block to the `Test` workflow.

Note: Pushing workflow file changes requires the `workflows: write` permission for the token. This run's token lacked that scope; the edits are documented here for maintainers to apply.

## Findings
- No plaintext secrets found in tracked files.
- No secret patterns detected in the last 300 commits' diffs.
- Several workflows use version tags (`@v4`, `@v5`) instead of SHAs.
- Some jobs use network installer patterns that can be hardened.

## Recommended Follow-ups
- Add a `.gitleaks.toml` for allowlists and org-wide rules.
- Review per-workflow `permissions:` and scope down further where possible (consider job-level `permissions`).
- Periodically re-pin action SHAs to latest secure release.

## Proposed Edits (apply manually if not already)
- `.github/workflows/visual-testing.yml`: pin actions, harden Chrome apt keyring, guard secret-dependent step, pin upload-artifact.
- `.github/workflows/code-review.yml`: pin actions, guard secret-dependent step.
- `.github/workflows/fix-ci.yml`: pin actions, guard secret-dependent step.
- `.github/workflows/translate-keys.yml`: pin actions, guard secret-dependent step.
- `.github/workflows/fix-conflicts.yml`: pin actions, guard secret-dependent step.
- `.github/workflows/improve-pr-description.yml`: pin actions, guard secret-dependent step.
- `.github/workflows/update-docs.yml`: pin actions, guard secret-dependent step.
- `.github/workflows/test.yml`: set `permissions: contents: read`, pin actions.
- `.github/workflows/secrets-audit.yml`: pin actions.
