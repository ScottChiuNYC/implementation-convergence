# Lossless reconciliation, independent verification, and design deliberation

This reference is normative for the Implementation Contract Convergence formal loop. The dispatcher pins the candidate SHA, raw-result seals, worker identities, input manifests and resulting evidence. The backend determines storage only; these semantic gates apply to both GitHub and local runs.

## Lossless reconciliation

The Reconciler maps **every** valid sealed raw finding to one or more atomic semantic obligations, or an explicitly justified nonblocking dismissal. Preserve original finding IDs and exact provenance. Grouping is presentational: groups are not obligations and must not silently resolve or erase distinct requirements.

Classify cross-finding relationships as EQUIVALENT (same material obligation and scope), RELATED (shared topic but distinct obligations), CONFLICTING (incompatible material claims or proposed requirements), or DISTINCT. Record the justification and source IDs for every equivalence, conflict and dismissal. Related findings may share a group but retain separate obligations. Conflicting proposals are not automatically contract contradictions: distinguish findings about actual authority from differing design preferences.

Each obligation receives a stable ID, source finding IDs, exact semantic requirement, disposition (already satisfied, nonblocking with rationale, agent-authorized decision, owner-required decision, or remediation), authority citation, and any dependency/conflict links. Every raw finding must be covered; every obligation must have a disposition. Do not turn an agent preference into existing authority.

## Independent reconciliation verification

After the Reconciler seals its output, launch a **fresh verifier distinct from the Reconciler, Auditors and Remediator**. Supply checked current authority, the complete sealed raw finding set and the sealed reconciliation; do not supply earlier private deliberation or historical worker reasoning. The verifier independently checks full raw-to-obligation coverage, equivalence validity, semantic preservation, classification, dismissals, authority, conflicting claims, and disposition consistency.

Seal a PASS or FAIL report with specific finding/obligation IDs and counterexamples. On FAIL, the Reconciler may repair the reconciliation from the same immutable raw findings; a fresh verifier must check the revised sealed reconciliation. Do not alter sealed Auditor outputs. If the same semantic defect persists after two repairs, stop with an execution blocker instead of looping or silently passing. No downstream decision or PASS transition is permitted before verified reconciliation.

## Bounded multi-agent design deliberation

For **every material proposed agent-authorized decision** and **every owner-required decision packet**, obtain three independent initial assessments in fresh contexts, with checked current authority, verified obligations, constraints and alternatives; do not show sibling assessments before each is sealed. Assess feasibility, pros, cons, downstream effects, scope/authority, recommendation and whether owner authority is required.

When initial assessments materially disagree, allow **one** structured cross-challenge round, showing sealed positions and requiring evidence-based responses. When they agree, record agreement without a redundant challenge. A fresh moderator synthesizes the arguments, preserves material minority objections and unresolved uncertainty, and recommends a disposition. The moderator cannot grant owner authority, override prior owner decisions, or turn a vote into proof. The dispatcher validates the synthesis against verified obligations and current authority.

Deliberation may cover related obligations together, but every obligation retains its ID and disposition. The resulting record includes independent positions, challenge outcomes where applicable, alternatives, dissent, recommendation, owner/agent authority rationale and links to the original findings. Minor editorial corrections or mechanically dictated changes with no material choice do not require three-way deliberation; record the non-material classification and justification.

Owner-required items are presented in conversation using existing stable D-IDs, A/B/C labels, tradeoffs and advisory recommendation; deliberation never substitutes for the owner's selection. Agent-authorized decisions can proceed without owner intervention only when within explicit authority. Preserve alternative letter-to-meaning mappings across interruption and resume.

## Durability and recovery

Seal the raw mapping, verifier verdict, individual deliberator assessments, challenge record, moderator synthesis and final dispositions with candidate SHA, input manifest, worker identities and evidence links/hashes. On restart, read back and validate each seal before resuming at the first incomplete gate. Do not renumber existing IDs, infer owner answers, silently skip missing evidence, or expose sibling Auditor findings before their seals.

## Regression obligations

Test at least: equivalent duplicates; related refinement/coarsening/hysteresis obligations; conflicts versus alternative preferences; unmapped findings; incorrect dismissal; unauthorized agent resolution; verifier rejection and repair; repeated-failure stop; independent initial positions; disagreement challenge; preserved dissent; owner veto of unanimous advice; no needless owner escalation; stable IDs and partial owner response; interrupted resume; local and GitHub durable state. Static protocol tests alone do not establish runtime worker isolation or E2E recovery.
