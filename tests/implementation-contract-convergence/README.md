# Implementation Contract Convergence Tests

This directory is reserved for behavioral fixtures and regression cases for the skill.

The first useful scenarios should cover:

1. free-form conversation -> faithful initial Essence -> semantic coverage;
2. draft with a remediable ambiguity -> FAIL -> remediation -> fresh PASS;
3. draft requiring a genuine owner decision -> WAITING_FOR_OWNER;
4. stylistic or non-material preference -> no formal blocker;
5. substantive change after PASS -> freeze rejected until fresh audit;
6. hidden conversation dependency -> formal blocker;
7. unsupported material invention during drafting -> caught by semantic coverage;
8. owner-configured Auditor slot count -> journal and reconciliation remain slot-neutral;
9. matching conversational intent without explicit invocation -> skill does not start;
10. explicit Codex invocation -> manual-only policy permits the run;
11. explicit Copilot slash invocation -> manual-only policy permits the run;
12. local and GitHub backends represent the same logical round, finding, decision, and freeze semantics;
13. local runtime files remain outside the audited git snapshot;
14. missing fresh isolated workers -> no formal multi-Auditor PASS;
15. backend interruption -> recover from durable state or fail closed without reconstructing raw evidence from memory.

Do not add orchestration infrastructure merely to make these tests look automated. Start with the smallest fixture format that can expose real skill failures.
