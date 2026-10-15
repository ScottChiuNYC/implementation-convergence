"""Synthetic spill regression: no private project content or live GitHub calls."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills/implementation-contract-convergence/scripts/auditor_packet.py"
spec = importlib.util.spec_from_file_location("auditor_packet", SCRIPT)
packet_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packet_module)
CANARY = "FORBIDDEN_PRIOR_REMEDIATION_ASSERTION"


def fixture(backend="github"):
    commit, tree = "a" * 40, "b" * 40
    files = []
    for path, content in (("contract.md", "Current normative requirements.\n"),
                          ("boundary.md", "Current established boundary.\n"),
                          ("auditor.md", "Generic independent audit instructions.\n")):
        data = content.encode()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        files.append({"path": path, "content": content, "blob_sha": blob,
                      "raw_response": CANARY})
    return {
        "assignment": {"run": "r", "round": "2", "slot": "A", "execution": "A1", "scope": "Component"},
        "target": {"backend": backend, "commit_sha": commit, "tree_sha": tree, "extra": CANARY},
        # Mirrors a broad commit response: valid metadata plus an unrequested patch.
        "verified_commit": {"sha": commit, "tree": {"sha": tree, "extra": CANARY},
                            "message": CANARY, "diff": "+++ docs/audit/REMEDIATION.md\n+" + CANARY,
                            "parents": [{"history": CANARY}]},
        "allowlist": {"contract.md": "essence", "boundary.md": "boundary", "auditor.md": "instruction"},
        "files": files, "isolation": "delivery_only", "control_issue": CANARY,
    }


def result(packet, **changes):
    record = {key: copy.deepcopy(packet[key]) for key in ("assignment", "target", "packet_sha256")}
    record.update(status="SEALED", validity="VALID", exposure=False, verdict="PASS", findings=[])
    record.update(changes)
    return record


class PacketTests(unittest.TestCase):
    def test_broad_verification_response_is_not_delivered(self):
        source = fixture()
        self.assertIn(CANARY, json.dumps(source))  # The demonstrated dangerous emission.
        packet = packet_module.build_packet(source)
        self.assertNotIn(CANARY, json.dumps(packet))
        self.assertNotIn("REMEDIATION.md", json.dumps(packet))
        self.assertEqual({f["path"] for f in packet["files"]}, set(source["allowlist"]))
        self.assertEqual({f["role"] for f in packet["files"]}, {"essence", "boundary", "instruction"})

    def test_backend_parity(self):
        github = packet_module.build_packet(fixture())
        local = packet_module.build_packet(fixture("local"))
        self.assertEqual(github["files"], local["files"])
        self.assertTrue(packet_module.validate_result(local, result(local)))

    def test_unapproved_file_is_rejected(self):
        source = fixture()
        source["files"].append({"path": "docs/audit/REMEDIATION.md", "content": CANARY})
        with self.assertRaises(ValueError):
            packet_module.build_packet(source)

    def test_missing_or_duplicate_file_is_rejected(self):
        for operation in (lambda files: files.pop(), lambda files: files.append(files[0])):
            with self.subTest(operation=operation):
                source = fixture()
                operation(source["files"])
                with self.assertRaises(ValueError):
                    packet_module.build_packet(source)

    def test_missing_authority_role_is_rejected(self):
        source = fixture()
        source["allowlist"]["boundary.md"] = "instruction"
        with self.assertRaises(ValueError):
            packet_module.build_packet(source)

    def test_wrong_commit_or_tree_is_rejected(self):
        for key in ("commit", "tree"):
            source = fixture()
            if key == "commit":
                source["verified_commit"]["sha"] = "c" * 40
            else:
                source["verified_commit"]["tree"]["sha"] = "c" * 40
            with self.assertRaises(ValueError):
                packet_module.build_packet(source)

    def test_changed_content_is_rejected(self):
        source = fixture()
        source["files"][0]["content"] += "Changed after verification"
        with self.assertRaises(ValueError):
            packet_module.build_packet(source)

    def test_sha256_git_blob_and_unicode(self):
        source = fixture()
        data = "Normative text: \u03c4\n".encode("utf-8")
        source["files"][0].update(content=data.decode(), blob_sha=hashlib.sha256(
            b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest())
        self.assertEqual(packet_module.build_packet(source)["files"][2]["content"], data.decode())

    def test_packet_digest_binds_assignment_and_contents(self):
        source = fixture()
        original = packet_module.build_packet(source)
        self.assertEqual(original, packet_module.build_packet(source))
        source["assignment"]["execution"] = "A2"
        self.assertNotEqual(original["packet_sha256"], packet_module.build_packet(source)["packet_sha256"])

    def test_contamination_is_invalid_without_verdict(self):
        packet = packet_module.build_packet(fixture())
        invalid = result(packet, validity="INVALID", exposure=True, verdict=None)
        self.assertFalse(packet_module.validate_result(packet, invalid))
        for changes in ({"verdict": "PASS"}, {"verdict": "FAIL"}, {"findings": ["observation"]},
                        {"findings": None}, {"advisory": "zero findings after review"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                packet_module.validate_result(packet, {**invalid, **changes})

    def test_exposed_valid_verdict_cannot_count(self):
        packet = packet_module.build_packet(fixture())
        with self.assertRaises(ValueError):
            packet_module.validate_result(packet, result(packet, exposure=True))

    def test_same_slot_retry_is_new_execution_without_old_result(self):
        source = fixture()
        first = packet_module.build_packet(source)
        invalid = result(first, validity="INVALID", exposure=True, verdict=None)
        source["assignment"]["execution"] = "A2"
        replacement = packet_module.build_packet(source)
        self.assertEqual(first["target"], replacement["target"])
        self.assertEqual(first["files"], replacement["files"])
        self.assertEqual(first["assignment"]["slot"], replacement["assignment"]["slot"])
        self.assertFalse(packet_module.validate_result(first, invalid))
        with self.assertRaises(ValueError):
            packet_module.validate_result(replacement, invalid)
        self.assertTrue(packet_module.validate_result(replacement, result(replacement)))

    def test_unsealed_or_wrong_binding_cannot_count(self):
        packet = packet_module.build_packet(fixture())
        for changes in ({"status": "PENDING"}, {"packet_sha256": "wrong"}, {"exposure": "no"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                packet_module.validate_result(packet, result(packet, **changes))

    def test_verdict_requires_matching_findings(self):
        packet = packet_module.build_packet(fixture())
        self.assertTrue(packet_module.validate_result(packet, result(packet, verdict="FAIL", findings=["gap"])))
        for changes in ({"verdict": "FAIL"}, {"findings": ["gap"]}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                packet_module.validate_result(packet, result(packet, **changes))

    def test_cli_emits_only_packet_and_sanitizes_errors(self):
        source = fixture()
        good = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(source),
                              capture_output=True, text=True, check=True)
        self.assertNotIn(CANARY, good.stdout + good.stderr)
        self.assertEqual(json.loads(good.stdout), packet_module.build_packet(source))
        source["files"][0]["content"] = CANARY
        bad = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(source),
                             capture_output=True, text=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertNotIn(CANARY, bad.stdout + bad.stderr)
        self.assertNotIn("Traceback", bad.stderr)


if __name__ == "__main__":
    unittest.main()
