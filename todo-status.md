

<!-- todo-orchestrator:v2-managed:start -->
# Todo Status v2 Projection

Project revision: `2`

## Workstreams
- `TD-00` | status: planned | execution: inactive | next: Deliver a portable host-agnostic text-mode desktop through restrained milestones.
- `TD-M0-FOUNDATION` | status: done | execution: closed | next: Establish identity, documentation, agent guidance, build skeleton, authoritative workflow, and Project Control visibility without implementing the desktop.
- `TD-M1-RUNTIME` | status: planned | execution: ready | next: Select the lightweight terminal substrate and implement the smallest safely restoring runtime shell; do not add embedded terminal panes.
- `TD-M1-SURFACES` | status: planned | execution: ready | next: Introduce the smallest useful surface lifecycle and render contract, with one simple built-in surface and no stable plugin ABI.
- `TD-M1-INPUT` | status: planned | execution: ready | next: Add basic keyboard dispatch and global commands without coupling input events to application-specific semantics.
- `TD-M1-CAPABILITIES` | status: planned | execution: ready | next: Validate startup, graceful degradation, resize, shutdown, and restoration across representative TERM configurations and SSH-like sessions.
- `TD-M2-LAYOUT` | status: planned | execution: ready | next: Develop evidence-backed split, tab, placement, and focus traversal behavior for multiple surfaces.
- `TD-M2-LAUNCHER` | status: planned | execution: ready | next: Provide a coherent launcher or command palette for built-in applications and desktop commands.
- `TD-M2-CONFIG` | status: planned | execution: ready | next: Add portable configuration and keybinding behavior based on actual desktop command needs.
- `TD-M2-BASIC-APPS` | status: planned | execution: ready | next: Build small native applications that exercise the surface model without embedding host-specific collection policy in the core.
- `TD-M3-TERMINAL` | status: planned | execution: ready | next: Deliberately select and integrate a mature VT state engine with PTY ownership, resize propagation, interactive shells, and multiple terminal panes.
- `TD-M4-PROJECT-CONTROL` | status: planned | execution: ready | next: Expose Project Control through an application and provider without transferring Project Control semantics into the desktop core.
- `TD-M4-CODEX` | status: planned | execution: ready | next: Add Codex interaction as an application/provider using demonstrated integration boundaries rather than core semantics.
- `TD-M4-TELEMETRY` | status: planned | execution: ready | next: Present GPU, CPU, network, and storage telemetry through replaceable providers without making txtDesk a monitoring library.
- `TD-M5-HOST-CONTROL` | status: planned | execution: ready | next: Build optional edge applications and profiles for the iMac, server power, IPMI, IoT mains, Tailscale-aware management, and other deployment-specific needs.
- `TD-VALIDATION-DOCS` | status: planned | execution: ready | next: Validate architecture boundaries, portability, terminal safety, tests, and user/developer documentation across the delivered project.
<!-- todo-orchestrator:v2-managed:end -->
