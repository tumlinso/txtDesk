

<!-- todo-orchestrator:v2-managed:start -->
# Todo Orchestrator v2 Projection

Project revision: `4`

## Workstreams
- `TD-00` | kind: epic | status: planned | parent: - | objective: Deliver a portable host-agnostic text-mode desktop through restrained milestones.
- `TD-M0-FOUNDATION` | kind: task | status: done | parent: TD-00 | objective: Establish identity, documentation, agent guidance, a Python package skeleton, authoritative workflow, and Project Control visibility without implementing the desktop.
- `TD-M1-RUNTIME` | kind: workstream | status: planned | parent: TD-00 | objective: Build the smallest real txtDesk composition above Textual with clean startup and exit, resize behavior, minimal chrome, global commands, and one simple surface.
- `TD-M1-SURFACES` | kind: workstream | status: planned | parent: TD-00 | objective: Establish txtDesk desktop chrome and surface registration using Textual primitives, with no stable plugin API or speculative base-class hierarchy.
- `TD-M1-INPUT` | kind: workstream | status: planned | parent: TD-00 | objective: Add basic keyboard dispatch and global commands without coupling input events to application-specific semantics.
- `TD-M1-CAPABILITIES` | kind: validation_task | status: planned | parent: TD-00 | objective: Validate package entry points, Textual startup, resize, shutdown, failure cleanup, graceful degradation, representative TERM configurations, and SSH-like sessions.
- `TD-M2-LAYOUT` | kind: workstream | status: planned | parent: TD-00 | objective: Develop evidence-backed split, tab, placement, and focus traversal behavior for multiple surfaces.
- `TD-M2-LAUNCHER` | kind: workstream | status: planned | parent: TD-00 | objective: Provide a coherent launcher or command palette for built-in applications and desktop commands.
- `TD-M2-CONFIG` | kind: workstream | status: planned | parent: TD-00 | objective: Add portable configuration and keybinding behavior based on actual desktop command needs.
- `TD-M2-BASIC-APPS` | kind: workstream | status: planned | parent: TD-00 | objective: Build small filesystem, process, and status surfaces that exercise composition without embedding host-specific collection policy in the core.
- `TD-M3-TERMINAL` | kind: workstream | status: planned | parent: TD-00 | objective: Evaluate and integrate a mature Python-accessible terminal-state engine or contained native binding with PTY lifecycle, screen buffers, rendering, input forwarding, resize propagation, and interactive shells.
- `TD-M4-PROJECT-CONTROL` | kind: workstream | status: planned | parent: TD-00 | objective: Expose Project Control through an application and provider without transferring Project Control semantics into the desktop core.
- `TD-M4-CODEX` | kind: workstream | status: planned | parent: TD-00 | objective: Add Codex interaction as an application/provider using demonstrated integration boundaries rather than core semantics.
- `TD-M4-TELEMETRY` | kind: workstream | status: planned | parent: TD-00 | objective: Present GPU, CPU, network, and storage telemetry through replaceable providers without making txtDesk a monitoring library.
- `TD-M5-HOST-CONTROL` | kind: workstream | status: planned | parent: TD-00 | objective: Build optional edge applications and profiles for the iMac, server power, IPMI, IoT mains, Tailscale-aware management, and other deployment-specific needs.
- `TD-VALIDATION-DOCS` | kind: validation_task | status: planned | parent: TD-00 | objective: Validate unit tests, packaging and entry points, TUI smoke behavior, SSH and terminal compatibility, architecture boundaries, and user/developer documentation across the delivered project.
<!-- todo-orchestrator:v2-managed:end -->
