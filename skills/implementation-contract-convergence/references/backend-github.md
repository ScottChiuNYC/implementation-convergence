# GitHub Backend

Use GitHub as durable control-plane transport when the host has GitHub mutation and readback capability and remote persistence or collaboration is desired.

GitHub transport must preserve the same logical records and role boundaries as the local backend.

## Exact target

Every formal round binds to one immutable git commit SHA and the explicit repository-relative Target Essence path. Record the path, blob identity, repository and commit SHA in the round identity; never substitute another Essence or infer scope from a repository default.

Issue and comment activity does not change the target. Repository commits may invalidate audit authority.

## Dispatcher-only verification and delivery

Before launching Auditors, the dispatcher follows `auditor-inputs.md`: verify the commit/tree and exact-ref allowlisted blobs, inspect contents, then deliver only the clean packet. The dispatcher owns GitHub reads, result writes and readback; Auditors do not invoke the connector.

Prefer Git-data commit metadata (`GET /repos/<owner>/<repo>/git/commits/<sha>`) and tree/blob or exact-ref file reads. Metadata responses still contain messages/parents: project only identities. A convenience commit/PR verification wrapper may return a full diff containing remediation reports even when no report was explicitly requested. Never pass such a response, its text blocks, full file list, or commit message to an Auditor. Projection must precede delivery; hiding it after it enters a worker's context cannot restore independence.

Control/result Issues and verification evidence remain dispatcher/Reconciler resources. Auditors receive assignment metadata, not Issue bodies or links to browse. Skill instructions may be pinned to a separate skill commit; record their identities in the input manifest.

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
- execution identity and input packet digest;
- exact target SHA;
- status: PENDING.

Each Auditor must remain blind to sibling result contents until it seals its own result.

After an Auditor finishes, mechanically write the complete result and mark it SEALED.

Do not substantively edit a sealed result. For contamination, preserve it as an invalid execution and precreate a new result Issue for a fresh execution of the same logical slot, target and scope. Record replacement linkage in coordinator state only. Apply `auditor-inputs.md`; no substantive or advisory verdict from the invalid execution counts.

## Reconciliation

Only after every configured slot has a valid sealed result for the same target, scope and input manifest may the Reconciler read them together. Preserve invalid result locators as excluded execution evidence, never as substantive findings or extra slots.

Persist the round and target identities, every raw result identity, raw-to-canonical mappings or explicit dismissals, canonical findings, owner-decision items, verdict, and next transition.

Then update round-control state mechanically.

## Owner decisions

Persist owner-decision items durably. At owner handoff, also render all pending items, labeled alternatives, trade-offs and advisory recommendations in the conversation as required by `freeze-and-handoff.md`; an Issue link alone is insufficient.

The human's actual resolution must be recorded before remediation proceeds across that decision boundary.

Keep the stable decision ID and complete letter-to-meaning mapping in the durable owner-decision record. Persist each actual owner response, source, selected letter and resolved meaning, including partial responses. On recovery, read the canonical records and actual owner replies before rendering only unresolved decisions. Never infer a selection from an agent-authored issue, an ambiguous reply or a missing response.

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

### CI applicability for contract-only changes

ICC is specification convergence, not solver implementation or numerical experimentation. Do not run builds/tests of application code or manually dispatch CI solely for an ICC audit or document-only freeze. For each PR or freeze writeback, inspect the changed paths and applicable repository policy (including required status checks/rulesets) before deciding that CI is a gate.

When the change is confined to the Target Essence, `ESSENCE_AUDIT.md`, and other ICC control-plane documentation, **CI is not required by this skill**. Unless repository policy explicitly requires the check for those changes, mark the CI gate **not applicable (documentation-only)**, keep the exact-head/diff/readback/merge verification, and **do not wait** for automatically triggered push or pull_request build workflows. The fact that GitHub Actions started a run does not itself create a CI wait requirement.

If repository policy actually requires CI or publication for the change, verify the exact applicable run/publication to terminal state rather than treating queued, skipped, or in-progress as completion. For implementation, build configuration, dependency, and test changes, honor the project's normal CI policy; this exception never weakens C2C verification. If branch protection requires a job skipped by path filtering, treat that as a repository integration blocker; do not bypass protection or claim the missing required check passed.

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
