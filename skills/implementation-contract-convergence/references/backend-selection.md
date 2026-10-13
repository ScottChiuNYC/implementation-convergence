# Backend Selection

Select one durable backend before the first formal round.

## Explicit selection

If the human explicitly requests local or GitHub execution, honor that choice when the required capabilities exist.

Do not silently switch backends after a round begins. If a backend becomes unavailable, persist the current boundary and stop or begin a newly authorized run after reconciling durable state.

## Automatic selection

When the human does not specify a backend:

1. use the local backend only when the target repository is available as a stable local workspace and the host provides persistent shared filesystem read/write, git, and fresh isolated subagent or worker execution sufficient for the configured Auditor slots;
2. use the GitHub backend when remote durable collaboration or cross-session recovery is needed and the host provides GitHub repository read/write, Issue read/write for control-plane records, branch and PR read/write with exact-head verification, and enough fresh isolated workers for formal audit;
3. otherwise fail closed before formal audit.

A host does not qualify for the local backend merely because it exposes a filesystem or cloud computer. Local state must be shared by the required workers and reliably persist for the lifetime of the convergence run and any supported resume path. If that durability cannot be established, prefer the GitHub backend when its capabilities are available.

A GitHub connector is not required merely because the repository is hosted on GitHub.

## Cloud and connector-oriented hosts

For cloud, mobile, connector-only, or cross-session execution, do not assume an execution container is durable protocol state.

When fresh isolated workers are available but durable local state cannot be guaranteed, select the GitHub backend if the required GitHub mutation and readback capabilities exist.

## Selection principle

Protocol semantics and role authority are identical across backends.

Choose the backend for durable transport and integration mechanics, not for different audit semantics.

Use references/backend-local.md for local execution, references/backend-github.md for GitHub execution, and references/state-model.md for the records both must represent.
