# txtDesk

txtDesk is a portable text-mode desktop environment intended to run directly
inside an ordinary Unix terminal, including a terminal reached over SSH. The
intended user experience is the same locally or remotely:

```sh
ssh some-machine
txtdesk
```

or simply `txtdesk` in a local terminal. The host should not define the
desktop's identity.

Traditional terminal sessions tend to become one shell, a multiplexer, or a
collection of unrelated terminal applications. txtDesk aims to provide a
coherent desktop-like interaction model in which shells, files, status
information, development tools, monitoring, and control applications can
coexist as first-class text surfaces.

The desktop core is host-agnostic. It owns terminal and screen lifecycle,
rendering, input and focus, layout, desktop chrome, commands, configuration,
and application registration. Machine-specific behavior and integrations such
as Project Control, Codex, telemetry, IPMI, remote power, or a particular
server profile belong in applications and providers outside that core. The old
iMac control-console idea is one possible future deployment, not the identity
of the project.

## Status

txtDesk is in repository-bootstrap and architecture-definition phase. The
current command is deliberately only a package smoke placeholder; it is not a
desktop implementation.

txtDesk is Python-first: Python 3.12+ is the default implementation substrate,
and Textual is the current preferred high-level TUI foundation. This favors
clear, rapid development of interaction, composition, subprocess, state, and
integration behavior over building generic terminal machinery from scratch.
Native components remain possible when a demonstrated low-level or performance
need justifies them.

From a checkout with Python 3.12 or newer:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
python -m txtdesk
txtdesk
pytest
```

See [the architecture](docs/architecture.md), [scope](docs/scope.md),
[roadmap](docs/roadmap.md), and [development conventions](docs/development.md)
before extending the project.
