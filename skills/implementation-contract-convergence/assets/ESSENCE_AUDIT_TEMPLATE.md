# Essence Audit

This file is a human-readable provenance journal. It is not normative implementation authority.

## Status

- Essence: <path>
- State: PROPOSED | WAITING_FOR_OWNER | FROZEN
- Latest audited target: <immutable identity>
- Latest round: <N>

## Round <N>

- Target: <immutable identity>
- Auditor results:
  - A: PASS | FAIL | INVALID
  - B: PASS | FAIL | INVALID
  - C: PASS | FAIL | INVALID
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
- Unresolved owner decisions: none
