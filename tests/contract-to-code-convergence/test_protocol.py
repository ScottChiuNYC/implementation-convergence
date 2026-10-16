"""Document-contract regressions, not a workflow runner or isolation proof.

Keep assertions scoped to the normative section and check both the required
action and its fail-closed branch. Live worker behavior needs forward/E2E runs.
"""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILL = "skills/contract-to-code-convergence/"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def section(text, heading):
    """Return one level-two section, so unrelated prose cannot satisfy a guard."""
    marker = "## " + heading + "\n"
    return text.partition(marker)[2].split("\n## ", 1)[0]


def normalized(text):
    return " ".join(text.lower().split())


class ContractToCodeProtocolTests(unittest.TestCase):
    def setUp(self):
        self.skill = read(SKILL + "SKILL.md")
        self.handoff = read(SKILL + "references/state-and-handoff.md")
        self.entry = normalized(section(self.skill, "Entry and immutable authority"))
        self.authority = normalized(section(self.handoff, "Authority and journal"))
        self.evidence = normalized(section(self.handoff, "Durable evidence and isolation"))
        self.recovery = normalized(section(self.handoff, "Interruption recovery"))

    def test_unique_frozen_essence_can_be_selected_without_owner_path(self):
        self.assertIn("otherwise discover candidates from the pinned repository tree and normative references", self.entry)
        for text in (self.entry, self.authority):
            self.assertIn("automatically only", text)
            self.assertIn("exactly one unambiguous frozen / implementation_ready essence", text)
        self.assertNotIn("if the path is omitted, ask", self.entry)

    def test_missing_frozen_essence_blocks_instead_of_drafting_authority(self):
        self.assertIn("if zero candidates exist, stop as blocked and report the missing authority", self.entry)
        self.assertIn("stop when none exists (blocked)", self.authority)
        self.assertIn("do not reinterpret, reopen, or modify the frozen essence", normalized(self.skill))

    def test_ambiguous_frozen_essences_require_owner_selection(self):
        self.assertIn("if multiple plausible candidates exist, enter waiting_for_owner and ask the owner to select, without guessing", self.entry)
        self.assertIn("ask the owner when multiple candidates exist (waiting_for_owner)", self.authority)
        self.assertIn("do not expand scope to sibling essences", self.entry)

    def test_explicit_path_takes_precedence_without_fallback(self):
        self.assertIn("if the owner supplies a repository-relative target essence path, use exactly that path", self.entry)
        for text in (self.entry, self.authority):
            self.assertIn("existence, frozen status and provenance", text)
            self.assertIn("an invalid explicit path is blocked, with no fallback discovery", text)

    def test_candidates_are_authority_scopes_not_status_word_matches(self):
        self.assertIn("referenced normative parts of one essence are not separate candidates", self.entry)
        self.assertIn("count referenced normative parts as one essence", self.authority)
        for text in (self.entry, self.authority):
            self.assertIn("filenames, quoted status words and archived copies alone do not establish current frozen authority", text)

    def test_selection_is_pinned_and_persisted_before_delegation(self):
        self.assertIn("record its path, repository commit sha, blob sha, discovery evidence, and selection reason before formal delegation", self.entry)
        journal = self.authority.partition("persist selected path,")[2].partition("before delegation")[0]
        for field in ("baseline commit", "essence blob sha", "selection reason",
                      "project boundary and normative-part identities", "governing skill revision sha"):
            self.assertIn(field, journal)

    def test_gate_index_binds_observation_to_exact_candidate_and_location(self):
        fields = self.evidence.partition("for each material gate, index")[2].partition(". retain")[0]
        for field in ("role", "candidate sha", "baseline sha before implementation",
                      "command/check", "exit status or inspection outcome",
                      "durable evidence location", "sha256 digest when applicable",
                      "retention/availability limitations"):
            self.assertIn(field, fields)
        self.assertIn("governing skill revision sha", self.entry)

    def test_evidence_requires_retained_results_and_verified_readback(self):
        self.assertIn("retain critical command outputs, assertions and inspection results", self.evidence)
        self.assertIn("read back retained evidence and verify its identity and applicable digest before counting it", self.evidence)
        for text in (self.entry, self.evidence):
            self.assertIn("a hash or unavailable link alone is not retained evidence", text)

    def test_unavailable_or_mismatched_evidence_reopens_affected_gate(self):
        self.assertIn("if evidence is missing, expired or mismatched, mark the affected gate incomplete and rerun or recover it before verified", self.evidence)
        self.assertIn("never infer a pass from the index alone", self.evidence)

    def test_recreated_evidence_cannot_backdate_acceptance_seal(self):
        self.assertIn("later evidence must not retroactively claim that acceptance was sealed before implementation", self.evidence)
        self.assertIn("an unprovable pre-code seal is blocked until its original provenance is recovered", self.evidence)
        stage_a = normalized(section(self.skill, "Stage A — independent acceptance derivation (before implementation)"))
        self.assertIn("before the implementer writes code", stage_a)
        self.assertIn("exact content hashes and durable locations", stage_a)
        self.assertIn("only transition to acceptance_sealed after manifest and feasible pre-code test assets are independently read back", normalized(self.handoff))

    def test_isolation_report_names_levels_and_demonstrated_mechanism(self):
        for text in (self.entry, self.evidence):
            for level in ("fresh-context only", "controlled-input delivery", "enforced tool-access isolation"):
                self.assertIn(level, text)
            self.assertIn("mechanism", text)
            self.assertIn("limitations", text)
        self.assertIn("role/execution identity", self.evidence)
        self.assertIn("delivered inputs", self.evidence)
        self.assertIn("never claim a stronger level than demonstrated", self.evidence)

    def test_prompt_restrictions_do_not_prove_tool_isolation(self):
        self.assertIn("fresh context does not prove input filtering", self.evidence)
        self.assertIn("checked input delivery does not restrict inherited tools", self.evidence)
        for text in (self.entry, self.evidence):
            self.assertIn("prompts alone do not enforce tool access", text)
            self.assertIn("if the required isolation level is unavailable, fail the compatibility gate", text)
        self.assertIn("reporting a limitation does not waive the requirement", self.evidence)

    def test_recovery_revalidates_authority_and_keeps_original_target_and_skill(self):
        for field in ("selected path", "pinned baseline commit", "essence blob",
                      "referenced authority identities", "governing skill revision",
                      "acceptance seal and asset hashes", "current candidate/ci shas",
                      "findings and merge policy"):
            self.assertIn(field, self.recovery)
        self.assertIn("never silently select a new target or adopt a newer skill revision", self.recovery)
        completion = normalized(section(self.skill, "Completion and publication"))
        self.assertIn("revalidate the recorded authority and governing skill revision", completion)
        self.assertIn("never silently select a new target", completion)

    def test_recovery_distinguishes_baseline_from_implementation_candidate(self):
        self.assertIn("validate authority at the recorded baseline separately from the current candidate", self.recovery)
        self.assertIn("implementation commits need not equal the baseline", self.recovery)
        self.assertIn("a moved candidate invalidates prior candidate-sha-specific evidence", self.recovery)
        self.assertIn("rerun impacted checks and rebind final verification", self.recovery)

    def test_recovery_fails_closed_and_resumes_first_incomplete_stage(self):
        self.assertIn("resume the first incomplete stage only after readback", self.recovery)
        self.assertIn("divergent or missing state is blocked until reconciled", self.recovery)
        self.assertIn("a prior agent summary or terminal-state label is not proof", self.recovery)
        self.assertIn("stable ids and exact option meaning; never silently reinterpret partial responses", self.recovery)

    def test_github_and_local_have_same_evidence_obligations(self):
        compatibility = normalized(section(self.skill, "Invocation and compatibility"))
        self.assertIn("backend changes transport, not evidence or authority rules", compatibility)
        handoff = normalized(self.handoff)
        self.assertIn("issues/pr comments/checks and retained artifacts as durable transport", handoff)
        self.assertIn("ephemeral scratch paths alone are insufficient", handoff)
        self.assertIn("local backend may use tracked or untracked durable files plus git", handoff)

    def test_readme_selection_guidance_matches_both_backend_prompts(self):
        readme = normalized(read(SKILL + "README.md"))
        self.assertEqual(readme.count("target essence: <optional repository-relative path>"), 2)
        for clause in ("exactly one unambiguous frozen / implementation_ready essence",
                       "an invalid explicit path is blocked, with no fallback discovery",
                       "ask the owner (waiting_for_owner)", "if none exists, stop (blocked)",
                       "referenced normative parts of one essence are not separate candidates",
                       "governing skill revision", "first incomplete stage"):
            self.assertIn(clause, readme)
        self.assertNotIn("target essence path is required", readme.replace("**", ""))

    def test_overview_keeps_first_skill_path_rule_unchanged(self):
        quick_start = normalized(section(read("README.md"), "Quick-start prompts"))
        self.assertIn("implementation contract convergence requires an explicit target essence path", quick_start)
        self.assertIn("for contract-to-code convergence, that path is optional only when exactly one unambiguous frozen essence", quick_start)

    def test_status_is_qualified_without_claiming_revised_e2e_certification(self):
        for path in ("README.md", "docs/lifecycle.md", SKILL + "README.md"):
            text = normalized(read(path))
            self.assertIn("e2e pass with", text)
            self.assertNotIn("not yet validated as a single-invocation", text)
            self.assertNotIn("not yet single-invocation e2e verified", text)
        skill_readme = normalized(read(SKILL + "README.md"))
        self.assertIn("has not itself passed a new e2e run", skill_readme)
        self.assertIn("do not execute an agent workflow or prove worker isolation", skill_readme)

    def test_acceptance_and_fresh_verification_guards_remain_consistent(self):
        manifest = normalized(read(SKILL + "references/acceptance-manifest.md"))
        self.assertIn("created and sealed by an independent acceptance analyst before implementation begins", manifest)
        self.assertIn("recording expected outcomes before viewing implementation results", manifest)
        self.assertIn("final-verifier supplemental cases and expected results must be recorded before candidate outputs are examined", normalized(self.handoff))
        self.assertIn("new fresh final verifier", normalized(section(self.skill, "Stage D — independent final verification")))

    def test_ci_runs_new_suite_and_skill_stays_explicitly_invoked(self):
        workflow = read(".github/workflows/publish-codebinder-pdf.yml")
        self.assertIn("python -m unittest discover -s tests/contract-to-code-convergence -p 'test_*.py'", workflow)
        metadata = read(SKILL + "agents/openai.yaml")
        self.assertRegex(metadata, r"allow_implicit_invocation:\s*false")
        self.assertIn("require explicit owner invocation", normalized(self.skill))


if __name__ == "__main__":
    unittest.main()
