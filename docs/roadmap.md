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

Status: complete.

Create a minimal LED blink program.

Expected result:

- Beginner learns where code lives.
- Beginner learns how to copy a file to the Pico.
- Onboard LED blinks.

## Step 4: E-Paper Display Hardware

Status: complete.

Document wiring and connect the e-paper display.

Expected result:

- Pin choices are recorded.
- Required display driver/library is identified.
- Wiring is understandable enough to reproduce.

## Step 5: First E-Paper Program

Status: complete.

Create a simple display program.

Expected result:

- Display shows a short text or simple shape.
- Display code is kept separate from the main app where practical.

Completed result:

- `src/apps/epaper_clear_test.py` refreshes white, black, then white.
- `src/apps/epaper_hello.py` shows a simple text and shape screen.
- `src/modules/waveshare_epaper_2in9.py` is based on the confirmed-working
  official Waveshare Pico MicroPython driver.

## Step 6: More Functionality

Status: started.

Add future home-use modules one at a time.

Current result:

- `src/apps/home_status.py` shows a static home status screen with placeholders
  for future time, temperature, and system data.

Possible later examples:

- Room status display
- Clock or calendar display
- Sensor reading display
- Button-controlled mode switching
