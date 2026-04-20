# Beginner Workflow

This project should be usable without advanced tooling.

## Recommended Tools

- Current development computer: PC running Kubuntu.
- Current editor setup: Visual Studio Code with Codex.
- Thonny for editing and copying files to the Pico.
- A USB cable that supports data, not only charging.
- Optional later tool: `mpremote` for command-line file copy and REPL access.

## Kubuntu Serial Permission

On Kubuntu, Thonny may see the Pico as `/dev/ttyACM0` but fail with
`Permission denied`. Add the current user to the `dialout` group:

```bash
sudo usermod -a -G dialout brutus
```

Then log out and back in, or reboot. Group changes do not usually apply to
already-open sessions.

## Basic Development Loop

1. Connect the Pico by USB.
2. Open the project on the computer.
3. Edit one small file.
4. Copy the file to the Pico.
5. Run or reset the Pico.
6. Observe the result.
7. Write down what changed if wiring or behavior changed.

## File Naming Convention

- `main.py` will be used later for the program that starts automatically on the
  Pico.
- Hardware-specific code should go under `src/modules/`.
- Small runnable examples should go under `src/apps/`.
- Shared beginner-friendly helper code should go under `src/lib/`.

## Before Adding Code

For every new module or hat, document:

- What hardware is connected.
- Which Pico pins are used.
- Which power pins are used.
- Any important safety limits or warnings.
- How to test the module in the simplest possible way.
