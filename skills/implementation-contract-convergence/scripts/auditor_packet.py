"""Optional dispatcher-side projection; no GitHub access or worker orchestration.

Input JSON: assignment, target, verified_commit, allowlist, files, isolation.
The dispatcher independently verifies tree membership and semantic permission.
Only the returned packet may enter an Auditor context, never this input JSON.
"""

import hashlib
import json
import re
import sys


def digest(value):
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def git_blob(content, object_id):
    data = content.encode("utf-8")
    algorithm = "sha1" if len(object_id) == 40 else "sha256"
    return hashlib.new(algorithm, b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def object_id(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", value):
        raise ValueError("invalid object identity")
    return value


def build_packet(source):
    """Positive projection of reviewed exact-ref files; ignores response extras."""
    assignment = {key: source["assignment"][key]
                  for key in ("run", "round", "slot", "execution", "scope")}
    if not all(isinstance(v, str) and v for v in assignment.values()):
        raise ValueError("missing assignment identity or scope")
    target = {key: source["target"][key] for key in ("backend", "commit_sha", "tree_sha")}
    if target["backend"] not in ("github", "local"):
        raise ValueError("unsupported backend")
    for key in ("commit_sha", "tree_sha"):
        object_id(target[key])
    verified = source["verified_commit"]
    if verified["sha"] != target["commit_sha"] or verified["tree"]["sha"] != target["tree_sha"]:
        raise ValueError("target mismatch")
    isolation = source["isolation"]
    if isolation not in ("delivery_only", "host_enforced"):
        raise ValueError("missing isolation mode")
    allowlist = source["allowlist"]
    if not allowlist or set(allowlist.values()) - {"essence", "boundary", "instruction"}:
        raise ValueError("invalid allowlist")
    if set(allowlist.values()) != {"essence", "boundary", "instruction"}:
        raise ValueError("incomplete authority roles")
    files = []
    seen = set()
    for item in source["files"]:
        path = item["path"]
        if path not in allowlist or path in seen:
            raise ValueError("unexpected or duplicate input file")
        seen.add(path)
        blob = object_id(item["blob_sha"])
        if git_blob(item["content"], blob) != blob:
            raise ValueError("content identity mismatch")
        files.append({"path": path, "role": allowlist[path], "blob_sha": blob,
                      "content_sha256": hashlib.sha256(item["content"].encode("utf-8")).hexdigest(),
                      "content": item["content"]})
    if seen != set(allowlist):
        raise ValueError("missing allowlisted input")
    packet = {"assignment": assignment, "target": target, "isolation": isolation,
              "files": sorted(files, key=lambda f: f["path"])}
    packet["packet_sha256"] = digest(packet)
    return packet


def validate_result(packet, result):
    """Check a new sealed record, including invalidation; not a verdict evaluator."""
    if any(result[key] != packet[key] for key in ("assignment", "target", "packet_sha256")):
        raise ValueError("result binding mismatch")
    if result["status"] != "SEALED" or type(result["exposure"]) is not bool:
        raise ValueError("unsealed or missing exposure declaration")
    if not isinstance(result["findings"], list):
        raise ValueError("invalid findings")
    if result["validity"] == "INVALID":
        if result["verdict"] is not None or result["findings"] or result.get("advisory"):
            raise ValueError("invalid execution cannot carry a substantive review")
        return False
    if result["validity"] != "VALID" or result["exposure"]:
        raise ValueError("contaminated execution cannot be valid")
    if result["verdict"] not in ("PASS", "FAIL"):
        raise ValueError("missing substantive verdict")
    if (result["verdict"] == "PASS") != (len(result["findings"]) == 0):
        raise ValueError("verdict/findings mismatch")
    return True


if __name__ == "__main__":
    try:
        print(json.dumps(build_packet(json.load(sys.stdin)), ensure_ascii=False, indent=2))
    except (KeyError, TypeError, ValueError, AttributeError, UnicodeError):
        # Never echo unfiltered input or a traceback carrying source material.
        sys.exit("Auditor packet rejected: inspect dispatcher-only input.")
