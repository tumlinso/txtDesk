<!-- todo-orchestrator:v2-managed:start -->
# TD-M1-RUNTIME: Minimal terminal/runtime shell

Task revision: `2`; current project revision is in `todo-status.md`.

## Objective
Implement terminal initialization and RAII restoration, capability-aware screen setup, resize handling, an event loop, and minimal desktop chrome.

## State
- Lifecycle: `planned`
- Execution: `ready`
- Parallel policy: `serial`
- Result: `-`

## Next Action
Select the lightweight terminal substrate and implement the smallest safely restoring runtime shell; do not add embedded terminal panes.

## Ownership
- `exclusive`: `CMakeLists.txt`
- `exclusive`: `include/txtdesk`
- `exclusive`: `src`
- `exclusive`: `tests`

## Dependencies
- `task`: `TD-M0-FOUNDATION`
<!-- todo-orchestrator:v2-managed:end -->
