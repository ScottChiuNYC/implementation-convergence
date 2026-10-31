---
name: implementation-contract-convergence
description: Manually invoked workflow that converges free-form implementation intent or a draft Essence into a frozen, unambiguous implementation contract through semantic coverage checking, independent audits, reconciliation, bounded remediation, and narrow owner escalation.
compatibility: Requires a host that can launch fresh isolated subagents or workers and provide durable shared run state. Local backend also requires persistent filesystem read/write and git; GitHub backend requires repository, Issue, branch, PR, and exact-SHA read/write and readback capabilities.
---

# Implementation Contract Convergence

Converge implementation intent into a standalone frozen contract that an independent implementer can execute without making a material product, model, or architecture decision on the owner's behalf.

The contract may intentionally leave implementation freedom when all allowed choices are materially equivalent.

## Activation boundary

This is a human-triggered workflow.

Do not start this skill merely because a conversation or draft appears ready for convergence. Require explicit human invocation: the human must name this skill, use the host's explicit skill command, or otherwise directly instruct the agent to run Implementation Contract Convergence.

OpenAI packaging also sets agents/openai.yaml policy.allow_implicit_invocation to false. Other hosts may provide their own invocation controls; those controls are defense in depth, while this in-skill activation rule remains authoritative.

Once the human starts the skill, the internal audit, reconciliation, remediation, and re-audit loop may proceed autonomously until FROZEN, WAITING_FOR_OWNER, or a fail-closed blocker.

Subagents spawned inside the workflow are role workers. They do not recursively invoke this skill.

## Compatibility gate

Before doing any formal convergence work, verify that the host can satisfy all hard requirements:

1. launch the configured number of fresh, sufficiently isolated Auditor workers;
2. keep sibling Auditor findings hidden from one another until each result is sealed;
3. launch a fresh Reconciler and a separate Remediator when required;
4. provide durable shared run state through one selected backend so a fresh coordinator can reconstruct the run after interruption;
5. bind every formal round to an immutable target identity.

Read `references/auditor-inputs.md` before launching workers. Establish fresh contexts without inherited conversation and dispatcher-controlled allowlisted delivery. Record whether isolation is host-enforced or delivery-only; prompts alone do not enforce access restrictions. Apply the documented fail-closed rule when required isolation is unavailable.

If any hard requirement is unavailable or cannot be established, stop with an incompatible-host or execution blocker. Do not simulate independent Auditors in one shared context, do not claim formal PASS, and do not freeze the Essence.

An incompatible host may still help draft an Essence or perform an advisory review outside this formal skill.

## Inputs

For repository-scoped invocation, require an explicit **Target Essence repository-relative path** as well as the Target Repository. Resolve and read that exact path at a pinned commit SHA, and record both path and SHA in durable run identity. Do not silently select a different Essence or expand scope to sibling Essences. If the path is omitted, ask the owner to identify it before formal work (even if only one candidate currently exists); do not infer from filenames or version labels. For free-form conversation-to-new-Essence work, obtain an explicit destination path before creating the repository artifact. Incremental revisions to the same responsibility may reopen its Essence rather than create a new one.


Accept any of these starting points:

- a free-form design conversation or notes;
- an existing draft Essence;
- a draft Essence plus conversation or other owner-designated source material.

Use current owner instructions and current repository authority. Do not silently import stale chat history or legacy protocol as authority.

The effective implementation contract must be reconstructible from durable repository authority without hidden conversation context. It consists of the Essence plus the established Project Boundary.

Before drafting, semantic coverage, remediation, or formal audit, read:

- `references/essence.md` — what the Essence owns and what implementation-ready means;
- `references/project-boundary.md` — what the component may assume is already provided and how to keep boundary-owned mechanics out of Essence scope;
- `references/incremental-development.md` — whether an incremental change needs no contract change, reopening an existing Essence, or a new Essence.

## Style of generated code and interfaces

When creating code-like material (C++/Python interfaces, class declarations, executable examples or client code), follow the target project's durable coding policy as part of its Project Boundary. No automatic formatter or formatter-only CI is implied; avoid irrelevant reformatting. Cosmetic style alone is not a material ICC finding and must not change domain semantics or published interfaces.

## Entry: classify, draft, and check semantic coverage

Before drafting or auditing, identify the Project Boundary from current durable repository authority.

For incremental work on an existing project, first classify the change using `references/incremental-development.md`. Do not create a new Essence merely because a new milestone, feature, or release has started.

If no Essence exists, draft the initial Essence from the available design context while keeping boundary-owned mechanics outside its responsibility.

If an Essence exists and the current conversation or owner-designated notes contain relevant decisions, compare them before formal audit.

Read references/semantic-coverage.md and perform both directions:

1. source -> Essence: every material decision, constraint, assumption, non-goal, and unresolved choice from the source is represented faithfully;
2. Essence -> source: the Essence does not invent a material decision that the source did not establish.

Repair ordinary omissions or distortions before formal audit. Preserve genuine unresolved choices as unresolved; do not guess.

## No unauthorized material acceptance commitments

Convergence may clarify and verify existing requirements; it must not silently create new material product or numerical promises. Trace each material acceptance obligation to (a) explicit current Owner/repository authority, (b) an explicitly delegated material choice within its bounds, or (c) a mathematical consequence rigorously derived from that authority under stated assumptions. Generic permission to fill implementation details is not permission to invent new scientific accuracy or performance targets.

Auditors and the Remediator may propose mathematical identities, derivations, proof obligations, and objectively checkable verification methods for already-authorized behavior. A mathematical claim must state its domain, assumptions and exact-arithmetic versus floating-point interpretation. A theorem about asymptotic convergence does **not** entail any arbitrary finite-grid observed-order threshold.

