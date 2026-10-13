# Local Backend

Use this backend for IDE agents and local coding agents that have filesystem, git, and fresh subagent capability but do not need GitHub Issues as workflow transport.

## Local runtime state

Default runtime root:

    .implementation-convergence/
      runs/
        <run-id>/
          run.json
          round-001/
            round.json
            auditor-a.md
            auditor-b.md
            auditor-c.md
            reconciliation.md
            remediation.json
          owner-decisions/
            <decision-id>.md

The exact filenames may vary with the configured Auditor slots, but the logical records in state-model.md must exist.

This directory is machine/control state, not normative repository content.

If the runtime root is inside the worktree, exclude it locally before formal audit, preferably through .git/info/exclude, so runtime writes do not alter the audited repository snapshot or create accidental commits.

Do not add runtime state to the target repository merely to make it durable.

## Human journal

Maintain a tracked ESSENCE_AUDIT.md adjacent to the Essence, using the provided asset as a starting point.

The journal is concise human provenance. It is not a substitute for raw machine records and is not normative implementation authority.

Update it after reconciled transitions, owner decisions, remediation closeout, and freeze.

## Immutable targets

Use exact git commit SHAs as formal audit targets.

Before a formal round:

1. ensure the candidate Essence and every repository-authoritative dependency needed for the audit are represented by the target commit;
2. record that commit SHA in round state;
3. give every Auditor the same SHA;
4. do not mutate that target while the round is active.

If the workspace contains unrelated uncommitted work that prevents an exact target, isolate the convergence work in a branch or worktree, or stop rather than folding unrelated changes into the contract target.

## Auditor isolation

Create fresh independent Auditor contexts.

The coordinator may write a result to the local runtime root only after that Auditor has sealed it.

An Auditor must not receive sibling result paths or contents before sealing.

Only the Reconciler reads all sealed results together.

## Remediation

Perform contract edits on an isolated convergence branch or worktree.

The Remediator receives only canonical findings, resolved owner decisions, and current durable authority.

After remediation:

1. validate the intended contract changes;
2. create an exact git commit representing the new candidate;
3. record its SHA;
4. start a fresh formal round against that SHA.

Do not claim PASS from remediation self-checks.

## Integration posture

For this skill, the safe default is handoff-only:

- converge on an isolated branch or worktree;
- freeze the exact successful contract state;
- leave the branch or commit for human review;
- do not merge to the project's canonical branch unless the human or repository policy explicitly authorizes that action.

This matches the owner-review boundary between contract convergence and later code implementation.

## Recovery

After interruption:

1. read run state;
2. reconcile it with actual git and worktree state;
3. use sealed records only when their exact target identities still match;
4. never recreate missing raw findings from memory.

If required raw evidence is missing or target identity cannot be established, fail closed and start a fresh authorized round.

## Completion

Local-backend success requires a reconciled PASS for the exact target, mechanical freeze writeback only, exact frozen commit identity, zero unresolved owner decisions, an updated human journal, runtime records sufficient to reconstruct the formal round, and explicit handoff of the branch or commit to the human.

No GitHub Issue or PR is required for formal validity.
