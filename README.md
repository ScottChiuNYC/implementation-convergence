# Implementation Convergence

Reusable skills for converging implementation intent into a frozen contract and verified code.

## Planned skills

This repository is intentionally clean before skill authoring begins.

- **Implementation Contract Convergence** — planned skill for converging implementation intent into a frozen, unambiguous implementation contract.
- **Contract-to-Code Convergence** — planned skill for converging a frozen implementation contract into verified code.

The skill contracts and internal protocols have not been imported. They will be designed deliberately in this repository rather than inherited as accidental authority.

## Retained repository infrastructure

Only two reusable infrastructure capabilities are intentionally retained:

1. **CodeBinder PDF** — builds a reviewable whole-repository PDF and optionally publishes it to Google Drive.
2. **Remote Safe Patch** — provides a fail-closed path for narrow, exact edits made through connector-only GitHub workflows.

Everything else should earn its place based on the needs of these skills.

## Repository principles

- Keep skill semantics self-contained.
- Do not couple the two skills merely because they share a repository.
- Prefer a small shared infrastructure layer.
- Use normal feature branches and pull requests for broad or structural changes.
- Use Remote Safe Patch only for narrow single-file exact edits.
- Keep the generated CodeBinder PDF reviewable.
- Prefer squash merge for focused pull requests.

## License

MIT. See `LICENSE`.
