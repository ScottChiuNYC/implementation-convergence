"""Static ICC protocol regression checks; these do not simulate agent behavior."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2] / "skills/implementation-contract-convergence"

def read(path):
    return (ROOT / path).read_text(encoding="utf-8").lower()


class AcceptanceAuthorityProtocolTests(unittest.TestCase):
    def test_material_numerical_commitments_require_authority(self):
        skill = read("SKILL.md")
        essence = read("references/essence.md")
        for term in ("no unauthorized material acceptance commitments",
                     "explicit owner", "rigorous", "observed convergence",
                     "transfer", "efficiency"):
            self.assertIn(term, skill)
        for term in ("bounded delegation", "exact arithmetic", "finite grids",
                     "owner decision", "normative"):
            self.assertIn(term, essence)

    def test_no_silent_new_numerical_gates(self):
        for path in ("SKILL.md", "references/auditor.md",
                     "references/remediator.md"):
            text = read(path)
            for term in ("empirical", "threshold", "owner", "mathematical"):
                self.assertIn(term, text, path)
        self.assertIn("not turn an agent-invented empirical numerical gate", read("SKILL.md"))
        self.assertIn("cannot become a mandatory gate", read("references/auditor.md"))
        self.assertIn("do not invent material empirical numerical acceptance gates", read("references/remediator.md"))

    def test_existing_requirements_still_can_be_verified(self):
        skill = read("SKILL.md")
        self.assertIn("verification methods for already-authorized behavior", skill)
        self.assertIn("independently derive tests to verify the", skill)
        self.assertIn("existing", skill)
        self.assertIn("cannot amend it", skill)

    def test_github_document_only_ci_not_mandatory(self):
        backend = read("references/backend-github.md")
        for term in ("documentation-only", "do not run builds/tests",
                     "do not wait", "automatically triggered",
                     "repository policy", "required status checks"):
            self.assertIn(term, backend)
        self.assertIn("exact-head/diff/readback/merge verification", backend)
        self.assertIn("never weakens c2c verification", backend)

    def test_math_only_icc_no_dynamic_feasibility_prototype(self):
        skill = read("SKILL.md")
        self.assertIn("mathematical consistency review belongs here", skill)
        self.assertIn("numerical regression studies and dynamic feasibility prototypes belong to contract-to-code convergence", skill)
        self.assertIn("no new icc execution stage or subagent", skill)


if __name__ == "__main__":
    unittest.main()
