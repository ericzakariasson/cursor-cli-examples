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
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\s*[:=]`

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
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\s*[:=]`

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
- Generic assignments: case-insensitive `(api|secret|token|password|passwd|pwd|key)\s*[:=]\s*"..."`

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

# Security Audit Log

Date: 2025-11-20
Branch: audit-hardening
Scope: ericzakariasson/cursor-cli-examples

## Summary
- No potential secrets detected in repository files or the last 200 commits.
- Proposed minimal workflow hardening: pin actions to SHAs, add fork-PR guards on secret-using jobs, and add least-privilege permissions to test workflow. These changes are documented below but not pushed to workflows due to missing `workflows` permission for this token.

## Proposed Workflow Hardening (not applied via push this run)
- Pin actions:
  - actions/checkout@v4 -> `@34e114876b0b11c390a56381ad16ebd13914f8d5`
  - astral-sh/setup-uv@v4 -> `@e4db8464a088ece1b920f60402e813ea4de65b8f`
  - actions/upload-artifact@v4 -> `@ea165f8d65b6e75b540449e92b4886f43607fa02`
  - actions/setup-python@v5 -> `@a26af69be951a213d495a4c3e4e4022e16d87065`
- Add fork-PR guard: `if: github.event.pull_request.head.repo.fork == false` to jobs using `${{ secrets.* }}` in PR-triggered workflows.
- Add default least-privilege permissions to `.github/workflows/test.yml`: `permissions: { contents: read }`.

## Next Steps
- Re-run with a token that has `workflows` scope, or apply the above edits manually via a PR.

## Compare
- https://github.com/ericzakariasson/cursor-cli-examples/compare/main...audit-hardening

<!-- security-hardening-audit:2025-11-20 -->
