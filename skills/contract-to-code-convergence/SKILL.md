---
name: contract-to-code-convergence
description: Explicitly invoked workflow to turn a frozen implementation contract into verified code through independent acceptance derivation, implementation, independent review/remediation, and final verification.
compatibility: Requires fresh isolated worker contexts, durable run state, repository read/write and test execution, and exact-commit verification. GitHub backend requires branch/PR/check access; local backend requires durable filesystem and git.
---

# Contract-to-Code Convergence (draft v0.1)

Given a FROZEN / IMPLEMENTATION_READY Essence and its established Project Boundary, converge implementation to demonstrable contract compliance. Do not reinterpret, reopen, or modify the frozen Essence in this skill. The effective authority is **Essence + Project Boundary**, not prior agent reports, hidden conversation, or audit history.

## Invocation and compatibility

Require explicit owner invocation; do not implicitly begin implementation because a contract was frozen. Once invoked, proceed autonomously through the approved run policy. Check for (1) fresh, sufficiently isolated workers, (2) durable shared state and interruption recovery, (3) immutable commit identification, (4) repository modification and build/test capability, and (5) independent verification of CI and artifacts. If any essential capability is absent, fail closed and report the precise blocker. A single agent impersonating three roles is not independent verification.

Use one backend per run: GitHub branches/PRs/checks and durable records, or a persistent local git worktree plus durable records. Ephemeral cloud filesystem alone is not a durable local backend. Backend changes transport, not evidence or authority rules. The host may delegate to native Work/Codex workers; do not construct a custom orchestration runtime without demonstrating a missing native capability.

## Entry and immutable authority

For repository-scoped invocation, require an explicit **Target Essence repository-relative path** as well as the Target Repository. Resolve and read that exact path at a pinned commit SHA, and record both path and SHA in durable run identity. Do not silently select a different Essence or expand scope to sibling Essences. If the path is omitted, ask the owner to identify it before formal work (even if only one candidate currently exists); do not infer from filenames or version labels. For free-form conversation-to-new-Essence work, obtain an explicit destination path before creating the repository artifact. Incremental revisions to the same responsibility may reopen its Essence rather than create a new one.


1. Identify the exact frozen Essence, Project Boundary, repository baseline SHA, declared responsibility, acceptance conditions and prohibited behavior.
2. Check freeze provenance, unresolved owner decisions, material boundary drift and baseline project build. Do not treat a green CI badge for an unrelated SHA as evidence.
3. For an incremental task, constrain the scope to the affected responsibility, interfaces and boundary; do not reconverge unrelated components.
4. Synchronize project scaffolding only if necessary. For Copier, inspect .copier-answers.yml, confirm the intended revision/tag, preserve project files, and verify baseline build *before* domain implementation. Never silently update unrelated infrastructure.
5. Record run identity, source SHAs, roles, stage, findings and evidence locations in durable state.

## Stage A — independent acceptance derivation (before implementation)

Launch an **Acceptance Analyst** in a fresh context with frozen authority and the baseline, **before the Implementer writes code**. Produce a sealed acceptance manifest with stable IDs linking each material requirement to: expected observable behavior/invariant, positive and negative cases, verification method, tolerances or objective pass criteria, and any justified non-automatable inspection. Include boundary and packaging obligations only where authority requires them. Mark unknowns rather than inventing new domain requirements.

Before implementation, the Acceptance Analyst also develops independent executable acceptance assets where feasible: black-box tests, mathematical/reference oracles, fixtures, numerical invariants, and objective assertion logic. Derive these from frozen authority, not existing implementation or prior solution reports. When the implementation API is not prescribed, seal API-neutral oracles and test data plus a thin-adapter specification; do not invent a mandatory API. Tests need not pass before code exists. Public acceptance criteria, thresholds, and normally the test assets are available to the Implementer. No hidden-test infrastructure is required. See references/acceptance-manifest.md.

