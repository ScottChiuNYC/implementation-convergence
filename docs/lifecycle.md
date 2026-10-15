# Implementation Convergence Lifecycle

This repository contains two related but independently usable skills.

    free-form design conversation or draft Essence
            |
            | human explicit invocation
            v
    compatibility gate
            |
            v
    Implementation Contract Convergence
            |
            | local or GitHub durable backend
            v
    frozen, unambiguous implementation contract
            |
            v
    optional owner review / risk gate
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

- explicit human activation;
- host compatibility verification;
- conversation or draft -> initial Essence coverage;
- backend-neutral durable workflow state;
- local and GitHub transport selection;
- independent contract audit;
- canonical reconciliation;
- bounded remediation;
- narrow owner escalation;
- verified freeze.

The outer workflow is human-triggered. Internal convergence may run autonomously after explicit invocation and a successful compatibility gate.

A formal run requires fresh sufficiently isolated workers plus durable shared state. A filesystem that is merely available inside a temporary cloud execution environment is not sufficient evidence for the local backend.

### Contract-to-Code Convergence

v0.1 drafted, not yet validated as a single-invocation end-to-end workflow.

The second skill owns pre-implementation independent acceptance derivation, implementation, independent review/remediation, fresh final verification, and optionally authorized merge. Publication/PDF/downstream propagation remain explicit project-level actions. It consumes frozen Essence plus Project Boundary without silently changing either.

## Boundary

The generic contract model is:

    effective implementation contract
    = Essence
    + Project Boundary

The frozen Essence is the normative handoff artifact for the component's own responsibility. The Project Boundary remains the durable authority for pre-existing repository mechanics and reusable capabilities outside that responsibility.

An Essence may be physically decomposed into referenced normative files, but that does not create additional generic contract categories.

Audit history is provenance, not hidden implementation authority.

Backend selection changes storage and integration mechanics only. It does not change the meaning of PASS, owner authority, Auditor independence, or freeze.

## Incremental development

An Essence belongs to a coherent implementation responsibility, not to a development milestone.

Use the smallest contract action that matches the change:

    contract-preserving implementation change
    -> keep the existing Essence frozen

    material change to the same responsibility
    -> reopen and reconverge the existing Essence

    new coherent responsibility or component
    -> create a new Essence against the current Project Boundary

Formal audit always binds to one exact immutable repository or workspace target, but an incremental round should certify only the smallest complete scope: the changed or new Essence responsibility, materially affected interfaces, and relevant Project Boundary.

A Project Boundary change reopens dependent Essences only when it changes a material assumption they rely on.

See `skills/implementation-contract-convergence/references/incremental-development.md` for the detailed classifier.

Each skill should remain self-contained. Shared repository infrastructure should be introduced only when both skills genuinely require it.
