# Safe Patch

Safe Patch is a narrow, fail-closed editor for one existing tracked UTF-8 file.

Use it only when the intended change is an exact replacement. Broad or structural changes belong in a normal feature branch and pull request.

## Core guards

`tools/safe_patch.py` rejects a write when, among other conditions:

- the repository is not a Git working tree;
- HEAD is detached or on `main` / `master`;
- the expected HEAD is missing or stale;
- the target escapes the repository, is missing, untracked, or already dirty;
- the exact old-text anchor is missing or non-unique;
- the diff exceeds the configured changed-line budget;
- supported Python, JSON, TOML, or Markdown validation fails.

Writes are atomic. Validation failure restores the original file.

## Non-goals

Safe Patch is not a general refactoring engine, merge tool, fuzzy editor, or permission bypass. Use the ordinary branch/PR path whenever the change is not narrow and exact.
