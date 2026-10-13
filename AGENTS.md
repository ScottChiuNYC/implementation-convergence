# Agent Instructions

This repository contains reusable implementation-convergence skills.

## Read first

Before modifying the repository, read:

1. `README.md`
2. the files for the skill or infrastructure capability being changed

Do not infer skill semantics from old ART or Steward conventions. If a skill contract is not present in this repository, treat it as not yet defined.

## Working rules

- Keep each skill self-contained.
- Add shared infrastructure only when both skills genuinely need it.
- Use a normal feature branch and pull request for broad, structural, multi-file, new-file, rename, delete, or infrastructure changes.
- Use Remote Safe Patch only for a narrow exact edit to one existing tracked UTF-8 file.
- Validate the exact pull-request head before merge.
- Prefer squash merge for focused changes.
- After merge, verify `main` and any applicable CodeBinder PDF publication.

## Retained infrastructure

- CodeBinder PDF: `docs/workflow/codebinder_pdf_pipeline.md`
- Safe Patch: `docs/workflow/safe_patch.md`
- Remote Safe Patch: `docs/workflow/remote_safe_patch.md`