Do not turn an agent-invented empirical numerical gate into mandatory Frozen acceptance without explicit Owner authority or rigorous entailment: examples include benchmark-specific error cutoffs, observed convergence-rate tolerances, interpolation/transfer budget fractions, efficiency ratios, performance floors, and arbitrary floating-point comparison thresholds. Do not relabel a new substantive commitment as a mere test, estimator, or implementation detail. Unsupported proposed gates may be recorded as non-normative research suggestions, never as hidden must-pass conditions.

If a new material acceptance decision is necessary and is neither already authorized nor rigorously entailed, escalate it via the existing Owner Decision protocol; do not default to a numerical threshold. Mathematical consistency review belongs here. Implementation-dependent numerical experiments, numerical regression studies and dynamic feasibility prototypes belong to Contract-to-Code Convergence after freeze; no new ICC execution stage or subagent is implied. C2C may independently derive tests to verify the **existing** Frozen Contract, but such tests cannot amend it.
## Select durable backend

Before the first formal round:

1. read references/state-model.md;
2. read references/backend-selection.md;
3. select exactly one backend for the run;
4. load only the selected backend reference:
   - local: references/backend-local.md
   - GitHub: references/backend-github.md

The backend controls durable transport and integration mechanics only. It does not change audit semantics, role authority, or the definition of PASS.

## Formal convergence loop

When the candidate Essence is ready for formal audit:

1. establish the exact candidate Essence, declared audit scope, its Project Boundary, and the repository or workspace authority being audited;
2. create or update durable run state and the human-readable audit journal;
3. have the dispatcher verify the target and prepare checked, allowlisted input packets, then launch fresh independent Auditor slots without inherited conversation;
4. durably seal raw results; invalidate contaminated executions and retry the same logical slot in a fresh context without reusing observations;
5. after every required slot has a valid sealed result for the same target, scope and input manifest, run a fresh Reconciler;
6. durably persist the canonical reconciliation;
7. follow exactly one transition:
   - PASS -> FREEZE
   - FAIL + no owner decision -> REMEDIATE -> fresh audit
   - FAIL + owner decision -> WAITING_FOR_OWNER
8. after remediation, establish a new immutable target and audit it from scratch;
9. stop only at verified FROZEN, WAITING_FOR_OWNER, or a fail-closed execution blocker.

Use references/execution-policy.md for independence and target rules.

## Role boundaries

`references/essence.md` and `references/project-boundary.md` are the shared contract-definition standards for drafting, remediation, and audit.

Load the role reference only when that role is active:

- Auditor: references/auditor.md
- Reconciler: references/reconciler.md
- Remediator: references/remediator.md
- Freeze and owner handoff: references/freeze-and-handoff.md

The coordinating or root agent owns workflow transitions, target verification, Auditor input delivery, and durable bookkeeping. It must not substitute its own substantive judgment for an Auditor, Reconciler, or owner decision. Auditors receive only permitted current authority and generic audit instructions, never execution history or unfiltered backend responses.

## What counts as a blocker

A formal finding must be capable of changing a materially protected implementation outcome.

Typical blockers include:

- contradictory normative requirements;
- an unclear Project Boundary that leaves ownership or assumed capabilities materially ambiguous;
- missing behavior that forces the implementer to choose among materially different outcomes;
- ambiguous scope, state transition, interface, numerical convention, error behavior, data ownership, or acceptance condition;
- an unstated assumption whose alternatives materially change implementation;
- a requirement that cannot be reconstructed from durable authority.

These are not blockers by themselves:

- prose style;
- naming taste;
- unspecified private code shape;
- implementation freedom where compliant choices are materially equivalent;
- missing internal detail that is already unambiguously owned by the established Project Boundary;
- a reviewer's preference for additional explanation that does not affect implementation behavior.

## Owner barrier

Do not ask the owner merely because an Auditor raised a question.

First complete the full audit round and reconciliation.

Escalate only when canonical reconciliation establishes that current authority cannot determine a material choice. Present the smallest decision packet needed to unblock convergence **directly in the owner-facing conversation**, with stable decision IDs, A/B/C-labeled alternatives and descriptive names, concise pros/cons, and an advisory recommendation with rationale (or an explicit reason no recommendation is justified). A durable backend link supplements but never replaces the conversational packet. Accept owner replies by decision ID and letter, persist their meaning, and resume without redundant approval gates. Follow `references/freeze-and-handoff.md`. Do not continue authoritative remediation across an unresolved owner decision.

## Freeze rule

A reconciled PASS authorizes freeze only for the exact audited authority state and declared audit scope.

Freeze writeback is mechanical. It may mark status, record provenance, and update the audit journal, but it must not change substantive contract meaning.

If substantive wording must change, reopen the candidate and run a fresh audit.

Read references/freeze-and-handoff.md before freezing.

## Progress guard

Do not loop forever.

If materially the same canonical blocker survives two consecutive remediation attempts, diagnose whether the cause is:

- a missing owner decision;
- an execution or tooling limitation;
- remediation that failed to implement the canonical finding.

Then stop at the appropriate durable boundary rather than repeating the same round indefinitely.

## Output

Success means all of the following are true:

- the Essence is explicitly frozen or implementation-ready;
- the latest formal round is reconciled PASS;
- the freeze corresponds to the exact audited authority state;
- there are no unresolved owner decisions;
- durable backend state and the audit journal preserve enough provenance to reconstruct the convergence history;
- the frozen Essence identifies its responsibility and Project Boundary clearly enough that the effective implementation contract is reconstructible by the next stage.

Audit history is provenance, not hidden implementation authority.

## Not this skill

Do not implement the frozen contract here.

Code generation, acceptance-test derivation, implementation, implementation remediation, and contract-to-code conformance belong to the separate Contract-to-Code Convergence skill.
