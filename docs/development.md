# Development conventions

The current engineering preference is C++20, CMake, and old-school Unix source
naming: `.cc`, `.hh`, and `.inl` only where an inline implementation is
semantically useful. POSIX and Unix-like systems come first, text is UTF-8, and
the base interface must not require a GUI display server, root access,
systemd, tmux, zellij, or a particular SSH client.

Use a lightweight terminal UI substrate such as ncursesw unless later evidence
supports an equivalent. Keep platform-dependent terminal/runtime code
isolated. Use RAII for terminal and session restoration: leaving a user's
terminal corrupted after normal exit or a recoverable failure is a serious
bug.

Enable useful compiler warnings and test non-rendering logic where practical.
Avoid unnecessary dependencies, prefer mature libraries over reimplementing
terminal protocols, and establish rendering correctness before optimization.
Preserve usability through ordinary SSH sessions and degrade gracefully when
terminal capabilities are limited rather than assuming a rich terminal.

Terminal behavior should eventually be validated with several `$TERM` values,
including conservative and feature-rich configurations. Such validation must
cover startup, resize, shutdown, error paths, and restoration.
