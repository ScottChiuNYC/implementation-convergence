# Incremental Development

## Purpose

Implementation Contract Convergence is not limited to a project's first implementation.

Use it whenever incremental development introduces or changes a **material implementation responsibility**. Do not run a new contract-convergence cycle merely because another sprint, feature branch, refactor, or release begins.

An Essence belongs to a coherent implementation responsibility or scope, not to a development milestone.

## Decision rule

For each proposed increment, classify the change before drafting a new contract.

### No Essence change

Do not reopen or create an Essence when the existing frozen contract already determines the intended behavior and the change is materially contract-preserving.

Typical examples:

- refactoring;
- performance optimization that preserves protected behavior and guarantees;
- internal data-structure changes;
- bug fixes where the frozen Essence already states the correct behavior;
- implementation cleanup or test expansion that does not change the material contract.

These changes belong to implementation/conformance work, not contract convergence.

### Reopen the existing Essence

Reopen a frozen Essence when the **same coherent responsibility** changes materially.

Examples include:

- adding a new supported mode to an existing component;
- changing public or cross-layer behavior;
- changing a numerical convention, failure policy, ownership rule, compatibility guarantee, or other material contract;
- discovering that the frozen Essence itself omitted a material requirement.

Use:

```text
FROZEN
-> REOPENED / PROPOSED
-> converge changed contract
-> fresh formal audit
-> reconciled PASS
-> new freeze
```

Do not create a feature-specific Essence merely to avoid reopening the existing responsibility.

### Create a new Essence

Create a new Essence when the increment introduces a **new coherent responsibility or component** with its own material behavior and lifecycle.

The new component is developed against the project's current durable boundary. Existing components keep their own frozen Essences; they do not need to be rewritten into the new Essence.

Do not create a new Essence merely because a change is large. Size is not the criterion; responsibility is.

## Project growth

Incremental development should let a project grow without any single Essence becoming a project-wide monolith.

Conceptually:

```text
Project Boundary
├── Essence A -> Component A
├── Essence B -> Component B
└── Essence C -> Component C
```

For a new component, already established repository mechanics and reusable capabilities may become part of its Project Boundary. Existing component contracts remain authoritative for the responsibilities they own.

The project does not need one ever-growing master Essence.

## Audit scope versus target identity

Formal audit remains bound to one exact immutable repository or workspace target.

That does **not** mean every increment requires re-auditing the entire project from first principles.

For incremental work, choose the smallest complete audit scope that can establish material correctness:

```text
audit scope
= changed or new Essence responsibility
+ materially affected interfaces
+ relevant Project Boundary
```

The exact repository SHA still anchors the authority state, while the declared audit scope limits what the round is certifying.

If a change materially affects another frozen Essence, that affected responsibility must be reopened or included in an explicitly coherent contract change. Do not hide cross-component contract changes inside a nominally local audit.

## Project Boundary changes

A Project Boundary may itself evolve.

When boundary changes are purely internal to a boundary-owned capability and preserve every relied-on contract, dependent Essences do not reopen.

When a boundary change alters an assumption, interface, guarantee, failure behavior, or other material dependency of an Essence, reopen every materially affected Essence before relying on the new boundary.

## Practical classifier

Use this table as a default:

| Change | Contract action |
| --- | --- |
| Refactor or optimization with materially equivalent behavior | No Essence change |
| Bug fix where frozen Essence already defines correct behavior | No Essence change |
| Material change to an existing responsibility | Reopen that Essence |
| Missing material requirement discovered in a frozen Essence | Reopen that Essence |
| New coherent responsibility or component | Create a new Essence |
| Project Boundary change with no material effect on an Essence | No Essence change |
| Project Boundary change that alters an Essence's material assumptions | Reopen affected Essence(s) |

## Design principle

Freeze only the next materially meaningful responsibility that is ready to implement.

Do not force a first-version Essence to predict the project's eventual architecture. Let later responsibilities emerge from real implementation needs, and use the existing repository and frozen contracts as durable context for the next increment.
