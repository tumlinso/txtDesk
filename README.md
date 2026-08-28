# txtDesk

txtDesk is a portable text-mode desktop environment intended to run directly
inside an ordinary Unix terminal, including a terminal reached over SSH. The
eventual entry point is:

```text
txtdesk
```

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
current executable is deliberately only a compileable placeholder; it is not a
desktop implementation.

The current engineering preference is C++20 with CMake and a lightweight Unix
terminal UI substrate such as ncursesw. From a checkout with a C++20 compiler
and CMake:

```sh
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

See [the architecture](docs/architecture.md), [scope](docs/scope.md),
[roadmap](docs/roadmap.md), and [development conventions](docs/development.md)
before extending the project.
