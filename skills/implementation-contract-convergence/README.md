# Implementation Contract Convergence

This skill converges a draft Essence to a frozen contract. [SKILL.md](SKILL.md) defines the formal protocol; these examples are only explicit invocation interfaces.

## Copy-paste invocation examples

### GitHub backend (ChatGPT Work or another compatible host)

```text
Use the Implementation Contract Convergence Skill from:
https://github.com/ScottChiuNYC/implementation-convergence

Target repository: <repository URL>
Target Essence: <repository-relative path>
Use the GitHub backend.

Converge the specified draft Essence through the Skill's defined final state.
Escalate only genuine owner decisions or unavoidable blockers.
Follow the Skill's own protocol.
```

### Local backend (compatible Codex / VS Code Copilot host)

Make the skill available to the host as described in the [repository README](../../README.md), then explicitly invoke:

```text
Use the Implementation Contract Convergence Skill.
Target repository: <local repository path>
Target Essence: <repository-relative path>
Use the local backend.

Converge the specified draft Essence through the Skill's defined final state.
Escalate only genuine owner decisions or unavoidable blockers.
Follow the Skill's own protocol.
```

The local backend requires durable shared state and isolated workers. The GitHub backend requires durable GitHub read/write and isolated workers. Neither example bypasses compatibility checks or changes the skill's owner-decision, freeze, handoff or merge rules. Work, Codex and Copilot are examples of hosts, not guarantees of capability.

The **Target Essence path is required** for repository-scoped invocations, including incremental development. Do not assume the only Essence in a repository is the intended target. Version labels alone are insufficient when ambiguous.
