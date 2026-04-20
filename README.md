# Raspberry Pi Pico Home Platform

Beginner-friendly MicroPython project for a small modular Raspberry Pi Pico 1
based platform. The goal is to build simple home-use modules step by step, while
keeping the code easy to read, easy to copy to the Pico, and easy to combine
with different Pico hats.

## Target Hardware

- Raspberry Pi Pico 1, non-W
- MicroPython firmware
- USB connection to the development computer
- Future modules may include hats such as e-paper displays, sensors, buttons,
  relays, or other simple home-use peripherals

## Current Development Environment

- PC running Kubuntu
- Visual Studio Code
- Codex coding assistant

## Project Principles

- Make small, reviewable changes.
- Prefer simple MicroPython over clever abstractions.
- Keep beginner workflow visible in the documentation.
- Keep each hardware module separate enough that modules can be combined later.
- Do not add code before the project is ready for that step.

## Current Status

The Pico has been erased, flashed with fresh MicroPython firmware, and verified
in Thonny. No MicroPython program has been added yet.

## Planned Steps

1. Create the initial project structure and documentation only.
2. Clean old firmware and files from the Pico, then flash current MicroPython
   firmware for a fresh start.
3. Create the first very simple program, such as blinking the onboard LED.
4. Connect an e-paper display.
5. Create a simple program using the e-paper display.
6. Add more functionality in small modular steps.

## Repository Layout

```text
.
├── docs/        General beginner documentation and project notes
├── firmware/    Firmware download and flashing notes
├── hardware/    Hardware wiring notes and module/hats documentation
└── src/         Future MicroPython source files
    ├── apps/    Future runnable examples or small applications
    ├── lib/     Future shared helper code
    └── modules/ Future hardware-specific modules
```

## How To Run

There is nothing to run yet. The first runnable program will be added in a later
step after the Pico has fresh MicroPython firmware installed.

## Next Recommended Step

Create the first beginner program: blink the onboard LED.
