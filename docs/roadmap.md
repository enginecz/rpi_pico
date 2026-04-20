# Roadmap

The project should grow in small, understandable steps.

## Step 1: Project Structure And Documentation

Status: complete.

Create a clean repository layout and write enough documentation to make the next
steps clear. Do not add MicroPython code yet.

## Step 2: Fresh Pico Firmware

Status: complete.

Clean old files from the Pico and flash current MicroPython firmware for
Raspberry Pi Pico 1.

Expected result:

- Pico runs fresh MicroPython.
- Beginner can connect using Thonny or another simple tool.
- Repository has notes for the exact flashing process used.

## Step 3: First Program

Create a minimal LED blink program.

Expected result:

- Beginner learns where code lives.
- Beginner learns how to copy a file to the Pico.
- Onboard LED blinks.

## Step 4: E-Paper Display Hardware

Document wiring and connect the e-paper display.

Expected result:

- Pin choices are recorded.
- Required display driver/library is identified.
- Wiring is understandable enough to reproduce.

## Step 5: First E-Paper Program

Create a simple display program.

Expected result:

- Display shows a short text or simple shape.
- Display code is kept separate from the main app where practical.

## Step 6: More Functionality

Add future home-use modules one at a time.

Possible later examples:

- Room status display
- Clock or calendar display
- Sensor reading display
- Button-controlled mode switching
