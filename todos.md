

<!-- todo-orchestrator:v2-managed:start -->
# Todo Orchestrator v2 Projection

Project revision: `2`

## Workstreams
- `TD-00` | kind: epic | status: planned | parent: - | objective: Deliver a portable host-agnostic text-mode desktop through restrained milestones.
- `TD-M0-FOUNDATION` | kind: task | status: done | parent: TD-00 | objective: Establish identity, documentation, agent guidance, build skeleton, authoritative workflow, and Project Control visibility without implementing the desktop.
- `TD-M1-RUNTIME` | kind: workstream | status: planned | parent: TD-00 | objective: Implement terminal initialization and RAII restoration, capability-aware screen setup, resize handling, an event loop, and minimal desktop chrome.
- `TD-M1-SURFACES` | kind: workstream | status: planned | parent: TD-00 | objective: Introduce the smallest useful surface lifecycle and render contract, with one simple built-in surface and no stable plugin ABI.
- `TD-M1-INPUT` | kind: workstream | status: planned | parent: TD-00 | objective: Add basic keyboard dispatch and global commands without coupling input events to application-specific semantics.
- `TD-M1-CAPABILITIES` | kind: validation_task | status: planned | parent: TD-00 | objective: Validate startup, graceful degradation, resize, shutdown, and restoration across representative TERM configurations and SSH-like sessions.
- `TD-M2-LAYOUT` | kind: workstream | status: planned | parent: TD-00 | objective: Develop evidence-backed split, tab, placement, and focus traversal behavior for multiple surfaces.
- `TD-M2-LAUNCHER` | kind: workstream | status: planned | parent: TD-00 | objective: Provide a coherent launcher or command palette for built-in applications and desktop commands.
- `TD-M2-CONFIG` | kind: workstream | status: planned | parent: TD-00 | objective: Add portable configuration and keybinding behavior based on actual desktop command needs.
- `TD-M2-BASIC-APPS` | kind: workstream | status: planned | parent: TD-00 | objective: Build small native applications that exercise the surface model without embedding host-specific collection policy in the core.
- `TD-M3-TERMINAL` | kind: workstream | status: planned | parent: TD-00 | objective: Deliberately select and integrate a mature VT state engine with PTY ownership, resize propagation, interactive shells, and multiple terminal panes.
- `TD-M4-PROJECT-CONTROL` | kind: workstream | status: planned | parent: TD-00 | objective: Expose Project Control through an application and provider without transferring Project Control semantics into the desktop core.
- `TD-M4-CODEX` | kind: workstream | status: planned | parent: TD-00 | objective: Add Codex interaction as an application/provider using demonstrated integration boundaries rather than core semantics.
- `TD-M4-TELEMETRY` | kind: workstream | status: planned | parent: TD-00 | objective: Present GPU, CPU, network, and storage telemetry through replaceable providers without making txtDesk a monitoring library.
- `TD-M5-HOST-CONTROL` | kind: workstream | status: planned | parent: TD-00 | objective: Build optional edge applications and profiles for the iMac, server power, IPMI, IoT mains, Tailscale-aware management, and other deployment-specific needs.
- `TD-VALIDATION-DOCS` | kind: validation_task | status: planned | parent: TD-00 | objective: Validate architecture boundaries, portability, terminal safety, tests, and user/developer documentation across the delivered project.
<!-- todo-orchestrator:v2-managed:end -->
