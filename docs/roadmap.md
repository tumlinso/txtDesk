# Roadmap

This roadmap is deliberately restrained and may change as working software
teaches the project where its boundaries belong.

## M0: Repository foundation

- project identity and documentation;
- agent guidance and build skeleton;
- todo workflow and Project Control visibility; and
- initial architectural boundaries.

## M1: Minimal desktop shell

Build a small runnable `txtdesk` that initializes and reliably restores the
terminal, handles resize, draws simple desktop chrome, dispatches basic
keyboard commands, and hosts at least one simple built-in surface behind a
minimal surface abstraction.

## M2: Desktop composition

- split, tab, and layout model;
- focus traversal;
- application launcher or command palette;
- configuration and keybindings; and
- simple file, process, and status applications.

## M3: Real terminal application

- PTY process ownership;
- a mature VT terminal-state engine;
- an embedded interactive shell;
- resize propagation; and
- multiple terminal panes.

## M4: Development and control applications

Examples include Project Control, Codex, task and agent views, and telemetry.
These are applications/providers rather than desktop-core concerns.

## M5: Host-specific deployments

Examples include an old-iMac control-console profile, server power controls,
IPMI, an IoT mains switch, and Tailscale-aware remote management. These belong
at the edge, not in the core.