The dispatcher verifies that the manifest and acceptance assets are derived from current authority, records exact content hashes and durable locations, and makes them available to the Implementer. The Implementer must not unilaterally alter sealed acceptance criteria, test assertions, or oracles to make code pass. A suspected defective test must be documented with a reproducer and independently reviewed; a corrected version receives a new hash and provenance, without changing frozen authority. Acceptance criteria are evidence targets, not a second normative contract; a disagreement with the frozen authority must be resolved in favor of the authority or escalated if materially ambiguous. The Acceptance Analyst may later serve as independent Reviewer **only if** it receives no implementation work or mutable implementer context before the manifest is sealed; use a fresh review context.

## Stage B — implementation

Launch an Implementer using the frozen authority, Project Boundary, and sealed acceptance manifest. Implement complete scope, add meaningful implementation-level unit/integration tests, connect sealed acceptance assets through a minimal transparent adapter where necessary, run the independent public acceptance suite plus canonical build and validation, and open an implementation PR or equivalent local candidate. Do not modify frozen authority, audit history, or acceptance criteria to make tests pass. Preserve source/package boundaries. Record commit SHA, commands, outputs, tests, artifact checks and limitations. Self-reported success is not final evidence.

## Stage C — independent review and remediation

Launch a fresh independent Reviewer with frozen authority, sealed acceptance manifest, implementation diff and reproducible environment. Independently examine mathematical/domain correctness, interfaces, errors, edge cases, tests, false positives, packaging, and unapproved behavior. Construct counterexamples or independent oracles where useful. Produce requirement-to-code-to-test/evidence traceability and severity-ranked findings with locations and reproduction. Check both directions: all requirements implemented, and no material unauthorized additions.

A Remediator may be the Reviewer, but not the original Implementer by default. Fix confirmed findings narrowly, add regressions, and rerun affected plus canonical tests. Every code change creates a new candidate SHA. Re-review changed behavior and impacted requirements. Unresolved material choices go to WAITING_FOR_OWNER with stable decision IDs, labeled alternatives, pros/cons and a recommendation; do not choose on the owner's behalf.

## Stage D — independent final verification

Use a **new fresh Final Verifier**, separate from implementation and remediation. Verify the current candidate SHA, frozen authority unchanged, acceptance traceability complete, prior findings actually fixed, regression effectiveness, CI/checks on the candidate SHA, packaging and downstream consumers when applicable, no blocking review comments or conflicts, and authorized merge policy. Independently rerun focused checks when feasible. The Final Verifier must independently derive and execute or otherwise substantiate additional contract-based counterexamples, test cases, or reference checks beyond merely replaying the Implementer's public suite; choose and record the cases and expected results before inspecting candidate outputs. These checks need not be secret or pre-stored. If execution is impossible, record the specific limitation and strongest alternative evidence; do not claim complete independent verification without adequate evidence. This is an exit-criteria check, not an automatic full fourth audit.

If a blocker is found, return to remediation and reverify the new SHA. If the same substantive blocker persists across two remediation attempts, diagnose and stop at WAITING_FOR_OWNER or BLOCKED instead of looping forever. Never call a run VERIFIED with unresolved material findings or unverified SHA provenance.

## Completion and publication

States: PREFLIGHT -> ACCEPTANCE_SEALED -> IMPLEMENTING -> REVIEWING -> REMEDIATING (loop) -> FINAL_VERIFYING -> VERIFIED; alternatively WAITING_FOR_OWNER or BLOCKED. MERGED is a separate authorized terminal state. Preserve durable state after interruptions and reconstruct from exact commits and sealed evidence before resuming; never infer completion from a prior agent summary.

Default **do not merge** without explicit owner authorization or a predeclared merge policy. When authorized, final verifier may squash merge only after all exit criteria pass; record merge SHA. Publish, PDF generation and downstream propagation are separate opt-in project actions and must not be implied by merge. Report requirement coverage, verified SHA, tests and CI, findings and fixes, limitations, final status and links.

## Non-goals

Do not re-run Implementation Contract Convergence silently, rewrite the Essence, introduce a generic dedicated-contract taxonomy, require arbitrary fixed review rounds, or claim enforced worker isolation based on prompts alone. This draft protocol has not yet passed a full single-invocation E2E test.
