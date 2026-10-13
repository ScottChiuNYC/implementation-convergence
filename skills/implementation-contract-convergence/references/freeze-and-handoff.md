# Freeze and Handoff

## Owner barrier

Escalate only after canonical reconciliation establishes that a material choice is not determined by current authority.

At WAITING_FOR_OWNER:

- persist the canonical decision packet;
- stop authoritative remediation that depends on the unresolved choice;
- preserve the exact candidate and round state;
- resume only after the owner's answer is durably incorporated.

## PASS precondition

Freeze requires:

- a complete formal round;
- valid results from all required Auditor slots;
- reconciled PASS;
- zero canonical substantive findings;
- zero unresolved owner decisions;
- unchanged audited authority since the PASS target was established.

## Freeze writeback

Freeze writeback is mechanical.

It may:

- mark the Essence FROZEN or IMPLEMENTATION_READY;
- record the audited target identity;
- record the reconciled PASS / audit record locator;
- update the human audit journal or repository index.

It must not make a substantive contract change.

If substantive contract text must change, the previous PASS no longer authorizes freeze. Reopen and run a fresh formal round.

## Frozen handoff contract

A successful output to the next stage consists of:

- the canonical frozen Essence locator;
- an immutable identity for the frozen contract state;
- explicit frozen / implementation-ready status;
- the latest reconciled PASS provenance;
- no unresolved owner-decision items.

The Essence is normative authority.

Audit reports, raw findings, reconciliation records, and remediation history are provenance. They must not be required to discover missing implementation requirements.

## Reopen

A frozen Essence reopens only for a material contract change.

After reopening:

    FROZEN
    -> PROPOSED / REOPENED
    -> fresh formal audit
    -> reconciled PASS
    -> new freeze
