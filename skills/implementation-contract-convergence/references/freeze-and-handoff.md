# Freeze and Handoff

## Owner barrier

Escalate only after canonical reconciliation establishes that a material choice is not determined by current authority.

At WAITING_FOR_OWNER:

- persist the canonical decision packet;
- present **every** pending decision directly in the owner-facing conversation, not merely a link to the durable packet. For each decision show its stable ID, exact question, alternatives labeled A/B/C with descriptive names, concise pros/cons and consequences, and a clearly non-binding recommendation by letter with rationale (or explain why no recommendation is justified);
- include the durable packet link as a reference, not as a substitute for the conversational presentation;
- invite concise responses such as `D-01: B, D-02: A`; interpret them using the stable decision-ID/letter mapping and clarify only ambiguous responses;
- preserve alternative labels and meanings across re-presentation; do not silently renumber or rename an existing choice;
- record the owner's actual selections and their resolved meanings durably, then resume the workflow without an additional approval gate unless another genuine owner decision is needed;
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

A frozen Essence reopens only for a material contract change to the responsibility it owns, including a material change in the Project Boundary assumptions that responsibility relies on.

After reopening:

    FROZEN
    -> PROPOSED / REOPENED
    -> fresh formal audit
    -> reconciled PASS
    -> new freeze

Do not reopen for implementation-only changes that remain inside the frozen contract.

Do not create a new Essence merely to avoid reopening an existing responsibility. Create a new Essence only when the increment introduces a genuinely new coherent responsibility or component.

See `incremental-development.md` for the full classifier and incremental audit-scope rules.
