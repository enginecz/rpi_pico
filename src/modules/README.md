# Modules

Future hardware-specific MicroPython modules will live here.

## Current Modules

- [waveshare_epaper_2in9.py](waveshare_epaper_2in9.py): project copy of the
  official Waveshare Pico MicroPython driver for the Pico-ePaper-2.9 B/W
  display, with the demo block removed and small beginner-friendly aliases.

## Notes

The e-paper driver is based on Waveshare's official Pico MicroPython
`Pico_ePaper-2.9.py` file. It supports `framebuf` drawing, full refresh,
partial refresh, and 4-gray functions from the original driver.

When using Thonny, save this file to the Pico root as
`waveshare_epaper_2in9.py` before running `src/apps/epaper_hello.py`.

The default project alias `EPaper2in9` points to Waveshare's landscape class,
because that is the variant confirmed on the physical display.

Older troubleshooting drivers live in `src/diagnostics/`.
