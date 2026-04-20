# Waveshare Pico-ePaper-2.9

## Module

- Manufacturer: Waveshare
- Product: Pico-ePaper-2.9
- Variant: B/W V2
- Display size: 2.9 inch
- Resolution: 296 x 128 pixels
- Colors: black and white
- Interface: SPI
- Target board: Raspberry Pi Pico 1, non-W

## Purpose

This will be the first display module for the project. It can be used later for
simple home status screens, sensor readouts, reminders, or low-power information
panels.

## Connection Type

This is a Pico-shaped display module. In the current project setup, it is
attached to the Pico through a Pimoroni Pico Omnibus board.

Current physical stack:

```text
Raspberry Pi Pico 1
-> Pimoroni Pico Omnibus
-> Waveshare Pico-ePaper-2.9 B/W V2
```

If wiring by cable instead, use the pin table below.

## Pin Usage

| E-Paper Pin | Pico Pin | Purpose |
| --- | --- | --- |
| VCC | VSYS | Power input |
| GND | GND | Ground |
| DIN | GP11 | SPI MOSI, data from Pico to display |
| CLK | GP10 | SPI SCK, clock |
| CS | GP9 | SPI chip select, active low |
| DC | GP8 | Data/command select |
| RST | GP12 | Reset, active low |
| BUSY | GP13 | Display busy signal |

## Beginner Notes

- E-paper refreshes slowly compared with normal screens.
- The display may flicker during a full refresh; this is normal.
- Avoid refreshing the display in a very fast loop.
- Put the display into sleep mode later when the driver supports it.
- Double-check the physical orientation before attaching boards together.
- The Pico Omnibus exposes shared Pico pins; it does not remove pin conflicts.

## Required Library

Selected driver: local MicroPython driver at
`src/modules/waveshare_epaper_2in9.py`.

The driver is based on Waveshare's official Pico MicroPython
`Pico_ePaper-2.9.py` file, with the original demo block removed and small
project aliases added.

The key source that finally solved the display refresh problem was the official
Waveshare Pico MicroPython driver:
<https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico_ePaper-2.9.py>

The default project class `EPaper2in9` uses Waveshare's landscape framebuffer
variant, because that variant was confirmed working on the physical display.

## Minimal Test

Implemented at `src/apps/epaper_hello.py`.

## Known Limitations

- Full refresh only.
- No partial refresh yet.
- No grayscale mode yet.
- Pin conflicts with future hats or modules must be checked before combining
  hardware.

## Troubleshooting

If running `src/apps/epaper_hello.py` shows nothing:

1. Press Stop/Restart backend in Thonny.
2. If Thonny says the device is busy, unplug the Pico and plug it in again
   without holding `BOOTSEL`.
3. Save the latest `src/modules/waveshare_epaper_2in9.py` to the Pico again.
4. Confirm it is saved on the Pico as `waveshare_epaper_2in9.py`.
5. Run `src/apps/epaper_hello.py` again from Thonny.
6. Watch the Thonny Shell for errors.
7. Check whether the e-paper display flickers during refresh.

If there is no flicker and no visible change, check the physical orientation of
the Pico, Pico Omnibus, and e-paper board.

The previous local wrapper timed out during display refresh. The current driver
uses the confirmed-working official Pico MicroPython implementation instead.

If the display flickers but leaves black/white noise again, first confirm that
the current `src/modules/waveshare_epaper_2in9.py` was saved to the Pico root as
`waveshare_epaper_2in9.py`. The current project driver should behave like the
confirmed-working official Waveshare Pico driver.

## Source

- Waveshare wiki: <https://www.waveshare.com/wiki/Pico-ePaper-2.9>
- Waveshare Pico e-paper demo repository:
  <https://github.com/waveshareteam/Pico_ePaper_Code>
- Confirmed working Pico MicroPython driver:
  <https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico_ePaper-2.9.py>
