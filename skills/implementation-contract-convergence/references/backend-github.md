# GitHub Backend

Use GitHub as durable control-plane transport when the host has GitHub mutation and readback capability and remote persistence or collaboration is desired.

GitHub transport must preserve the same logical records and role boundaries as the local backend.

## Exact target

Every formal round binds to one immutable git commit SHA.

Issue and comment activity does not change the target. Repository commits may invalidate audit authority.

## Canonical control-plane shape

For each formal round use:

    round-control issue
      |- one precreated raw-result issue per Auditor slot
      `- one reconciliation issue or record

The round-control issue records the round identity, exact target SHA, configured Auditor slots, raw-result record identities, reconciliation record identity, and round-level state only.

Before all Auditor slots are sealed, do not copy raw finding content into the round-control issue.

## Auditor result issues

Precreate one result issue per slot with assignment metadata only:

- round identity;
- slot identity;
- exact target SHA;
- status: PENDING.

Each Auditor must remain blind to sibling result contents until it seals its own result.

After an Auditor finishes, mechanically write the complete result and mark it SEALED.

Do not substantively edit a sealed result. A correction requires a fresh replacement slot or fresh round with preserved provenance.

## Reconciliation

Only after every required result is sealed may the Reconciler read them together.

Persist the round and target identities, every raw result identity, raw-to-canonical mappings or explicit dismissals, canonical findings, owner-decision items, verdict, and next transition.

Then update round-control state mechanically.

## Owner decisions

Persist owner-decision items durably.

The human's actual resolution must be recorded before remediation proceeds across that decision boundary.

Do not treat an agent-authored issue body as owner approval.

## Remediation transaction

Use a focused branch and PR for substantive Essence changes.

Before merge:

1. read current repository authority;
2. verify the intended diff;
3. verify PR head SHA;
4. reconcile relevant base advancement;
5. validate the exact head;
6. squash merge only the exact validated head when merge is authorized.

After merge, re-read main and record the resulting exact SHA before starting the next formal round.

If repository policy requires CI or publication, verify the exact applicable run to terminal state rather than treating queued or in-progress as completion.

## Issue mutation safety

Issue writes are side effects even though they do not change the git tree.

For create, update, or close operations:

    observe current state
    -> verify round, slot, and target identity
    -> perform the narrow write
    -> read back
    -> reconcile before retry after an unknown outcome

Never use control issues as scratchpads.

## Recovery

After interruption or ambiguous tool outcome, read actual Issue, branch, PR, main, and workflow state before acting.

Recover the existing canonical transaction when possible instead of creating duplicate rounds, replacement issues, or version-suffixed branches.

## Human journal

Maintain ESSENCE_AUDIT.md as the concise tracked human journal even when complete raw workflow history lives in GitHub Issues.

Audit history remains provenance, not hidden contract authority.

## Completion

GitHub-backend success requires a reconciled PASS for the exact target, mechanical freeze writeback only, exact frozen contract identity, zero unresolved owner decisions, updated journal and durable control-plane records, and required repository integration or publication verification when applicable.

The GitHub backend is optional. If GitHub Issue or PR mutation is unavailable but local filesystem, git, and isolated workers are available, use the local backend instead.
