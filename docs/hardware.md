# Hardware Notes

## Main Board

- Board: Raspberry Pi Pico 1, non-W
- Language: MicroPython
- Wireless networking: not available on this board

## Modularity Goal

Each hat or hardware module should have its own notes and, later, its own small
MicroPython module. This keeps the project understandable and makes it easier to
combine modules.

## Module Documentation Template

When adding a new module, record:

```text
Module name:
Purpose:
Power:
Pico pins used:
Required library:
Minimal test:
Known limitations:
```

## Pin Tracking

Pin usage should be documented before combining modules. This avoids two hats or
modules trying to use the same Pico pin for different purposes.

