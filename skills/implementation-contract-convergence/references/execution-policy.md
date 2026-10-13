# Execution Policy

## Exact target

Every formal round binds all Auditor slots to the same immutable candidate identity.

Prefer an exact git commit SHA when the Essence lives in a repository. Otherwise use the strongest immutable snapshot identity available.

A PASS is valid only for that exact authority state.

## Auditor independence

Use fresh independent worker contexts when the environment supports them.

Default formal configuration: three Auditor slots.

The owner or repository policy may explicitly choose another fixed configuration before the round begins. Do not change the slot count or composition after seeing findings.

A root agent must not leak sibling findings into an Auditor before that Auditor seals its result.

## Reconciler and Remediator freshness

Use a fresh Reconciler after all required Auditor results are sealed.

Use a separate Remediator after reconciliation.

The root agent coordinates transitions; it does not silently replace these roles with its own conclusions.

## Provenance

Record the strongest execution provenance the environment exposes, such as executor/runtime, model identity, or reasoning setting.

If the owner explicitly requires a particular model, executor, or reasoning policy and compliance cannot be established, fail closed as an execution blocker.

Do not invent provenance that the platform does not expose.

## Capability failure

If fresh independent workers are unavailable, do not claim a formal multi-Auditor PASS.

You may perform an advisory review if useful, but label it non-formal and stop before freeze unless the owner explicitly changes the policy.

Operational failure is not a substantive contract finding.

## Round integrity

Complete all configured Auditor slots before reconciliation.

Do not terminate a round early because one Auditor found an owner decision.

Do not silently substitute a new target after the round starts.
