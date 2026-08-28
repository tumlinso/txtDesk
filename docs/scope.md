# Project scope

txtDesk is a portable text-mode desktop environment that operates on the
current Unix terminal. SSH usability follows naturally from that model:
txtDesk does not establish the SSH connection.

## In scope

- a portable text desktop and terminal user interface;
- application surfaces and their lifecycle;
- screen layout and pane composition;
- focus and input dispatch;
- commands and keybindings;
- configuration;
- an eventual embedded terminal application; and
- eventual pluggable applications and integrations.

## Three distinct concerns

**txtDesk core** provides generic terminal/runtime and desktop behavior:
screen ownership, rendering, layout, focus, input, commands, configuration,
surface lifecycle, and clean shutdown.

**Applications and providers** use those facilities to present shells, files,
processes, status, development tools, external services, or control surfaces.
They do not redefine core desktop policy.

**Host-specific deployment and configuration** selects applications,
providers, keybindings, and machine policy for a particular installation. An
iMac control-console profile or a server-management profile belongs here, at
the edge.

## Out of scope for the core

The core does not own SSH connectivity, server-specific control logic, IPMI,
Tailscale, IoT devices, Project Control semantics, Codex semantics, telemetry
collection implementations, remote-machine abstraction, or machine-specific
deployment policy. Those capabilities may later appear through applications
or providers without coupling the desktop framework to them.
