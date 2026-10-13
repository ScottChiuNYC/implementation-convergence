# Essence Audit

This file is a human-readable provenance journal. It is not normative implementation authority.

## Status

- Essence: <path>
- Run: <run identity>
- Backend: local | github
- State: PROPOSED | AUDITING | RECONCILING | REMEDIATING | WAITING_FOR_OWNER | FROZEN | BLOCKED
- Latest audited target: <immutable identity>
- Latest round: <N>

## Round <N>

- Target: <immutable identity>
- Auditor results:
  - <slot-id>: PASS | FAIL | INVALID — <durable result locator>
  - <repeat for every configured slot>
- Reconciliation: <durable locator>
- Canonical findings: <IDs or none>
- Closed findings: <IDs or none>
- Owner decisions: <IDs or none>
- Remediation identity: <commit / branch / PR / snapshot or none>
- Round verdict: PASS | FAIL
- Next state: REMEDIATE | WAITING_FOR_OWNER | FREEZE | DONE

## Freeze

- Reconciled PASS target: <immutable identity>
- Freeze identity: <immutable identity>
- Frozen contract: <path>
- Latest reconciliation: <durable locator>
- Unresolved owner decisions: none
