# Repository Security Audit Log

Date: 2025-08-30
Branch: audit/workflow-hardening

## Summary
- No secrets detected in working tree or 1-year commit history using common patterns (AWS keys, GitHub tokens, private keys, Slack tokens, generic key/secret/password literals).
- Hardened workflows recommended: pin GitHub Actions to commit SHAs, least-privilege permissions, replace deprecated apt-key usage.

## Findings
- Workflows found in `.github/workflows/`:
  - code-review.yml
  - fix-ci.yml
  - fix-conflicts.yml
  - improve-pr-description.yml
  - secrets-audit.yml
  - test.yml
  - translate-keys.yml
  - update-docs.yml
  - visual-testing.yml

### Risky patterns observed
- Unpinned actions in several workflows (actions/checkout, actions/setup-python, actions/upload-artifact, astral-sh/setup-uv).
- Test workflow missing a top-level permissions block (defaults to write in some contexts).
- Deprecated `apt-key` usage in `visual-testing.yml` when adding Google Chrome repository.

## Recommended minimal changes
- Pin actions to SHAs (example SHAs as of today):
  - actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
- Add least-privilege permissions, e.g., in `test.yml`:
  - `permissions: { contents: read }`
- Replace `apt-key` with `signed-by` flow for Google Chrome repo in `visual-testing.yml`.

## Next steps
- Apply the above edits on a dedicated branch and open a PR. If any workflow update is blocked by repository rules, apply only Markdown/log changes and open an issue for follow-up.

## Additional notes
- No `pull_request_target` usage detected.
- No deprecated `::set-output` commands found.
