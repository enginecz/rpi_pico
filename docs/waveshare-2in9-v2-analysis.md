# Waveshare 2.9 Inch V2 Analysis

This note records what was found while debugging the Waveshare 2.9 inch
black/white V2 e-paper display.

## Folder Scope

`E-Paper_code/` was a large Waveshare multi-platform package temporarily added
during debugging. It was not a Raspberry Pi Pico MicroPython package and has
been removed from the project.

Relevant folders for 2.9 inch V2:

- `E-Paper_code/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9_V2.py`
- `E-Paper_code/RaspberryPi_JetsonNano/python/examples/epd_2in9_V2_test.py`
- `E-Paper_code/RaspberryPi_JetsonNano/c/lib/e-Paper/EPD_2in9_V2.c`
- `E-Paper_code/RaspberryPi_JetsonNano/c/examples/EPD_2in9_V2_test.c`
- `E-Paper_code/Arduino/epd2in9_V2/epd2in9_V2.cpp`
- `E-Paper_code/Arduino/epd2in9_V2/epd2in9_V2.h`

## Important Difference From Our Current Driver

The Raspberry Pi/Jetson Python driver and the Arduino/C style driver are very
similar, but not byte-for-byte identical.

Observed full-refresh LUT difference:

```text
local current driver WS_20_30 byte 66: 0x01
RaspberryPi_JetsonNano python WS_20_30 byte 66: 0x02
Arduino epd2in9_V2 WS_20_30 byte 66: 0x01
```

Because the user-provided folder is the intended reference now, the next driver
attempt should follow the Raspberry Pi/Jetson Python `epd2in9_V2.py` first.

## V2 Display Basics

- Resolution: 128 x 296 pixels
- Color mode: black/white, with optional 4-gray support in Waveshare examples
- BUSY behavior in Waveshare code: `1` means busy, `0` means idle
- Full refresh command sequence:

```text
0x22
0xC7
0x20
wait busy release
```

## Waveshare Init Sequence

From `epd2in9_V2.py`, normal init is:

```text
reset
wait busy
0x12              software reset
wait busy
0x01 27 01 00     driver output control
0x11 03           data entry mode
0x44 00 0F        RAM X window
0x45 00 00 27 01  RAM Y window
0x21 00 80        display update control
0x4E 00           RAM X cursor
0x4F 00 00        RAM Y cursor
wait busy
set LUT WS_20_30
```

## Clear Behavior

The Raspberry Pi/Jetson Python driver `Clear()` is not the same as our latest
diagnostic clear. It does:

```text
write 0x24 RAM with color
refresh
write 0x26 RAM with color
refresh
```

Our recent diagnostic driver wrote both RAM areas first and refreshed once. The
next clean-room attempt should copy Waveshare's `Clear()` sequence exactly.

## Buffer Behavior

The Raspberry Pi/Jetson Python `getbuffer()` builds a list of bytes initialized
to `0xFF`. For vertical images:

```text
black pixel clears bit: buf[(x + y * width) / 8] &= ~(0x80 >> (x % 8))
```

This corresponds to a 128 x 296 portrait buffer with MSB-first horizontal bits.

## Pin Notes

The generic Raspberry Pi/Jetson package pin numbers are for Raspberry Pi BCM
pins, not Pico pins.

For the Pico-ePaper board, keep the Pico pin mapping from the Waveshare Pico
documentation:

| Function | Pico Pin |
| --- | --- |
| RST | GP12 |
| DC | GP8 |
| CS | GP9 |
| BUSY | GP13 |
| CLK | GP10 |
| DIN / MOSI | GP11 |

## Next Driver Direction

For the next attempt:

1. Port `E-Paper_code/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9_V2.py`
   directly to MicroPython.
2. Keep method names close to Waveshare: `init`, `Clear`, `display`,
   `display_Base`, `ReadBusy`, `SetLut`.
3. Use the Python driver's `WS_20_30` table exactly, including byte 66 as `0x02`.
4. Implement `Clear()` exactly as Waveshare does: refresh after `0x24`, then
   refresh after `0x26`.
5. Only after a clean white/black clear works, add beginner-friendly wrappers.

## Official Pico Python Driver

The most relevant official source for this project is now the Waveshare Pico
MicroPython driver:

<https://github.com/waveshareteam/Pico_ePaper_Code/blob/main/python/Pico_ePaper-2.9.py>

This is different from the RaspberryPi/JetsonNano driver because it is already
written for Pico MicroPython.

Important Pico-specific observations:

- `BUSY_PIN` is configured as `Pin(BUSY_PIN, Pin.IN, Pin.PULL_UP)`.
- `Clear()` writes both `0x24` and `0x26` RAM areas first, then refreshes once.
- The demo opens the `Pico_ePaper-xxx.py` file directly in Thonny.

The no-wrapper hardware check passed when the official file was copied to the
Pico as `pico_epaper_2_9_official.py` and run through
`src/diagnostics/epaper_official_pico_clear_test.py`.

## Local Port Status

`src/modules/waveshare_epaper_2in9.py` is now based directly on the official
Pico MicroPython `Pico_ePaper-2.9.py` file:

- The original demo block was removed.
- `WHITE`, `BLACK`, `EPaper2in9`, `EPaper2in9Portrait`, and
  `EPaper2in9Landscape` aliases were added for beginner-friendly project code.
- `EPaper2in9` points to the landscape class because that variant passed the
  physical display test.

Current hardware result:

- The official Pico driver works on the physical display.
- The earlier local wrapper timed out during `display refresh`, so it has been
  replaced as the main driver path.

## Legacy 2.9 Inch Probe

Because the early V2 wrapper reached refresh and then stalled, a separate
diagnostic driver was kept at `src/diagnostics/waveshare_epaper_2in9_legacy.py`.

It ports:

```text
E-Paper_code/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9.py
```

This is not replacing the V2 driver. It is a controlled test for the older
Waveshare 2.9 inch init/refresh sequence:

```text
0x01 driver output control
0x0C booster soft start
0x2C VCOM
0x3A dummy line period
0x3B gate time
0x11 data entry mode
0x32 30-byte LUT
0x22 0xC4
0x20
0xFF
wait busy release
```

Run `src/diagnostics/epaper_legacy_clear_test.py` only after saving
`src/diagnostics/waveshare_epaper_2in9_legacy.py` to the Pico root as
`waveshare_epaper_2in9_legacy.py`.
