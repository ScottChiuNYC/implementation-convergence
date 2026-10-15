# State and handoff — draft protocol

Record the run and exact authority/baseline SHAs before delegation. A durable journal contains stage, role identity, branch/PR, sealed acceptance manifest hash, candidate HEAD SHA, CI run SHA, findings IDs, remediation commits, owner decision IDs, and merge policy.

Roles: Dispatcher (state and input validation), Acceptance Analyst (pre-code independent criteria), Implementer, Independent Reviewer/Remediator, fresh Final Verifier. One worker may hold reviewer and remediator roles; no worker may verify its own remediation as Final Verifier.

Only transition to ACCEPTANCE_SEALED after acceptance manifest readback. Only transition to REVIEWING after implementation HEAD readback. A remediation invalidates prior candidate-SHA-specific evidence; rerun impacted checks and rebind final verification. A final verifier must independently inspect evidence and cannot accept status labels from the prior agent as proof.

If interrupted, load journal, verify current remote/local SHAs and artifacts, and resume the first incomplete stage. Divergent or missing state is BLOCKED until reconciled. Persist owner decisions with stable IDs and exact option meaning; never silently reinterpret partial responses.

The GitHub backend may use Issues/PR comments/checks as durable transport. The local backend may use tracked or untracked durable files plus git. Do not require the first skill's exact Issue schema: reuse proven transport where appropriate, but keep the second skill self-contained.

Exit states: VERIFIED (all acceptance criteria evidenced, no blockers, exact candidate SHA); MERGED (VERIFIED and authorized merge SHA); WAITING_FOR_OWNER; BLOCKED. Publishing and propagation have independent completion records.
