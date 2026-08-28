# Agent guidance for txtDesk

## Purpose and central invariant

txtDesk is a portable terminal desktop for Unix-like systems, including use
over SSH. Core desktop abstractions must never become coupled to the user's
current iMac, server topology, or deployment policy.

Keep a firm distinction between the generic desktop framework and the
applications/providers that run on it. The core owns terminal lifecycle,
rendering, input, focus, layout, commands, configuration, and surface
lifecycle. Project Control, Codex, telemetry, remote control, and machine
profiles are edge integrations.

## Engineering bias

Keep the core small, unsurprising, dependency-light, and Unix-friendly. Prefer
simple interfaces, obvious ownership, RAII, reliable terminal restoration,
testable non-rendering logic, minimal global state, native Unix facilities
where appropriate, and extensions at the application/provider boundary.

Agents must not:

- turn txtDesk into an SSH client;
- hardcode a server or Tailscale, IPMI, or IoT assumptions into the core;
- reinvent a VT terminal emulator or treat a PTY as an embedded terminal;
- create a stable plugin ABI before multiple real applications require one;
- introduce a daemon architecture without demonstrated need;
- build large class hierarchies for theoretical future use;
- replace ordinary Unix conventions with fashionable abstractions without
  cause;
- depend on GUI frameworks for the base interface; or
- implement unrelated control-console features during foundational work.

## Workflow and current phase

The project is in bootstrap/foundation mode. Before selecting work, use the
installed `coding-workflow` front door and inspect the authoritative
todo-orchestrator state. Do not freelance around that workflow, manually edit
its SQLite database or generated projections, create competing TODO ledgers,
or claim future work unnecessarily.

Read `docs/scope.md` and `docs/architecture.md` before changing boundaries.
Treat the roadmap as a current sequence, not a frozen design. Do not continue
into a later milestone merely because its directory or task exists.
