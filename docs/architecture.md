# Architecture direction

The following layers are a conceptual decomposition for guiding early work,
not a frozen class hierarchy or ABI.

## 1. Runtime/application layer

Textual currently provides the terminal application substrate: event loop,
rendering, widgets, layout primitives, focus mechanics, input events, resize,
and terminal lifecycle. txtDesk should use those facilities directly and add
only the desktop-wide lifecycle, commands, state, and policy it actually needs.
Do not recreate Textual behind a parallel framework or a speculative wrapper
layer. Platform-dependent behavior should remain contained.

## 2. Desktop layer

The desktop coordinates application lifecycle, focus policy, composition and
surface placement, global commands, shared configuration, and chrome such as
status and title areas. It should use Textual primitives where they fit and
remain independent of any particular application's semantics.

## 3. Application/surface layer

Applications present terminal, file, process, status, and other interactive
surfaces. Early applications may ship directly in the Python package. There is
not enough real use yet to design a stable plugin API or ABI; an extension
boundary should stabilize only after multiple applications reveal common
needs.

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
A future terminal surface must combine PTY/subprocess lifecycle, proper VT/ANSI
state parsing and emulation, screen-buffer state, input forwarding, resize
propagation, and rendering into a txtDesk surface. Dumping PTY bytes into a
widget is not sufficient. Future work should evaluate mature Python-accessible
terminal engines or a well-contained native binding against actual
requirements. No backend is selected during bootstrap; an early desktop may
instead provide a safe full-screen shell escape.
