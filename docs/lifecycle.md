# Implementation Convergence Lifecycle

This repository contains two related but independently usable skills.

    free-form design conversation / draft Essence
            |
            v
    Implementation Contract Convergence
            |
            v
    frozen, unambiguous implementation contract
            |
            v
    owner review
            |
            v
    Contract-to-Code Convergence
            |
            v
    verified implementation

## Current state

### Implementation Contract Convergence

Drafted as v0.1 under skills/implementation-contract-convergence/.

It owns:

- conversation/draft -> initial Essence coverage;
- independent contract audit;
- canonical reconciliation;
- bounded remediation;
- narrow owner escalation;
- verified freeze.

### Contract-to-Code Convergence

Not yet authored.

The placeholder directory exists only to make the intended repository shape explicit. It has no SKILL.md and therefore defines no executable skill contract.

## Boundary

The frozen Essence is the normative handoff artifact.

Audit history is provenance, not hidden implementation authority.

Each skill should remain self-contained. Shared repository infrastructure should be introduced only when both skills genuinely require it.
