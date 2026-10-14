# Essence

## Definition

An Essence is the durable, normative, implementation-ready contract for one implementation scope, interpreted against an established Project Boundary.

Its purpose is not to summarize a design conversation, preserve every research step, or prescribe private code shape. Its purpose is to remove material implementation ambiguity so that fresh independent implementers can produce materially equivalent in-scope outcomes without access to the originating conversation.

A file named `ESSENCE.md` is the normal representation, but the concept is the contract itself, not the filename.

An Essence belongs to a coherent implementation responsibility or scope, not to a sprint, release, feature branch, or development milestone. When a project evolves, reuse, reopen, or add an Essence according to `incremental-development.md` rather than creating a new project-wide specification for every increment.

## Core sufficiency test

A candidate Essence is ready to freeze only when all three statements are true:

- no material in-scope implementation decision remains unstated;
- no unintended material degree of implementation freedom remains;
- specification ambiguity cannot lead competent compliant implementers to materially different protected outcomes.

Intentional implementation freedom is allowed when the Essence explicitly delegates it or when all compliant choices are materially equivalent.

A frozen Essence must not require an implementer to infer a material decision from hidden chat context, audit history, reviewer memory, or undocumented convention.

## What "material" means

A choice is material when different reasonable choices can change an owner-protected outcome, including as applicable:

- scientific or model meaning;
- numerical behavior or convergence;
- public API or externally observable behavior;
- data semantics, provenance, units, coordinates, timing, or conventions;
- architecture boundaries, ownership, lifetime, or dependency direction;
- persistent state, concurrency, recovery, idempotency, or reconciliation;
- failure and unsupported-case behavior;
- security, authority, credentials, or destructive-action boundaries;
- reproducibility, observability, or acceptance evidence;
- committed scope or compatibility guarantees.

Private implementation choices that cannot change a protected outcome are not material merely because multiple designs are possible.

## Essence and Project Boundary

The universal implementation model is deliberately small:

```text
effective implementation contract
= Essence
+ Project Boundary
```

The **Essence** owns the material semantics of the component being built: its scope, behavior, domain rules, interfaces, invariants, failure semantics, acceptance evidence, and other implementation choices that belong to that component.

The **Project Boundary** defines what the component may assume is already provided by its environment. Read `project-boundary.md` for the boundary standard.

Typical boundary-owned concerns include existing repository layout, generic build/package/dependency plumbing, test and CI conventions, reusable libraries or frameworks, platform services, and other capabilities whose internal implementation is not this component's responsibility.

The Project Boundary does not need to be a dedicated file. It may already be determinable from stable repository structure, policy, templates, or other durable project authority. It must, however, be explicit enough that an independent implementer can distinguish what this component owns from what it may assume.

Do not duplicate boundary-owned mechanics into the Essence merely to make the Essence look self-contained. Conversely, do not push component-specific behavior into the Project Boundary to avoid specifying it.

An Essence may be physically split into multiple referenced normative files when that improves readability, for example a large formula appendix. Such files remain parts of **one Essence contract**. This skill does not introduce a generic `Dedicated Contract` category.

### Specification pressure and responsibility boundaries

Specification pressure is architectural evidence, not automatic proof of bad design.

If making the Essence complete appears to require specifying a substantial, self-contained capability with its own reusable purpose or lifecycle, first ask whether that capability is actually this component's responsibility.

- If not, prefer extracting or using that capability behind the Project Boundary and specify only the interaction this component relies on.
- If the owner intentionally keeps the capability in scope and the responsibility remains coherent, its material semantics stay inside the Essence contract, even if the Essence is physically split across files.
- Do not create a new companion-spec category merely to absorb complexity.

A large specification by itself is not a formal finding. A finding exists only when scope, ownership, or material behavior remains ambiguous enough to permit materially different outcomes.

## Authority

The Essence must state or make determinable:

- what scope it governs;
- what it explicitly does not govern;
- what Project Boundary it assumes;
- which referenced normative files, if any, are physically part of the same Essence contract;
- how conflicts inside the effective implementation contract are resolved.

The frozen Essence is normative implementation authority for the component it owns. The established Project Boundary remains authoritative for boundary-owned concerns.

Audit journals, raw Auditor findings, reconciliation records, remediation history, prompts, and the originating conversation are provenance or workflow evidence. They must not contain missing normative requirements that an implementer needs in order to reconstruct the effective implementation contract.

Do not duplicate long derivations or design documents merely for completeness. If implementation-critical material belongs to the component, make it part of the Essence contract directly or through a referenced normative section/file. If it belongs to another component or reusable capability, place that responsibility behind the Project Boundary rather than inventing a new companion-contract taxonomy.

## Completeness dimensions

An Essence has no mandatory chapter template. Its structure should fit the problem domain.

Before freeze, however, evaluate every applicable dimension below. Omit a dimension only when it is genuinely non-material or out of scope.

