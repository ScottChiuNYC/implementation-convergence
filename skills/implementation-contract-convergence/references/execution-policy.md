# Execution Policy

## Exact target

Every formal round binds all Auditor slots to the same immutable candidate identity and the same declared audit scope.

Prefer an exact git commit SHA when the Essence lives in a repository. Otherwise use the strongest immutable snapshot identity available.

The audit scope identifies the responsibility being certified plus any materially affected interfaces and relevant Project Boundary. It may be narrower than the repository, but it must be complete for the material consequences of the change.

A PASS is valid only for that exact authority state and declared audit scope.

## Auditor independence

Use fresh independent worker contexts when the environment supports them.

Default formal configuration: three Auditor slots.

The owner or repository policy may explicitly choose another fixed configuration before the round begins. Do not change the slot count or composition after seeing findings.

A root agent must not leak prior/sibling findings, remediation reasoning or reconciliation history into an Auditor. Follow `auditor-inputs.md`: dispatcher-only backend verification, positively allowlisted delivery, fresh contexts without inherited history, and recorded isolation mode.

Forbidden exposure invalidates the execution immediately: seal INVALID with null verdict, no substantive findings and no advisory review. Preserve its record and retry the same logical slot with a new execution identity and fresh context. Do not transfer observations or change slot count, target or scope. Reconciliation waits for all required valid executions. This operational recovery needs no new owner gate; block if the unsafe delivery cannot be corrected.

## Reconciler and Remediator freshness

Use a fresh Reconciler after all required Auditor results are sealed.

Use a separate Remediator after reconciliation.

The root agent coordinates transitions; it does not silently replace these roles with its own conclusions.

## Provenance

Record the strongest execution provenance the environment exposes, such as executor/runtime, model identity, or reasoning setting.

If the owner explicitly requires a particular model, executor, or reasoning policy and compliance cannot be established, fail closed as an execution blocker.

Do not invent provenance that the platform does not expose.

Record the input manifest and packet digest, dispatcher verification evidence, execution identity, isolation mode and actual restrictions when available. Delivery-only mode is not a tool-level isolation guarantee.

## Capability failure

If fresh independent workers are unavailable, do not claim a formal multi-Auditor PASS.

You may perform an advisory review if useful, but label it non-formal and stop before freeze unless the owner explicitly changes the policy.

Operational failure is not a substantive contract finding.

## Round integrity

Complete all configured Auditor slots with valid sealed executions before reconciliation. Never count an invalid execution's PASS, FAIL or advisory observations.

Do not terminate a round early because one Auditor found an owner decision.

Do not silently substitute a new target or change the declared audit scope after the round starts.
