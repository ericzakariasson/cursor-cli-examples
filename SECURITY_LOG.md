# Security Hardening Log

Date: 2025-12-01
Branch: audit

Summary of changes:
- Pinned GitHub Actions to immutable commit SHAs for supply-chain safety:
  - actions/checkout (v4.3.1)
  - actions/setup-python (v5.6.0)
  - actions/upload-artifact (v4.6.2)
  - astral-sh/setup-uv (v4.2.0)
- Added minimal token permissions to CI where missing:
  - `.github/workflows/test.yml`: `permissions: contents: read`
- Added fork-safety guards to PR-triggered workflows to avoid secret access and spurious failures for forks:
  - `code-review.yml`, `translate-keys.yml`, `update-docs.yml`, `visual-testing.yml`
- Replaced deprecated `apt-key` usage with signed keyring approach when installing Google Chrome in `visual-testing.yml`.

Secrets exposure scan:
- Working tree: no high-confidence secrets detected with patterns (AWS/GitHub/Slack/API keys, private keys, common tokens).
- Recent history (last 50 commits): no matches found.
- No `.gitleaks.toml` present; consider adding one if you maintain explicit allowlists.

Recommended follow-ups:
- Adopt organization-wide policy to pin third-party actions to SHAs.
- Review and minimize permissions in writer workflows; grant only when a step actually needs it.
- Consider adding a `.gitleaks.toml` to codify allowlists/ignores.
- Periodically re-pin action SHAs to the latest secure patch versions.

Note:
- The token in this context lacks the `workflows` scope, so updates to files under `.github/workflows/` could not be pushed. Hardened workflow files have been saved under `.audit/proposed-workflows/` for maintainers to review and apply. Once permissions allow, copying those files back into `.github/workflows/` will enable the hardening changes.
