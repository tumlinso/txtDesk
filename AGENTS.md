# Agent guidance for txtDesk

## Purpose and central invariant

txtDesk is a portable terminal desktop for Unix-like systems, including use
over SSH. Core desktop abstractions must never become coupled to the user's
current iMac, server topology, or deployment policy.

Keep a firm distinction between generic txtDesk behavior and the applications,
providers, and deployment profiles assembled around it. txtDesk core owns
application lifecycle, global commands, focus policy, desktop composition,
shared configuration and state where necessary, common chrome, and surface
registration. Project Control, Codex, telemetry, remote control, and machine
profiles are edge integrations.

## Engineering bias

Keep the core small, unsurprising, dependency-light, and Unix-friendly. Prefer
simple Python, obvious ownership and state, reliable cleanup, testable logic,
minimal global state, native Unix facilities where appropriate, and extensions
at the application/provider boundary.

Python 3.12+ is the default. Textual is the current preferred TUI foundation:
use its application, widget, layout, focus, input, and async facilities rather
than building a second framework underneath it. Do not wrap every Textual
concept speculatively. Native code or extensions must earn their existence
through a demonstrated low-level or performance requirement.

Agents must not:

- turn txtDesk into an SSH client;
- hardcode a server or Tailscale, IPMI, or IoT assumptions into the core;
- reinvent a VT terminal emulator or treat a PTY as an embedded terminal;
- create a stable plugin ABI before multiple real applications require one;
- introduce a daemon architecture without demonstrated need;
- build large class hierarchies for theoretical future use;
- build a custom widget, layout, or event framework under Textual;
- replace ordinary Unix conventions with fashionable abstractions without
  cause;
- depend on GUI frameworks for the base interface; or
- implement unrelated control-console features during foundational work.

## Workflow and current phase

The project is in bootstrap/foundation mode. The currently installed canonical
front door is `coding-workflow`; todo-orchestrator is its authoritative
SQLite-backed kernel. Before selecting work, use that front door and inspect
the live Project Control/todo state. Do not freelance around it, manually edit
its database or generated projections, create competing TODO ledgers, or claim
future work unnecessarily.

Read `docs/scope.md` and `docs/architecture.md` before changing boundaries.
Treat the roadmap as a current sequence, not a frozen design. Do not continue
into a later milestone merely because its directory or task exists.
