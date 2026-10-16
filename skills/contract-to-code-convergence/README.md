# Contract-to-Code Convergence — v0.1 draft

Second, independent skill in this repository. Input: a FROZEN / IMPLEMENTATION_READY Essence plus Project Boundary. Output: verified contract-conformant implementation; merge only when authorized.

Workflow: preflight and skeleton baseline -> **independently sealed acceptance manifest and feasible executable acceptance assets before code** -> implementation -> independent contract/code review and focused remediation -> fresh independent final verification with newly derived supplemental cases -> optional squash merge. Publication, CodeBinder PDF and downstream propagation are opt-in follow-up actions.

Read [SKILL.md](SKILL.md), [acceptance manifest](references/acceptance-manifest.md), and [state and handoff](references/state-and-handoff.md).

Status: **first single-invocation E2E PASS with qualifications (C2C-20261016-01)**, not production-ready. The pde-solver-convergence-test PR #2 reached authorized squash merge after 37 sealed acceptance criteria, implementation, independent review, and fresh final verification. The independent meta-review identified unresolved evidence of the former explicit Essence-path gate, context-based rather than enforced worker isolation, and incomplete retention of scratch logs. This protocol revision addresses those documentation and evidence gaps; it has not itself passed a new E2E run.

Explicit human invocation required. Formal execution needs isolated workers, durable state, exact-SHA checks and real build/test access. GitHub and local are intended backends, not yet independently certified for this new skill.

## Copy-paste invocation examples

These are minimal **explicit human triggers**. Replace placeholders. [SKILL.md](SKILL.md) is authoritative for acceptance analysis, implementation, independent review, remediation, verification, and terminal states; prompts must not restate its internal workflow.

### GitHub backend (ChatGPT Work or another compatible host)

```text
Use the Contract-to-Code Convergence Skill from:
https://github.com/ScottChiuNYC/implementation-convergence

Target repository: <repository URL>
Target Essence: <optional repository-relative path>
Use the GitHub backend.

Implement the specified FROZEN Essence Contract and complete the Skill's workflow through its defined final state.
Escalate only genuine owner decisions or unavoidable blockers.
Follow the Skill's own protocol.
```

**Optional authorization**, append only if desired:

```text
You are authorized to squash merge when all required verification criteria pass.
```

Without this authorization (or another valid prior authorization), do not infer merge permission. Publication and downstream propagation remain separately governed by the Skill.

### Local backend (compatible Codex / VS Code Copilot host)

Install or make the skill available to the host as documented in the [repository README](../../README.md), then explicitly invoke it:

```text
Use the Contract-to-Code Convergence Skill.
Target repository: <local repository path>
Target Essence: <optional repository-relative path>
Use the local backend.

Implement the specified FROZEN Essence Contract and complete the Skill's workflow through its defined final state.
Escalate only genuine owner decisions or unavoidable blockers.
Follow the Skill's own protocol.
```

The local backend requires durable state, isolated workers and actual build/test execution capability. These examples do not assert that a specific host passes the compatibility gate.

The **Target Essence path is optional** when exactly one unambiguous FROZEN / IMPLEMENTATION_READY Essence exists. Explicit paths take precedence and must be validated. If several candidates exist, ask the owner; if none exists, stop. Record the selected path and immutable authority identity for recovery.
