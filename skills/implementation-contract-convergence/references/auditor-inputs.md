# Auditor Input Boundary

The dispatcher prepares and verifies inputs before launching any Auditor. Verification belongs to the dispatcher, not the Auditor. Dispatcher and Reconciler contexts may access execution history; Auditor contexts may not.

## Prepare once per target

1. Verify the immutable commit and tree identities through the selected backend.
2. Explicitly allowlist the complete current Essence (including its normative file closure), relevant Project Boundary, and generic Auditor instructions and shared contract standards. Inspect their content: a path or role label alone does not establish permission.
3. Read repository authority at the exact target, verify file/blob identities against that tree, and record content digests. Pin the skill instructions separately to the skill version used for the run.
4. Project a clean input packet containing only run/round/slot/execution identities, target and scope, the approved manifest, file contents and digests, and isolation provenance. Keep verification responses and execution history in dispatcher-only state.
5. Inspect the final serialized packet before delivery. All slots receive the same authority material and scope; only assignment and execution identities differ. Record the packet digest with each assignment.

Forbidden inputs include prior or sibling Auditor verdicts/findings, remediation reports and repair claims, reconciliation history, audit journals, owner-decision history, parent conversation history, full commit/PR patches, commit messages, control Issue bodies, and CI narratives. Current owner resolutions must already be incorporated into current normative authority; do not supply the decision discussion to Auditors. A normative reference to forbidden history is a hidden-authority problem, not permission to read it.

Pass contents, not instructions to browse the repository. Links do not authorize further reads. Repository-wide instructions must be reviewed and reduced to applicable permitted authority; if the host automatically injects forbidden material, the context is invalid.

The optional `scripts/auditor_packet.py` helper positively projects a dispatcher-reviewed manifest and verifies content hashes. It performs no network requests or orchestration. It cannot decide whether text is semantically permitted or prove tree membership; the dispatcher must do both. Without Python, perform the same projection, identity checks and digest recording manually. Do not forward raw tool responses as a substitute.

Helper usage (dispatcher context only):

    python scripts/auditor_packet.py < dispatcher-input.json > auditor-packet.json

Its input object contains `assignment` (string fields `run`, `round`, `slot`, `execution`, `scope`), `target` (`backend`: `github` or `local`, `commit_sha`, `tree_sha`), `verified_commit` (normalized `sha` and `tree.sha`), `allowlist` (path to `essence`, `boundary`, or `instruction` role), `files` (objects with `path`, UTF-8 `content`, `blob_sha`), and `isolation` (`host_enforced` or `delivery_only`). The dispatcher supplies verified identities; instruction blobs may come from the separately pinned skill version. Output includes a canonical `packet_sha256` and per-file `content_sha256`. Unexpected response fields are discarded; missing, duplicate or unallowlisted files and mismatched identities are rejected.

The optional `validate_result(packet, result)` function checks structured new records using `assignment`, `target`, `packet_sha256`, `status: SEALED`, `validity`, boolean `exposure`, `verdict` and `findings`. It returns false for a correctly formed INVALID record and rejects a contaminated valid verdict or substantive/advisory invalid review. It does not inspect free-text summaries for disguised findings, decide semantic validity, or orchestrate recovery. The dispatcher and Reconciler still apply the protocol to actual records, including legacy formats.

## Launch and additional input

Launch a new worker with no inherited conversation, prior run context, or previous worker memory. Supply only the packet and the minimal kickoff from auditor.md. Inline delivery is preferred; a designated packet file may be read solely to load those delivered contents, without browsing its directory. Disable or restrict repository/network/filesystem tools to the allowlist when the host supports it. Do not fork the dispatcher conversation into an Auditor.

The Auditor must not verify GitHub commits, open result/control Issues, inspect git history, read runtime directories, or fetch repository files itself. If necessary authority is missing, request it from the dispatcher without following links. The dispatcher reviews any requested material at the same immutable target. If it changes the input manifest, retire the current executions and rebind all slots with the same expanded packet before accepting results; never silently change scope or mix input sets.

The dispatcher mechanically persists and reads back results. Persistence responses stay outside Auditor contexts.

## Isolation claims

Fresh context and filtered delivery provide context separation, not an access-control sandbox. Record either `host_enforced` (describe the actual tool/file restrictions) or `delivery_only` (the worker retains broader access but is instructed to use only delivered inputs). Never claim that prompt restrictions enforce tool isolation.

For example, [OpenAI's subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents) describes inherited permissions/tools and says custom instructions do not create a separate read-only sandbox; ChatGPT Work workers use tools available to the parent chat. Check the actual host rather than assuming a product name establishes isolation.

Delivery-only mode is a practical safeguard when fresh contexts and controlled input delivery can be established, with this limitation disclosed. It does not certify absence of undisclosed reads. If required isolation cannot be established, or the owner/repository requires strict enforced isolation unavailable on the host, the existing compatibility gate fails closed: no formal PASS or freeze. This is a capability check, not a new owner approval gate between stages.

## Exposure and replacement

Any delivery or read of forbidden material, including incidental tool-output spill, invalidates that execution. Stop immediately. Seal `validity: INVALID`, `verdict: null`, and an empty substantive findings list. Record only an execution-blocker summary, provenance, packet identity, and a minimal exposure description (tool and forbidden path/category, not copied history). Do not complete the review, return an advisory verdict, or reuse observations from it.

The dispatcher preserves the immutable invalid record, records its exclusion, and retries the **same logical slot**, target and scope with a new execution ID, new result locator, fresh context, and clean packet. Keep slot count fixed. Never send the invalid execution's observations or exposure details to the replacement. No additional owner approval is needed for this recovery.

Reconciliation waits for one valid sealed execution per configured slot with matching target/scope/input manifest. Exclude all invalid executions even if they contain a PASS, FAIL, or apparent zero-findings review. Preserve historical legacy records without editing them; mark exclusions in current coordinator/reconciliation state. If the unsafe delivery mechanism cannot be corrected, block instead of repeatedly launching contaminated replacements.
