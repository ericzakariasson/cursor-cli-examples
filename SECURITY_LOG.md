# Security Hardening Audit

Date: 2025-11-15
Branch: `audit/workflow-hardening`

## Summary
- Proposed pinning of GitHub Actions to immutable commit SHAs.
- Proposed adding explicit least-privilege permissions to CI test workflow.
- Proposed fork-safety guards for workflows that use repository secrets.
- No potential secrets detected in tracked files or last 100 commits.

Note: Workflow file edits could not be pushed by this automation due to repository workflow permissions. The proposed edits are documented below for maintainers to apply or to grant `workflows` permission to this automation.

## Proposed changes

### Actions to pin to SHAs
- `.github/workflows/visual-testing.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `astral-sh/setup-uv@v4` → `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4)
  - `actions/upload-artifact@v4` → `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4)
- `.github/workflows/code-review.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `astral-sh/setup-uv@v4` → `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4)
- `.github/workflows/fix-ci.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
- `.github/workflows/translate-keys.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
- `.github/workflows/fix-conflicts.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
- `.github/workflows/improve-pr-description.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
- `.github/workflows/update-docs.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
- `.github/workflows/test.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `actions/setup-python@v5` → `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5)
- `.github/workflows/secrets-audit.yml`
  - `actions/checkout@v4` → `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)

### Permissions hardening
- `.github/workflows/test.yml`: add top-level `permissions:`
  ```yaml
  permissions:
    contents: read
  ```

### Fork-safety guards
- Add `&& github.event.pull_request.head.repo.fork == false` to job-level `if:` conditions in:
  - `.github/workflows/visual-testing.yml`
  - `.github/workflows/code-review.yml`
  - `.github/workflows/translate-keys.yml`
  - `.github/workflows/update-docs.yml`

These jobs use repository secrets; the guard avoids exposing secrets or failing runs on forked PRs.

## Secrets scan
- No high-confidence secrets found in tracked files.
- No matches for common secret patterns in the last 100 commits.
- No `.gitleaks.toml` found; consider adding one if future allowlisting is needed.

## Next steps
- Apply the proposed changes via a maintainer PR, or grant this automation `workflows` permission to allow direct updates to workflow files.
