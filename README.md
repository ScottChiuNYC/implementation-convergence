# Implementation Convergence

Reusable skills for converging implementation intent into a frozen contract and verified code.

## Skills

### Implementation Contract Convergence

v0.1 drafted.

skills/implementation-contract-convergence/ converges free-form implementation intent or a draft Essence into a frozen, unambiguous implementation contract.

Its loop is:

    human explicit trigger
    -> conversation or draft Essence
    -> semantic coverage
    -> backend selection
    -> independent audit
    -> reconciliation
    -> remediation when determined by existing authority
    -> fresh re-audit
    -> PASS
    -> freeze

Owner escalation occurs only after canonical reconciliation proves that a material choice cannot be determined from current authority.

This skill is intentionally manual-only at the outer boundary. An agent should not decide on its own that a discussion is ready to enter contract convergence. Once a human invokes it, the internal loop may run autonomously until FROZEN, WAITING_FOR_OWNER, or a fail-closed blocker.

### Contract-to-Code Convergence

Planned second skill.

skills/contract-to-code-convergence/ currently contains only a placeholder. No SKILL.md exists yet, so its protocol is intentionally undefined.

See docs/lifecycle.md for the repository-level boundary between the two skills.

## Load the skill

The source of truth is:

    skills/implementation-contract-convergence/

For a target repository, the most portable repo-local location shared by Codex and GitHub Copilot is:

    <target-repo>/.agents/skills/implementation-contract-convergence/

Place the complete skill directory there, including SKILL.md, references/, assets/, and agents/.

During v0.1 development, prefer a deliberate copy, vendor, or sync step from this repository rather than editing divergent copies by hand.

### Codex

OpenAI documents repo-local Codex skills under .agents/skills/.

After the skill is present in the target repository, invoke `$implementation-contract-convergence` explicitly, for example:

    Converge docs/model/ESSENCE.md using the local backend.

Or invoke the same skill explicitly with this request when remote GitHub transport is desired and the required GitHub capabilities are available:

    Converge docs/model/ESSENCE.md using the GitHub backend.

The skill's agents/openai.yaml sets policy.allow_implicit_invocation to false, so Codex should not implicitly enter this workflow.

### GitHub Copilot in VS Code

GitHub Copilot recognizes .agents/skills/ as a project skill location. It also supports personal skills under ~/.agents/skills/ or ~/.copilot/skills/.

Invoke the skill from VS Code chat with the slash command:

    /implementation-contract-convergence Converge docs/model/ESSENCE.md using the local backend.

The SKILL.md frontmatter sets user-invocable to true and disable-model-invocation to true, so the skill appears for explicit user invocation but is not automatically loaded by the model.

For Copilot CLI, the same slash-command form applies after the skill is installed or discovered.

## Backends

There is one skill, not separate local and GitHub versions.

The protocol is backend-neutral:

    Implementation Contract Convergence
                 |
          backend selection
          /             \
       local           GitHub
 filesystem + git    Issues + PRs
          \             /
           same logical state
                 |
            Frozen Essence

### Local backend

Use for VS Code Copilot, local Codex, or another host with filesystem read/write, git, and fresh isolated subagents or workers.

Raw Auditor results, reconciliation, owner-decision state, and remediation state live in local runtime files. The tracked ESSENCE_AUDIT.md remains the concise human journal.

The default posture is handoff-only: converge and freeze on an isolated branch or worktree, then stop for human review rather than merging automatically.

### GitHub backend

Use when the host has GitHub Issue and PR mutation plus readback and remote durable collaboration is desired.

Use a round-control Issue, one sealed raw-result Issue per Auditor slot, a reconciliation record, durable owner-decision records, focused remediation branch and PR, and exact-SHA validation and readback.

GitHub is transport, not protocol authority.

See the backend references inside the skill for full rules.

## Repository layout

    skills/
      implementation-contract-convergence/
        SKILL.md
        agents/
          openai.yaml
        references/
          semantic-coverage.md
          state-model.md
          backend-selection.md
          backend-local.md
          backend-github.md
          auditor.md
          reconciler.md
          remediator.md
          execution-policy.md
          freeze-and-handoff.md
        assets/
          ESSENCE_AUDIT_TEMPLATE.md
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
- Keep protocol semantics backend-neutral.
- Human activation gates the outer workflow; automation belongs inside the activated workflow.
- Prefer a small shared infrastructure layer.
- Use normal feature branches and pull requests for broad or structural changes.
- Use Remote Safe Patch only for narrow single-file exact edits.
- Keep the generated CodeBinder PDF reviewable.
- Prefer squash merge for focused pull requests.

## License

MIT. See LICENSE.
