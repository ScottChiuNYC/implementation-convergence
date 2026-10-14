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
12. canonical SKILL.md frontmatter remains portable Agent Skills metadata while host-specific invocation controls remain outside the canonical manifest;
13. local and GitHub backends represent the same logical round, finding, decision, and freeze semantics;
14. local runtime files remain outside the audited git snapshot;
15. missing fresh isolated workers -> compatibility gate rejects formal execution and no formal PASS or freeze is possible;
16. shared worker isolation cannot be established -> compatibility gate fails closed;
17. temporary cloud filesystem with unproven durability -> local backend is rejected;
18. cloud or connector-oriented host with isolated workers and complete GitHub capabilities -> GitHub backend is selected;
19. backend interruption -> recover from durable state or fail closed without reconstructing raw evidence from memory;
20. OpenAI packaging exposes the skill to CHAT and CODEX while implicit invocation remains disabled;
21. a fresh Auditor with no prior ART or Steward context can reconstruct what an Essence is and apply the same material-completeness and freeze standard from `references/essence.md`;
22. a domain-specific Essence may omit non-applicable completeness dimensions without being forced into a fixed template, while any omitted material dimension remains a blocker;
23. project build/test/package mechanics already fixed by a durable Project Boundary -> no Essence finding merely because they are absent from the Essence;
24. Project Boundary exists only as an assumption in chat and is not reconstructible from durable repository authority -> formal blocker;
25. a reusable library or framework is clearly boundary-owned -> Auditor checks the relied-on interaction but does not audit that dependency's internals as part of this Essence;
26. completing the Essence appears to require a substantial reusable subsystem -> Auditor performs an SRP/responsibility-boundary diagnostic instead of automatically creating a dedicated contract;
27. specification pressure alone, without material scope or ownership ambiguity -> no formal blocker;
28. owner intentionally keeps a complex capability inside the component -> its material semantics remain part of the Essence contract, which may be physically split across referenced normative files;
29. a referenced normative formula appendix or similar file is explicitly part of the same Essence contract -> treat it as physical decomposition, not as a new generic contract type;
30. refactor or optimization preserves the frozen material contract -> no Essence reopen;
31. bug fix implements behavior already required by the frozen Essence -> no Essence reopen;
32. existing responsibility gains a material public or numerical behavior -> reopen the existing Essence rather than create a feature Essence;
33. new coherent reusable component with its own responsibility -> create a new Essence against the current Project Boundary;
34. large change with no new responsibility boundary -> size alone does not justify a new Essence;
35. incremental formal audit binds to the full exact repository SHA but certifies only the declared changed responsibility, materially affected interfaces, and relevant Project Boundary;
36. local change materially alters another frozen Essence's contract -> that affected Essence is reopened or explicitly included; it is not silently excluded from audit scope;
37. Project Boundary implementation changes but all relied-on contracts remain materially equivalent -> dependent Essence stays frozen;
38. Project Boundary change alters a material assumption relied on by an Essence -> reopen every materially affected Essence.

Do not add orchestration infrastructure merely to make these tests look automated. Start with the smallest fixture format that can expose real skill failures.
