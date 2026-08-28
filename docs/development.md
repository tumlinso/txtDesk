# Development conventions

Python 3.12+ is the default implementation language, using a conventional
`src/txtdesk/` package layout. txtDesk is dominated by interaction design,
orchestration, state, composition, subprocesses, external tools, and
asynchronous providers rather than throughput-critical numerical work.
Development speed and clarity matter more than native rendering performance.
Python is the default; native extensions must earn their existence.

Textual is the current preferred TUI foundation. Use its widgets, layout,
focus, input, application lifecycle, and async integration directly where they
fit. Python's `asyncio` facilities are appropriate for external data and
subprocess coordination, but ownership, cancellation, cleanup, and shared
state must remain explicit. Do not create a second event or widget framework
under Textual, or preemptively wrap it in case it is replaced later.

Use pytest for tests and lightweight type hints where they clarify interfaces.
Ruff provides basic linting and formatting without making the toolchain the
project's architecture. Avoid annotation ceremony, unnecessary dependencies,
and environment-manager lock-in. Keep Unix-specific subprocess and terminal
behavior isolated and test non-rendering state logic where practical.

POSIX and Unix-like systems come first, text is UTF-8, and the base interface
must not require a GUI display server, root access, systemd, tmux, zellij, or a
particular SSH client. Preserve ordinary SSH usability and degrade gracefully
when terminal capabilities are limited. Textual handles much of the terminal
lifecycle, but txtDesk must still ensure clean cancellation, error handling,
and terminal restoration; leaving a terminal corrupted is a serious bug.

Prefer mature libraries over reimplementing terminal protocols, and establish
correct interaction and rendering before optimization.

Terminal behavior should eventually be validated with several `$TERM` values,
including conservative and feature-rich configurations. Such validation must
cover startup, resize, shutdown, error paths, and restoration.