### Purpose, scope, naming, and exclusions

Define the intended result, supported use cases, canonical terms, scope boundary, and explicit non-goals. Do not describe future extensions as already supported.

### Terminology and invariants

Define material domain terms and invariants once. Include any applicable conservation/accounting, ordering, determinism, state-transition, ownership, security, or idempotency guarantees.

### Architecture, ownership, and dependency direction

For material boundaries, make clear who owns each abstraction, which layer may depend on which, what must not cross a boundary, and who owns construction, lifetime, parsing, normalization, validation, caching, persistence, execution, serialization, or reporting when those choices matter.

### Normative implementation surface

Identify the files, modules, interfaces, schemas, build/package surfaces, workflows, or generated artifacts whose shape is itself part of the contract when materially different project structures would affect the protected outcome.

A file manifest is not required when file placement is immaterial.

### Public and cross-layer contracts

For each material interface or message, define applicable names/signatures, required fields, types, shapes, units, coordinate or time conventions, defaults, ordering, determinism, mutability, ownership, invalid-input behavior, failure behavior, and compatibility/versioning rules.

Examples do not replace contracts.

### Inputs, provenance, and parameter roles

Give each material input one clear role and owner. As applicable distinguish product/input terms, external observations, fixed assumptions, calibrated or optimized variables, numerical configuration, policy axes, persisted state, and derived quantities.

Specify material source, normalization, units/domain, coverage/order/identity, fallback policy, and reproducibility identity where relevant.

A parameter must not silently migrate between roles.

### Algorithm and numerical contract

When numerical behavior matters, define the executable leaves that can materially change results: equations or algorithm steps, state/measure/coordinate conventions, discretization, grids/events, quadrature, normalization, retained dimensions, root solving, tolerances, stopping rules, degenerate branches, covariance/factorization policy, random seeds, exceptional floating-point behavior, convergence axes, and performance constraints where applicable.

Naming a library, solver, model family, or algorithm is insufficient when materially different subchoices remain.

### State, persistence, concurrency, and recovery

If state exists, define applicable authority, schema/version identity, cache keys and invalidation, restart/recovery, concurrency assumptions, atomicity, stale-state handling, idempotency, deduplication, and reconciliation after partial or unknown external outcomes.

### External providers and adapters

Where external services or providers exist, define the project-owned abstraction and applicable adapter responsibilities, dependency/version policy, connection/session ownership, authentication, timeout/retry/backoff, rate limits, reconnect behavior, idempotency, reconciliation, and fail-open/fail-closed semantics.

### Failure semantics and unsupported cases

Enumerate material failure classes and required behavior. State whether to reject, retry, degrade, return partial output, persist diagnostics, reconcile, stop, or fail closed.

Do not silently clamp, clip, skip, extrapolate, renormalize, substitute plausible values, or fall back to another method unless that behavior is explicitly authorized.

### Security and authority

When applicable, define secret classes and allowed storage, credential access, least privilege, production/test separation, trusted boundaries, destructive-action authority, and redaction/logging rules. Never place secret values in the Essence.

### Observability and reproducibility

Define metadata needed to reproduce, reconcile, or diagnose material behavior, such as repository SHA, data/source version, configuration/policy version, timestamps/as-of semantics, run IDs, model/algorithm version, external operation IDs, status, and failure reason.

### Acceptance evidence

Acceptance criteria must be executable or objectively checkable when the behavior is material.

Cover applicable happy paths, boundary/degenerate cases, invalid input, failure/recovery, determinism, reproducibility, integration boundaries, cross-language agreement, numerical convergence, regression-sensitive invariants, and authority/security failures.

`Works correctly` is not an acceptance criterion.

### Implementation phases and gates

When implementation is staged, define each materially meaningful capability, dependencies, evidence needed to proceed, and whether a gate establishes implementation readiness, scientific validity, or production readiness.

The next implementation step must be identifiable without reconstructing the originating conversation.

## Draft versus frozen

A draft Essence may contain explicit unresolved items.

A frozen Essence may not leave an unresolved material choice that forces the implementer to decide owner-level scientific, product, public-interface, security, architecture, or scope intent.

An unresolved item requires owner decision only when current durable authority neither determines nor explicitly delegates the answer and multiple materially different reasonable choices remain.

## Author/remediator self-check

Before formal audit, simulate implementation phase by phase and ask:

> If implementation started now, what material choice would still have to be invented because neither the Essence nor the established Project Boundary determines it?

Every surviving material answer is a contract gap.

Self-check improves the candidate but never grants freeze authority.

## Relationship to formal audit

This reference defines what an Essence is and what implementation-ready means.

The formal convergence protocol determines how independent Auditors, reconciliation, remediation, owner decisions, and exact-target freeze establish that the candidate satisfies this standard.

A formal PASS applies only to the exact audited authority state.
