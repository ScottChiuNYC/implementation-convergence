# Semantic Coverage

Use this step before formal audit when the input includes a free-form conversation, design notes, or other owner-designated source material.

Its purpose is faithful compression, not premature requirements management.

## Rule

Keep the source conversation free-form. Structure only when producing the candidate Essence.

Check both directions.

### Source -> Essence

Identify every implementation-material item established by the source:

- objective and protected outcome;
- in-scope and out-of-scope behavior;
- constraints and invariants;
- domain/model conventions;
- interfaces or externally observable behavior;
- numerical or data assumptions when material;
- explicit tradeoffs and rejected alternatives;
- unresolved choices that remain genuinely unresolved.

For each item, verify that the candidate Essence represents it without weakening, strengthening, or changing its meaning.

### Essence -> source

Inspect every material requirement in the candidate Essence.

Classify it as one of:

- directly established by the source;
- already established by current repository authority;
- a non-material editorial normalization;
- unsupported material invention.

Remove or surface unsupported material inventions. Do not let drafting silently decide architecture, model behavior, product behavior, or another protected outcome.

## Conflict handling

A clear current owner decision supersedes an older draft statement.

When two current authoritative sources conflict and the owner's intended resolution is not clear, preserve the conflict as an unresolved item. Do not choose a side merely to make the draft look complete.

## Completion

Semantic coverage is complete when:

- no material source decision is missing or distorted;
- no material Essence decision is unsupported;
- genuine unresolved choices remain visible;
- the candidate can be audited without rereading the original conversation.

This is a coverage check, not a formal PASS. Formal independent audit starts afterward.
