# Remote Safe Patch

## Purpose

Remote Safe Patch exposes the repository's fail-closed Safe Patch engine through a narrow GitHub control plane. It exists for connector-only environments where an agent can work through GitHub but does not have a trusted local checkout.

Use it only for a narrow exact edit to one existing tracked UTF-8 file.

New files, multi-file changes, renames, deletions, whole-document rewrites, and changes to patch infrastructure use the normal feature-branch / pull-request workflow.

## Preferred path

The owner-authored control issue is titled:

```text
[remote-safe-patch-control]
```

A v2 request uses exact literal blocks:

```text
[remote-safe-patch-intent]
version: 2
target: docs/example.md
max_changed_lines: 6
old: |
  The old sentence.
new: |
  The revised sentence.
```

Trusted GitHub Actions binds the request to current repository state, creates an isolated branch, applies deterministic guards, pushes only the requested target change, and opens a focused result PR.

## Safety properties

The retained implementation enforces applicable guards including:

- one existing tracked UTF-8 target;
- protected-target rejection;
- exact HEAD and target-blob binding;
- one exact unique old-text match;
- no-op rejection;
- changed-line budget enforcement;
- target-only post-write diff;
- clean post-commit working tree;
- no force push.

The patch workflows and patch engines protect themselves from being modified through the Remote Safe Patch path.

## Components

```text
.github/workflows/remote-safe-patch-control.yml
.github/workflows/remote-safe-patch.yml
tools/remote_safe_patch_control.py
tools/remote_safe_patch.py
tools/safe_patch.py
tools/tests/test_remote_safe_patch_control.py
tools/tests/test_remote_safe_patch.py
tools/tests/test_safe_patch.py
```

The control-issue workflow is the preferred route. The older PR-comment workflow is retained as a recovery route.

## Merge rule

A generated PR is not merge authority by itself.

Re-read the final PR head, verify the semantic diff and checks on that exact head, then squash merge and verify `main`.
