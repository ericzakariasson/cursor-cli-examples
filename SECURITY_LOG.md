# Security Audit Log

Date: 2025-11-25
Branch: audit-hardening
Scope: ericzakariasson/cursor-cli-examples

## Summary
- No potential secrets detected in tracked files or in the last 200 commits.
- Proposed minimal workflow hardening: pin actions to SHAs, add fork-PR guards on secret-using jobs, and set least-privilege permissions for tests. Applying workflow file edits may require repository-level `workflows` permission.

## Proposed Workflow Hardening
- Pin actions (verified this run):
  - `actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5` (v4)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4)
- Skip PR jobs that need secrets/write on forks:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Add explicit least-privilege permissions where missing; for test-only workflows:
  - `permissions: { contents: read }`

## Secret Scan Details
Patterns scanned (non-exhaustive):
- AWS access keys, GitHub personal tokens, Slack tokens, Google API keys, private key headers
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\\s*[:=]`

History window: tracked files and last 200 commits (diffs). No hits found.

## Guidance
- Keep actions pinned to SHAs; update periodically by bumping to the latest release SHA.
- Prefer job-level `permissions` scoped to the minimum needed; ensure each workflow declares a `permissions` block.
- Avoid `pull_request_target` unless absolutely necessary and well-guarded.
- Replace deprecated `apt-key` usage with keyring-based installation when feasible; avoid `curl | bash` unless validating source and checksums.

## Compare and Create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening?quick_pull=1

<!-- security-hardening-audit:2025-11-25 -->

---

# Security Audit Log

Date: 2025-11-12
Branch: audit-hardening
Scope: ericzakariasson/cursor-cli-examples

## Summary
- No plaintext secrets detected in tracked files in this run.
- No `.gitleaks.toml` allowlist found; consider adding one if you deploy gitleaks.
- Proposed minimal GitHub Actions workflow hardening (pin actions, fork guards, least-privilege permissions). Applying workflow file edits may require repository-level `workflows` permission.

## Proposed Workflow Hardening
- Add explicit least-privilege permissions where missing; for test-only workflows, set:
  - `permissions: { contents: read }`
- Skip PR jobs that need secrets/write on forks:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Pin third-party actions to immutable SHAs (verified this run):
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4)

## Secret Scan Details
Patterns scanned (non-exhaustive):
- AWS access keys, GitHub personal tokens, Slack tokens, Google API keys, private key headers
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\\s*[:=]`

History window: tracked files only in this run. For deeper coverage, consider periodic history scans with gitleaks.

## Guidance
- Keep actions pinned to SHAs; update by bumping to latest release SHAs.
- Prefer job-level `permissions` scoped to minimum needed; ensure each workflow declares a `permissions` block.
- Avoid `pull_request_target` unless absolutely necessary and well-guarded.

## Compare and Create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening?quick_pull=1

<!-- security-hardening-audit:2025-11-12 -->

---

# Security Audit Log

Date: 2025-11-08
Branch: audit-hardening
Scope: ericzakariasson/cursor-cli-examples

## Summary
- No potential secrets detected in tracked files (common patterns) in this run.
- No `.gitleaks.toml` allowlist found; consider adding if you deploy gitleaks.
- Proposed GitHub Actions workflow hardening with minimal, safe changes. Applying workflow file edits may require repository-level `workflows` permission.

## Proposed Workflow Hardening
- Add explicit least-privilege permissions where missing; for test-only workflows, set:
  - `permissions: { contents: read }`
- Skip PR jobs that need secrets/write on forks:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Pin third-party actions to immutable SHAs (verify upstream before applying):
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955` (v4)
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065` (v5)
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` (v4)
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a` (v4)
- Replace deprecated `apt-key` usage with keyring-based installation when feasible.
- Avoid `curl | bash` installers unless you validate source and checksums.

