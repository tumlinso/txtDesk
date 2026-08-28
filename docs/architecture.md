# Architecture direction

The following layers are a conceptual decomposition for guiding early work,
not a frozen class hierarchy or ABI.

## 1. Terminal/runtime layer

This layer owns the current terminal session: initialization and restoration,
screen ownership, capability detection and graceful degradation, resize
handling, rendering support, input collection, and the event loop. Platform-
dependent behavior should remain isolated here.

## 2. Desktop layer

The desktop coordinates focus, layout, surface placement and lifecycle, global
commands, and chrome such as status and title areas. It should depend on
generic surface behavior rather than the semantics of any particular
application.

## 3. Application/surface layer

Applications present terminal, file, process, status, and other interactive
surfaces. Early applications may be compiled directly into the executable.
There is not enough real use yet to design a stable plugin ABI; that boundary
should be stabilized only after multiple applications reveal common needs.

## 4. Provider/integration layer

Providers connect applications to external data or services such as Project
Control, Codex, telemetry sources, remote-control backends, and other host-
specific systems. Provider semantics must not leak into generic desktop
abstractions.

## Embedded terminals: PTY versus emulator

A PTY is necessary for running an interactive child process, but it is not
sufficient for embedding that process inside a rectangular pane. Once txtDesk
places a shell, Vim, Codex, or similar program in a pane, txtDesk is acting as a
terminal emulator and must correctly maintain VT/ANSI terminal state.

Do not construct a fake PTY pane or write a terminal emulator from scratch.
The future terminal application should use a mature terminal-state engine such
as libvterm, or another deliberately evaluated equivalent. No dependency is
selected or vendored during bootstrap. A first runnable desktop may instead
provide a safe full-screen shell escape until true embedded terminals exist.
