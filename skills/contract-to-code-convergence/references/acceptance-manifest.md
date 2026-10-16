# Acceptance Manifest — draft protocol

Created and sealed by an independent Acceptance Analyst before implementation begins.

Minimum durable fields:

- run_id, frozen_essence_ref and SHA, project_boundary_ref and SHA, baseline_repo_SHA, acceptance_manifest_SHA
- for each stable AC-ID: requirement reference; observable criterion/invariant; verification type (test, independent oracle, static inspection, artifact/CI); positive, negative and boundary cases; objective threshold if specified by authority; evidence expectation; non-automatable rationale if any
- explicit coverage gaps, material ambiguities, and prohibited behaviors
- analyst identity/role, seal timestamp, content hash

The manifest cannot amend frozen authority. If a criterion is materially unsupported, remove or mark it advisory; do not impose it as a new mandatory requirement. A new manifest version after sealing requires explicit provenance and independent confirmation; never quietly edit it to fit code.

Reviewer output extends the same stable IDs with implementation locations, test IDs, evidence SHAs, pass/fail and outstanding findings. Coverage must be bidirectional. A test that merely executes without asserting an outcome is not acceptance evidence.
