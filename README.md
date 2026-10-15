# Implementation Convergence

Reusable skills for converging implementation intent into a frozen contract and verified code.

## Skills

### Implementation Contract Convergence

v0.1 drafted.

skills/implementation-contract-convergence/ converges free-form implementation intent or a draft Essence into a frozen, unambiguous implementation contract.

Its loop is:

    human explicit trigger
    -> compatibility gate
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

An **Essence** is the durable, normative, implementation-ready contract for one implementation scope. It is interpreted against an established **Project Boundary**: the durable environment and reusable capabilities the component may assume already exist. The portable standards live in `references/essence.md` and `references/project-boundary.md`.

The generic model is intentionally only:

    effective implementation contract
    = Essence
    + Project Boundary

An Essence may be physically split into referenced normative files for readability, but those files remain one Essence contract. The skill does not create a generic Dedicated Contract taxonomy. If specification pressure suggests a substantial reusable subsystem, treat that first as evidence to re-check the single-responsibility / project boundary rather than automatically adding another spec.

For incremental development, an Essence belongs to a coherent responsibility rather than a milestone. Contract-preserving implementation changes leave the Essence frozen; material changes to the same responsibility reopen it; a genuinely new responsibility gets a new Essence. Formal audit remains bound to an exact repository SHA while its declared scope stays limited to the changed responsibility, affected interfaces, and relevant Project Boundary.

This skill is intentionally manual-only at the outer boundary. An agent should not decide on its own that a discussion is ready to enter contract convergence. Once a human invokes it and the host passes the compatibility gate, the internal loop may run autonomously until FROZEN, WAITING_FOR_OWNER, or a fail-closed blocker.

#### Hard compatibility

A formal run requires an agent host that can:

- launch fresh, sufficiently isolated subagents or workers;
- prevent sibling Auditor findings from leaking before sealing;
- provide durable shared run state through the selected backend;
- reconstruct the run after interruption;
- bind formal rounds to immutable target identities.

If these conditions are not met, the host may help draft or review an Essence, but it must not claim a formal convergence PASS or freeze.

The compatibility rule is capability-based rather than tied to product names.

Auditor inputs are verified and allowlisted by the dispatcher before launching fresh contexts. Workers receive current authority and generic instructions, not backend responses or run history. Hosts with inherited tools provide delivery-only separation, not enforced access isolation; record that limitation and fail closed when required isolation is unavailable. See `skills/implementation-contract-convergence/references/auditor-inputs.md`.

In current intended usage:

- VS Code Copilot or local Codex normally use the local backend when they have persistent shared filesystem state, git, and isolated workers;
- Codex may use either backend depending on its execution environment;
- ChatGPT Work or another cloud/mobile-oriented host should use the GitHub backend when isolated workers are available but durable local state is not guaranteed;
- ordinary chat without fresh isolated worker capability is not a compatible formal host.

### Contract-to-Code Convergence

Planned second skill.

skills/contract-to-code-convergence/ currently contains only a placeholder. No SKILL.md exists yet, so its protocol is intentionally undefined.

See docs/lifecycle.md for the repository-level boundary between the two skills.

## Load the skill

The source of truth is:

    skills/implementation-contract-convergence/

For a target repository, the most portable repo-local location shared by Codex and GitHub Copilot is:

    <target-repo>/.agents/skills/implementation-contract-convergence/

Place the complete skill directory there, including SKILL.md, references/, assets/, agents/, and optional scripts/.

During v0.1 development, prefer a deliberate copy, vendor, or sync step from this repository rather than editing divergent copies by hand.

### Codex

OpenAI documents repo-local Codex skills under .agents/skills/.

After the skill is present in the target repository, invoke `$implementation-contract-convergence` explicitly, for example:

    Converge docs/model/ESSENCE.md using the local backend.

Or invoke the same skill explicitly with this request when remote GitHub transport is desired and the required GitHub capabilities are available:

    Converge docs/model/ESSENCE.md using the GitHub backend.

The skill's agents/openai.yaml sets policy.allow_implicit_invocation to false, so Codex should not implicitly enter this workflow.

### ChatGPT Work

The OpenAI skill metadata exposes this skill to both CHAT and CODEX while keeping implicit invocation disabled.

Invoke it explicitly in Work, for example:

    Use the Implementation Contract Convergence skill on docs/model/ESSENCE.md. Use the GitHub backend.

Do not select the local backend merely because Work exposes a cloud computer or writable filesystem. Use local only when the host can establish the local durability contract in references/backend-local.md. Otherwise, when Work has fresh isolated workers plus the required GitHub connector capabilities, use the GitHub backend.

A normal ChatGPT conversation that cannot launch fresh isolated workers does not pass the formal compatibility gate.

### GitHub Copilot in VS Code

GitHub Copilot recognizes .agents/skills/ as a project skill location. It also supports personal skills under ~/.agents/skills/ or ~/.copilot/skills/.

Invoke the skill explicitly from VS Code chat or Copilot CLI with:

    /implementation-contract-convergence Converge docs/model/ESSENCE.md using the local backend.

The canonical SKILL.md keeps portable Agent Skills frontmatter. The manual-only rule is therefore enforced by the skill body itself rather than by GitHub-specific top-level metadata.

For a Copilot-only vendored copy, GitHub also supports the non-portable frontmatter extensions user-invocable: true and disable-model-invocation: true as an additional client-side guard. Do not add those extensions to the canonical portable SKILL.md.

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

Use for VS Code Copilot, local Codex, or another host with persistent shared filesystem read/write, git, and fresh isolated subagents or workers.

Raw Auditor results, reconciliation, owner-decision state, and remediation state live in local runtime files. The tracked ESSENCE_AUDIT.md remains the concise human journal.

A temporary cloud filesystem is not enough. The local backend requires durable shared run state that survives the expected convergence and recovery lifecycle.

The default posture is handoff-only: converge and freeze on an isolated branch or worktree, then stop for human review rather than merging automatically.

### GitHub backend

Use when the host has GitHub Issue and PR mutation plus readback and remote persistence or collaboration is desired.

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
          essence.md
          project-boundary.md
          incremental-development.md
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
- Verify host compatibility before formal execution.
- Prefer a small shared infrastructure layer.
- Use normal feature branches and pull requests for broad or structural changes.
- Use Remote Safe Patch only for narrow single-file exact edits.
- Keep the generated CodeBinder PDF reviewable.
- Prefer squash merge for focused pull requests.

## License

MIT. See LICENSE.
