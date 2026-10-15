"""Protocol contract regression checks; no live agent orchestration is claimed."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2] / "skills/implementation-contract-convergence"
def read(name):
    return (ROOT / name).read_text(encoding="utf-8").lower()

class OwnerDecisionProtocolTests(unittest.TestCase):
    def test_conversational_packet_and_advisory_authority(self):
        handoff = read("references/freeze-and-handoff.md")
        reconciler = read("references/reconciler.md")
        self.assertIn("every", handoff)
        self.assertIn("owner-facing conversation", handoff)
        for token in ("stable id", "a/b/c", "pros/cons", "recommendation", "d-01: b"):
            self.assertIn(token, handoff)
        self.assertIn("non-binding", reconciler)
        self.assertIn("owner's behalf", reconciler)

    def test_stable_alternatives_and_ambiguous_responses(self):
        handoff = read("references/freeze-and-handoff.md")
        self.assertIn("do not silently renumber", handoff)
        self.assertIn("clarify only ambiguous responses", handoff)
        for backend in ("backend-github.md", "backend-local.md"):
            text = read("references/" + backend)
            self.assertIn("letter-to-meaning mapping", text)
            self.assertIn("ambiguous", text)

    def test_partial_owner_replies_and_recovery_backend_parity(self):
        for backend in ("backend-github.md", "backend-local.md"):
            text = read("references/" + backend)
            for token in ("partial", "recovery", "selected letter", "resolved meaning", "owner"):
                self.assertIn(token, text)

    def test_no_agent_selection_and_no_extra_approval_gate(self):
        reconciler = read("references/reconciler.md")
        handoff = read("references/freeze-and-handoff.md")
        self.assertIn("neither the reconciler nor dispatcher may select", reconciler)
        self.assertIn("without an additional approval gate", handoff)
        self.assertIn("durably incorporated", handoff)

if __name__ == "__main__":
    unittest.main()
