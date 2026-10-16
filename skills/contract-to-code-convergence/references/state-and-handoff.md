# State and handoff — draft protocol

## Authority and journal

Resolve the Target Essence from an explicit owner path, or automatically only if exactly one unambiguous FROZEN / IMPLEMENTATION_READY Essence exists at the pinned baseline. Validate an explicit path's existence, frozen status and provenance; an invalid explicit path is BLOCKED, with no fallback discovery. Count referenced normative parts as one Essence; filenames, quoted status words and archived copies alone do not establish current frozen authority. Ask the owner when multiple candidates exist (WAITING_FOR_OWNER); stop when none exists (BLOCKED).

Persist selected path, baseline commit, Essence blob SHA, discovery evidence and selection reason, Project Boundary and normative-part identities, and governing Skill revision SHA before delegation. A durable journal also contains stage, role identity, branch/PR, sealed acceptance manifest hash, independent test-asset hashes and adapter status, candidate HEAD SHA, CI run SHA, findings IDs, remediation commits, owner decision IDs, and merge policy.

Roles: Dispatcher (state and input validation), Acceptance Analyst (pre-code independent criteria), Implementer, Independent Reviewer/Remediator, fresh Final Verifier. One worker may hold reviewer and remediator roles; no worker may verify its own remediation as Final Verifier.

Only transition to ACCEPTANCE_SEALED after manifest and feasible pre-code test assets are independently read back and their hashes recorded, with deferred adapter work explicitly listed. Only transition to REVIEWING after implementation HEAD readback. A remediation invalidates prior candidate-SHA-specific evidence; rerun impacted checks and rebind final verification. Any post-seal change to acceptance tests or oracles requires an independently approved, versioned correction with evidence and hashes. Final-verifier supplemental cases and expected results must be recorded before candidate outputs are examined. A final verifier must independently inspect evidence and cannot accept status labels from the prior agent as proof.

## Durable evidence and isolation

For each material gate, index the role, candidate SHA (or baseline SHA before implementation), command/check, exit status or inspection outcome, durable evidence location, SHA256 digest when applicable, and retention/availability limitations. Retain critical command outputs, assertions and inspection results needed to substantiate the gate, not just a success label. Read back retained evidence and verify its identity and applicable digest before counting it. A hash or unavailable link alone is not retained evidence. If evidence is missing, expired or mismatched, mark the affected gate incomplete and rerun or recover it before VERIFIED; never infer a pass from the index alone. Later evidence must not retroactively claim that acceptance was sealed before implementation: an unprovable pre-code seal is BLOCKED until its original provenance is recovered.

For each worker, record the role/execution identity, achieved isolation level, mechanism, delivered inputs and limitations. Distinguish fresh-context only, controlled-input delivery and enforced tool-access isolation. Fresh context does not prove input filtering; checked input delivery does not restrict inherited tools. Prompts alone do not enforce tool access. Never claim a stronger level than demonstrated. If the required isolation level is unavailable, fail the compatibility gate; reporting a limitation does not waive the requirement.

## Interruption recovery

If interrupted, load the journal and revalidate selected path, pinned baseline commit, Essence blob and referenced authority identities, governing Skill revision, acceptance seal and asset hashes, current candidate/CI SHAs, findings and merge policy. Validate authority at the recorded baseline separately from the current candidate; implementation commits need not equal the baseline. Never silently select a new target or adopt a newer Skill revision. Resume the first incomplete stage only after readback. Divergent or missing state is BLOCKED until reconciled; a prior agent summary or terminal-state label is not proof. A moved candidate invalidates prior candidate-SHA-specific evidence; rerun impacted checks and rebind final verification. Persist owner decisions with stable IDs and exact option meaning; never silently reinterpret partial responses.

The GitHub backend may use Issues/PR comments/checks and retained artifacts as durable transport; ephemeral scratch paths alone are insufficient. The local backend may use tracked or untracked durable files plus git. Do not require the first skill's exact Issue schema: reuse proven transport where appropriate, but keep the second skill self-contained.

Exit states: VERIFIED (all acceptance criteria evidenced, no blockers, exact candidate SHA); MERGED (VERIFIED and authorized merge SHA); WAITING_FOR_OWNER; BLOCKED. Publishing and propagation have independent completion records.
