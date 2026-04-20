# Hardware Notes

## Main Board

- Board: Raspberry Pi Pico 1, non-W
- Language: MicroPython
- Wireless networking: not available on this board

## Current Display Module

- Module: Waveshare Pico-ePaper-2.9
- Variant: B/W V2
- Resolution: 296 x 128 pixels
- Interface: SPI
- Detailed notes: [hardware/pico-epaper-2.9.md](../hardware/pico-epaper-2.9.md)

## Current Expander Board

- Module: Pimoroni Pico Omnibus
- Purpose: connects the Pico to Pico add-on boards and leaves another labelled
  connector area available
- Detailed notes:
  [hardware/pimoroni-pico-omnibus.md](../hardware/pimoroni-pico-omnibus.md)

## Current Physical Stack

```text
Raspberry Pi Pico 1
-> Pimoroni Pico Omnibus
-> Waveshare Pico-ePaper-2.9 B/W V2
```

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

## Pins Currently Reserved

The Waveshare Pico-ePaper-2.9 uses these Pico pins:

| Pico Pin | Used By | Purpose |
| --- | --- | --- |
| VSYS | Pico-ePaper-2.9 | Power input |
| GND | Pico-ePaper-2.9 | Ground |
| GP8 | Pico-ePaper-2.9 | Data/command select |
| GP9 | Pico-ePaper-2.9 | SPI chip select |
| GP10 | Pico-ePaper-2.9 | SPI clock |
| GP11 | Pico-ePaper-2.9 | SPI MOSI |
| GP12 | Pico-ePaper-2.9 | Reset |
| GP13 | Pico-ePaper-2.9 | Busy signal |