## Secret Scan Details
Patterns scanned (non-exhaustive):
- AWS access keys, GitHub personal tokens, Slack tokens, Google API keys, private key headers
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\\s*[:=]`

History window: tracked files only in this run. Consider adding a periodic history scan (e.g., gitleaks) for deeper coverage.

## Guidance
- Keep actions pinned to SHAs; update periodically by bumping to the latest release SHA.
- Prefer job-level `permissions` scoped to the minimum needed; ensure each workflow declares a `permissions` block.
- Avoid `pull_request_target` unless absolutely necessary and well-guarded.
- If future false positives arise in secret scans, add narrowly-scoped allowlist rules in a `.gitleaks.toml`.

## Compare and Create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening?quick_pull=1

<!-- security-hardening-audit:2025-11-08 -->

---

# Security Audit Log

Date: 2025-10-31
Branch: audit-hardening
Scope: ericzakariasson/cursor-cli-examples

## Summary
- No potential secrets detected in tracked files or in the last 200 commits.
- No `.gitleaks.toml` allowlist found; none required based on current scan.
- Proposed GitHub Actions workflow hardening with minimal, safe changes. Applying workflow file edits may require repository-level `workflows` permission.

## Proposed Workflow Hardening
- Add explicit least-privilege permissions where missing; for test-only workflows, set:
  - `permissions: { contents: read }`
- Skip PR jobs that need secrets/write on forks:
  - Example job condition: `${{ github.event.pull_request.draft == false && github.event.pull_request.head.repo.fork == false }}`
- Pin third-party actions to immutable SHAs (examples as of this run; verify upstream before applying):
  - `actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955`
  - `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065`
  - `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - `astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a`
- Replace deprecated `apt-key` usage with keyring-based installation when feasible.

## Secret Scan Details
Patterns scanned (non-exhaustive):
- AWS access keys, GitHub personal tokens, Slack tokens, Google API keys, private key headers
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\\s*[:=]\\s*\"...\"`

History window: last 200 commits (diffs). No hits found.

## Guidance
- Keep actions pinned to SHAs; update periodically by bumping to the latest release SHA.
- Prefer job-level `permissions` scoped to the minimum needed; ensure each workflow declares a `permissions` block.
- Avoid `pull_request_target` unless absolutely necessary and well-guarded.
- If future false positives arise in secret scans, add narrowly-scoped allowlist rules in a `.gitleaks.toml`.

## Compare and Create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening

<!-- security-hardening-audit:2025-10-31 -->

---

# Security Hardening Log

Date: 2025-12-04
Scope: ericzakariasson/cursor-cli-examples

Summary of actions
- Pinned GitHub Actions to immutable SHAs across workflows to prevent supply-chain drift.
- Added minimal permissions to missing workflow (`test.yml`), defaulting `contents: read`.
- Added fork-safety guards to steps that consume repository secrets so they do not run on forked PRs.
- Verified: no use of `pull_request_target`, no deprecated set-output/add-path/set-env commands, and most workflows already define explicit permissions.
- Secrets scan (current tree): no high-confidence secrets detected.

Details
- Pinned to SHAs
  - actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5
  - actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065
  - astral-sh/setup-uv@38f3f104447c67c051c4a08e39b64a148898af3a
  - actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02

- Workflows updated
  - .github/workflows/test.yml: add `permissions: contents: read`; pin checkout/setup-python
  - .github/workflows/visual-testing.yml: pin checkout/setup-uv/upload-artifact; add fork guard to secret-using step
  - .github/workflows/code-review.yml: pin checkout/setup-uv; add fork guard to secret-using step
  - .github/workflows/fix-ci.yml: pin checkout; add fork guard using workflow_run head repository
  - .github/workflows/translate-keys.yml: pin checkout; add fork guard to secret-using step
  - .github/workflows/update-docs.yml: pin checkout; add fork guard to secret-using step
  - .github/workflows/fix-conflicts.yml: pin checkout
  - .github/workflows/secrets-audit.yml: pin checkout

- Permissions review
  - Many workflows legitimately require `contents: write` and/or `pull-requests: write` to push branches or comment. No unnecessary broad permissions were identified beyond those functional needs.

- Secrets exposure review
  - No `.gitleaks.toml` found; no allowlist in place. Consider adding one if false positives arise in future scans.
  - No high-confidence secrets found in tracked files. If any secret rotation is suspected from external context, rotate in your secret manager and in GitHub Actions secrets.
  - Note: historical commit scanning is best handled with a dedicated tool (e.g., gitleaks or trufflehog). This pass covered the current working tree.

Remediation guidance
- Continue pinning all new workflow actions to SHAs.
- Keep `permissions` blocks explicit; prefer least-privilege per job.
- Avoid using `pull_request_target` unless absolutely necessary and guarded; prefer `pull_request` with `contents: read`.
- For steps that require organization secrets, gate execution for forked PRs as done here.

## Compare and Create PR
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening?quick_pull=1

<!-- security-hardening-audit:2025-12-04 -->
