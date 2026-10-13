# Implementation Contract Convergence Tests

This directory is reserved for behavioral fixtures and regression cases for the skill.

The first useful scenarios should cover:

1. free-form conversation -> faithful initial Essence -> semantic coverage;
2. draft with a remediable ambiguity -> FAIL -> remediation -> fresh PASS;
3. draft requiring a genuine owner decision -> WAITING_FOR_OWNER;
4. stylistic or non-material preference -> no formal blocker;
5. substantive change after PASS -> freeze rejected until fresh audit;
6. hidden conversation dependency -> formal blocker;
7. unsupported material invention during drafting -> caught by semantic coverage.

Do not add orchestration infrastructure merely to make these tests look automated. Start with the smallest fixture format that can expose real skill failures.
