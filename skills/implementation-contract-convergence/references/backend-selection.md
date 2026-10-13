# Backend Selection

Select one durable backend before the first formal round.

## Explicit selection

If the human explicitly requests local or GitHub execution, honor that choice when the required capabilities exist.

Do not silently switch backends after a round begins. If a backend becomes unavailable, persist the current boundary and stop or begin a newly authorized run after reconciling durable state.

## Automatic selection

When the human does not specify a backend:

1. use the local backend when the target repository is available as a local workspace and the host provides filesystem read/write, git, and fresh isolated subagent or worker execution sufficient for the configured Auditor slots;
2. use the GitHub backend when remote durable collaboration is desired and the host provides GitHub repository read/write, Issue read/write for control-plane records, branch and PR read/write with exact-head verification, and enough fresh isolated workers for formal audit;
3. otherwise fail closed before formal audit.

A GitHub connector is not required merely because the repository is hosted on GitHub.

## Selection principle

Protocol semantics and role authority are identical across backends.

Choose the backend for durable transport and integration mechanics, not for different audit semantics.

Use references/backend-local.md for local execution, references/backend-github.md for GitHub execution, and references/state-model.md for the records both must represent.
