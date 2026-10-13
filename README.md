# Implementation Convergence

Reusable skills for converging implementation intent into a frozen contract and verified code.

## Skills

### Implementation Contract Convergence

v0.1 drafted.

skills/implementation-contract-convergence/ converges free-form implementation intent or a draft Essence into a frozen, unambiguous implementation contract.

Its loop is:

    conversation / draft Essence
    -> semantic coverage
    -> independent audit
    -> reconciliation
    -> remediation when determined by existing authority
    -> fresh re-audit
    -> PASS
    -> freeze

Owner escalation occurs only after canonical reconciliation proves that a material choice cannot be determined from current authority.

### Contract-to-Code Convergence

Planned second skill.

skills/contract-to-code-convergence/ currently contains only a placeholder. No SKILL.md exists yet, so its protocol is intentionally undefined.

See docs/lifecycle.md for the repository-level boundary between the two skills.

## Repository layout

    skills/
      implementation-contract-convergence/
        SKILL.md
        references/
        assets/
      contract-to-code-convergence/
        README.md
    docs/
      lifecycle.md
      workflow/
    tests/
      implementation-contract-convergence/
    tools/

## Retained repository infrastructure

Only two reusable infrastructure capabilities are intentionally retained:

1. CodeBinder PDF — builds a reviewable whole-repository PDF and optionally publishes it to Google Drive.
2. Remote Safe Patch — provides a fail-closed path for narrow, exact edits made through connector-only GitHub workflows.

Everything else should earn its place based on the needs of these skills.

## Repository principles

- Keep skill semantics self-contained.
- Do not couple the two skills merely because they share a repository.
- Prefer a small shared infrastructure layer.
- Use normal feature branches and pull requests for broad or structural changes.
- Use Remote Safe Patch only for narrow single-file exact edits.
- Keep the generated CodeBinder PDF reviewable.
- Prefer squash merge for focused pull requests.

## License

MIT. See LICENSE.
