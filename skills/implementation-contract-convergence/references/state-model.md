# Backend-Neutral State Model

The protocol is defined in logical records. A backend chooses where those records live; it must not change their meaning.

## Required logical records

### Run

A run identifies one convergence attempt for one Essence.

Record at least the run identity, Essence locator, selected backend, current workflow state, current round identity when any, unresolved owner-decision identities, and final frozen contract identity when reached.

### Formal round

A formal round binds all Auditor slots to one immutable target and one declared audit scope.

Record at least the round identity, exact target identity, declared audit scope, configured Auditor slots, one raw-result locator per slot, reconciliation locator, round verdict, and next transition.

The target identity and declared audit scope must not change after the round begins.

### Raw Auditor result

Each Auditor slot produces one sealed result containing the round identity, slot identity, exact target identity, declared audit scope, verdict, complete substantive findings, available execution provenance, and sealed status.

A sealed result is immutable evidence. A substantive correction requires a fresh replacement slot or a fresh round with preserved provenance.

### Reconciliation

Persist the round identity, exact target identity, declared audit scope, every sealed raw-result identity, raw-to-canonical mappings or explicit dismissals, canonical findings, owner-decision items, round verdict, and next transition.

The next transition is REMEDIATE, WAITING_FOR_OWNER, or FREEZE.

### Owner decision

An owner-decision record contains a stable decision identity, affected canonical finding identities, exact question, materially viable alternatives, owner resolution, and durable source of that resolution.

Do not manufacture a resolution because the backend needs a value.

### Remediation

A remediation record contains the canonical findings authorized for repair, input target identity, remediation result identity, validation performed, and resulting exact target identity for the next fresh round.

Remediation does not itself establish PASS.

### Freeze

A freeze record contains the exact reconciled PASS target, frozen contract locator, frozen contract identity after mechanical freeze writeback, latest reconciliation locator, and confirmation that unresolved owner decisions are zero.

The Essence remains normative authority. Workflow records are provenance.

## Workflow states

Use these conceptual states:

    PROPOSED
    -> AUDITING
    -> RECONCILING
    -> REMEDIATING -> AUDITING
       or WAITING_FOR_OWNER
       or FREEZING -> FROZEN

A fail-closed operational condition may transition to BLOCKED from any active state.

Do not infer a later state merely because an agent says the work is complete. Establish the invariant required by that state first.

## Backend equivalence

| Logical record | Local backend | GitHub backend |
| --- | --- | --- |
| Run | run.json | control issue set plus repository state |
| Formal round | round.json | round-control issue |
| Raw Auditor result | auditor-slot files | one sealed result issue per slot |
| Reconciliation | reconciliation file | reconciliation issue or record |
| Owner decision | local durable decision record | durable owner-decision issue or record |
| Remediation | remediation record plus git identity | branch or PR plus record |
| Exact target | git commit SHA | git commit SHA |
| Human journal | ESSENCE_AUDIT.md | ESSENCE_AUDIT.md |

Backend-specific convenience must never weaken exact-target binding, Auditor independence, owner authority, or freeze rules.
