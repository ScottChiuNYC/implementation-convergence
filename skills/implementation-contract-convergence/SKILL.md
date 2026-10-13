---
name: implementation-contract-convergence
description: Converge free-form implementation intent or a draft Essence into a frozen, unambiguous implementation contract through semantic coverage checking, independent audits, reconciliation, bounded remediation, and owner escalation only when a material choice cannot be determined. Use when the user wants to turn design discussion, requirements, or an existing Essence into an implementation-ready frozen contract, or asks to audit, refine, converge, or freeze an Essence. Do not use to implement code from a frozen contract.
---

# Implementation Contract Convergence

Converge implementation intent into a standalone frozen contract that an independent implementer can execute without making a material product, model, or architecture decision on the owner's behalf.

The contract may intentionally leave implementation freedom when all allowed choices are materially equivalent.

## Inputs

Accept any of these starting points:

- a free-form design conversation or notes;
- an existing draft Essence;
- a draft Essence plus conversation or other owner-designated source material.

Use current owner instructions and current repository authority. Do not silently import stale chat history or legacy protocol as authority.

The final Essence must stand on its own. Formal audit must not depend on hidden conversation context.

## Entry: draft and semantic coverage

If no Essence exists, draft the initial Essence from the available design context.

If an Essence exists and the current conversation or owner-designated notes contain relevant decisions, compare them before formal audit.

Read references/semantic-coverage.md and perform both directions:

1. source -> Essence: every material decision, constraint, assumption, non-goal, and unresolved choice from the source is represented faithfully;
2. Essence -> source: the Essence does not invent a material decision that the source did not establish.

Repair ordinary omissions or distortions before formal audit. Preserve genuine unresolved choices as unresolved; do not guess.

## Formal convergence loop

When the candidate Essence is ready for formal audit:

1. establish the exact candidate and repository/workspace authority being audited;
2. create or update the adjacent human-readable audit journal;
3. run fresh independent Auditor slots against the same immutable target;
4. after every required Auditor result is sealed, run a fresh Reconciler;
5. follow exactly one transition:
   - PASS -> FREEZE
   - FAIL + no owner decision -> REMEDIATE -> fresh audit
   - FAIL + owner decision -> WAITING_FOR_OWNER
6. after remediation, audit the new exact target from scratch;
7. stop only at verified freeze, WAITING_FOR_OWNER, or a fail-closed execution blocker.

Use references/execution-policy.md for independence and target rules.

## Role boundaries

Load the role reference only when that role is active:

- Auditor: references/auditor.md
- Reconciler: references/reconciler.md
- Remediator: references/remediator.md
- Freeze / owner handoff: references/freeze-and-handoff.md

The coordinating/root agent owns workflow transitions and durable bookkeeping. It must not substitute its own substantive judgment for an Auditor, Reconciler, or owner decision.

## What counts as a blocker

A formal finding must be capable of changing a materially protected implementation outcome.

Typical blockers include:

- contradictory normative requirements;
- missing behavior that forces the implementer to choose among materially different outcomes;
- ambiguous scope, state transition, interface, numerical convention, error behavior, data ownership, or acceptance condition;
- an unstated assumption whose alternatives materially change implementation;
- a requirement that cannot be reconstructed from durable authority.

These are not blockers by themselves:

- prose style;
- naming taste;
- unspecified private code shape;
- implementation freedom where compliant choices are materially equivalent;
- a reviewer's preference for additional explanation that does not affect implementation behavior.

## Owner barrier

Do not ask the owner merely because an Auditor raised a question.

First complete the full audit round and reconciliation.

Escalate only when canonical reconciliation establishes that current authority cannot determine a material choice. Present the smallest decision packet needed to unblock convergence. Do not continue authoritative remediation across an unresolved owner decision.

## Freeze rule

A reconciled PASS authorizes freeze only for the exact audited authority state.

Freeze writeback is mechanical. It may mark status, record provenance, and update the audit journal, but it must not change substantive contract meaning.

If substantive wording must change, reopen the candidate and run a fresh audit.

Read references/freeze-and-handoff.md before freezing.

## Progress guard

Do not loop forever.

If materially the same canonical blocker survives two consecutive remediation attempts, diagnose whether the cause is:

- a missing owner decision;
- an execution/tooling limitation;
- remediation that failed to implement the canonical finding.

Then stop at the appropriate durable boundary rather than repeating the same round indefinitely.

## Output

Success means all of the following are true:

- the Essence is explicitly frozen / implementation-ready;
- the latest formal round is reconciled PASS;
- the freeze corresponds to the exact audited authority state;
- there are no unresolved owner decisions;
- the audit journal records enough provenance to reconstruct the convergence history;
- the frozen Essence itself contains all normative implementation authority needed by the next stage.

Audit history is provenance, not hidden implementation authority.

## Not this skill

Do not implement the frozen contract here.

Code generation, acceptance-test derivation, implementation, implementation remediation, and contract-to-code conformance belong to the separate Contract-to-Code Convergence skill.
