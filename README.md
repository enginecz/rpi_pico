# Raspberry Pi Pico Home Platform

Beginner-friendly MicroPython project for a small modular Raspberry Pi Pico 1
based platform. The goal is to build simple home-use modules step by step, while
keeping the code easy to read, easy to copy to the Pico, and easy to combine
with different Pico hats.

## Target Hardware

- Raspberry Pi Pico 1, non-W
- MicroPython firmware
- USB connection to the development computer
- First display module: Waveshare Pico-ePaper-2.9, 296 x 128 pixels, B/W V2
- First input: normally open button between GP15 and GND
- Future modules may include sensors, buttons, relays, or other simple home-use
  peripherals

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
- Keep all repository documentation, code comments, filenames, and user-facing
  program text in English.

## Current Status

The Pico has been erased, flashed with fresh MicroPython firmware, and verified
in Thonny. The first beginner LED blink program works. The Waveshare
Pico-ePaper-2.9 B/W display is connected and working with a clean clear test
and a first hello display program. A first small home status screen has been
added as the next application step. A button-triggered internal temperature
display program has been added as the first power-aware app.

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
└── src/         MicroPython source files
    ├── apps/    Runnable examples or small applications
    ├── diagnostics/ Troubleshooting scripts kept out of the normal workflow
    ├── lib/     Future shared helper code
    └── modules/ Future hardware-specific modules
```

## How To Run

Run the LED blink program:

1. Connect the Pico normally by USB.
2. Open Thonny.
3. Open `src/apps/blink_onboard_led.py`.
4. Make sure Thonny is connected to the Pico MicroPython interpreter.
5. Press Run.

The onboard LED should blink twice per second.

Run the first e-paper test:

1. Connect the Pico normally by USB.
2. In Thonny, open `src/modules/waveshare_epaper_2in9.py`.
3. Save it to the Pico as `waveshare_epaper_2in9.py`.
4. Open `src/apps/epaper_hello.py`.
5. Make sure Thonny is connected to the Pico MicroPython interpreter.
6. Press Run.

The e-paper display should refresh and show a short status message.

Run the first home status screen:

1. Make sure `src/modules/waveshare_epaper_2in9.py` is saved to the Pico as
   `waveshare_epaper_2in9.py`.
2. Open `src/apps/home_status.py`.
3. Press Run.

Run the button-triggered temperature screen:

1. Connect a normally open button between GP15 and GND.
2. Make sure `src/modules/waveshare_epaper_2in9.py` is saved to the Pico as
   `waveshare_epaper_2in9.py`.
3. Open `src/apps/temperature_on_button.py`.
4. Press Run.
5. Press the GP15 button to measure and update the display.

Run the manual power-cycle temperature screen:

1. Save `src/main.py` to the Pico as `main.py`.
2. Save `src/apps/temperature_once_on_power.py` to the Pico as
   `temperature_once_on_power.py`.
3. Unplug USB power.
4. Plug USB power in.
5. Wait for the display update.
6. Unplug USB power again.

When this autostart mode is active, `main.py` starts immediately after USB power
is connected. To upload new code, open Thonny right after connecting the Pico and
press Stop/Restart backend while the program is still running or refreshing the
e-paper display. After the program reaches long light sleep, upload tools may
have trouble interrupting it.

## Next Recommended Step

Replace the Pico internal temperature reading with a low-power external
temperature sensor.
