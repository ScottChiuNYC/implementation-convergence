# Project Boundary

## Definition

The Project Boundary defines what the implementation scope may assume is already provided by its durable environment.

It exists to keep an Essence focused on the responsibility of the component being built rather than forcing every Essence to re-specify the surrounding repository, toolchain, platform, or reusable dependencies.

The universal model is:

```text
effective implementation contract
= Essence
+ Project Boundary
```

The Project Boundary is a responsibility boundary, not necessarily a separate document.

## What may belong behind the boundary

Depending on the project, the boundary may already provide:

- repository layout and source/test locations;
- generic build, package, dependency, binding, and CI conventions;
- reusable numerical or infrastructure libraries;
- framework or platform services;
- logging, storage, messaging, broker, database, or other shared adapters;
- organization-wide policies or interfaces that this component consumes but does not own.

These are examples, not mandatory categories.

A mature repository may make its boundary obvious through existing structure and policy. A generated project may use an explicit skeleton contract. Both are valid if an independent implementer can reconstruct the same boundary from durable authority.

## Boundary test

Before drafting or auditing an Essence, ask:

1. What does this component own?
2. What may it assume is already provided?
3. Is that division durably reconstructible without the originating conversation?
4. Are the interactions across the boundary specified enough for this component to be implemented correctly?

If the answer to the third or fourth question is no and the ambiguity can change a material outcome, the boundary is not ready for formal freeze.

## Audit rule

Do not raise an Essence finding merely because it omits internal mechanics already fixed by the Project Boundary.

For a boundary-owned dependency, audit only what this component materially relies on: the interface, capability, version or behavioral assumption, failure expectation, ownership, or other interaction that affects this component.

Do not audit the dependency's internal implementation as though it were part of the current Essence.

The Project Boundary is not a dumping ground. A component-specific domain rule, algorithm, public behavior, failure policy, or other material responsibility cannot be moved outside the Essence merely to make the Essence shorter.

## Specification pressure and single responsibility

Specification pressure is architectural evidence, not proof.

When making an Essence complete appears to require specifying a substantial, self-contained capability with its own reusable purpose or lifecycle, do not automatically create a new companion or dedicated contract.

First ask whether that capability should be a separate component or library behind the Project Boundary.

- If yes, extract or reuse that responsibility and let the Essence specify only the interaction it depends on.
- If no, and the owner intentionally keeps the capability inside this component, its material semantics remain part of the Essence contract.
- A large or technically detailed Essence is not itself a formal defect when the responsibility is coherent.

A formal finding exists only when the current ownership or boundary ambiguity can produce materially different compliant implementations or other protected outcomes.

## Physical decomposition of Essence

A complex Essence may be split across multiple normative files for readability.

For example, a domain-specific mathematical component may keep a large formula appendix in a separate file. If the root Essence explicitly identifies that file as part of the same normative Essence contract, this is document decomposition rather than a new architectural contract type.

The skill deliberately does not define a generic `Dedicated Contract` category.

## Durability

The Project Boundary must be available from durable repository or workspace authority for the exact audited target.

Hidden chat assumptions, remembered local conventions, ambient packages, or an agent's private knowledge do not establish the boundary.

If a required boundary capability is absent, ambiguous, or available only accidentally in one executor environment, stop and repair the durable project authority before freeze.

## Coding conventions in the Project Boundary

When the target repository declares coding conventions, such as Google C++ Style or PEP 8, these are project-local implementation policies. ICC follows them for compilable examples, client code and API declarations without restating them in every Essence. Style is not a new domain requirement, does not by itself block freeze, and must not silently alter public compatibility. Formatter enforcement is not implied.
