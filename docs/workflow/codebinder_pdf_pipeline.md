# CodeBinder PDF Pipeline

## Purpose

The repository builds a reviewable PDF from tracked content so the owner can inspect the repository as one artifact.

The pipeline is infrastructure only. It must not encode assumptions about either implementation-convergence skill.

## Trigger

`.github/workflows/publish-codebinder-pdf.yml` runs on:

- pull requests to `main`;
- pushes to `main`;
- manual dispatch.

Pull-request runs build and validate the PDF. Successful `main` runs may also publish it to Google Drive.

## Validation

The workflow:

1. runs retained tool tests and Python syntax checks;
2. validates tracked Markdown and display-math delimiters;
3. converts the repository with CodeBinder;
4. verifies representative repository and infrastructure content was included;
5. builds the PDF with Sphinx and LaTeX;
6. checks PDF structure and rendered text;
7. uploads the GitHub Actions artifact;
8. optionally uploads the PDF to Google Drive.

The final-PDF validation rejects known rendering failures such as leaked `nbsphinx-math` role markup.

## Mathematics

Use:

- inline math: `$...$`;
- display math: standalone `$$...$$` blocks.

Do not use LaTeX-style `\\[ ... \\]` display delimiters in Markdown; the checked-in validator rejects them because they have produced broken reader-visible output in this toolchain.

## Google Drive

Publication is enabled only when all four repository secrets are present:

```text
GOOGLE_DRIVE_CLIENT_ID
GOOGLE_DRIVE_CLIENT_SECRET
GOOGLE_DRIVE_REFRESH_TOKEN
GOOGLE_DRIVE_FOLDER_ID
```

Behavior is fail-closed:

- 0/4 secrets: Drive publication is disabled;
- 4/4 secrets: publication is enabled;
- 1-3/4 secrets: the workflow fails the configuration check.

Secret values must never be committed or emitted into generated documentation.
