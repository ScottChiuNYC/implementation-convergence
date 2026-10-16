# Acceptance Manifest — draft protocol

Created and sealed by an independent Acceptance Analyst before implementation begins.

Minimum durable fields:

- run_id, frozen_essence_ref and SHA, project_boundary_ref and SHA, baseline_repo_SHA, acceptance_manifest_SHA
- for each stable AC-ID: requirement reference; observable criterion/invariant; verification type (test, independent oracle, static inspection, artifact/CI); positive, negative and boundary cases; objective threshold if specified by authority; evidence expectation; non-automatable rationale if any
- explicit coverage gaps, material ambiguities, and prohibited behaviors
- analyst identity/role, seal timestamp, content hash
- independent acceptance asset IDs, file paths, hashes, executable commands, expected failures before implementation where applicable, and API-neutral oracle/fixture references
- any deferred adapter contract, integration owner, and objective rule for checking that the adapter does not transform outputs or weaken assertions

The manifest cannot amend frozen authority. If a criterion is materially unsupported, remove or mark it advisory; do not impose it as a new mandatory requirement. A new manifest version after sealing requires explicit provenance and independent confirmation; never quietly edit it to fit code.

Before the Implementer begins, the Acceptance Analyst should independently implement executable black-box acceptance tests and reference oracles where the frozen authority permits. Tests target observable contract behavior rather than private implementation structure; some may be unit-level if the API is already fixed. Publish all normative criteria and pass/fail standards, and normally expose tests to the Implementer for iterative development. Do not build hidden-test storage or claim secrecy from prompt instructions. Where APIs are unspecified, seal API-independent oracle logic, fixtures, and a thin adapter specification instead of prescribing new interfaces. The Implementer may add its own tests, but may not silently weaken sealed tests. Any test defect requires independent adjudication, versioned repair and durable hashes.

The Final Verifier must derive additional contract-based cases independently, recording expected outcomes before viewing implementation results. Re-running public tests alone is insufficient.

Reviewer output extends the same stable IDs with implementation locations, test IDs, evidence SHAs, pass/fail and outstanding findings. Coverage must be bidirectional. A test that merely executes without asserting an outcome is not acceptance evidence.
