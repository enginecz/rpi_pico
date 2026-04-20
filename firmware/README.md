# Firmware

This folder is for notes about MicroPython firmware used on the Raspberry Pi
Pico. Firmware files themselves do not need to be committed unless there is a
specific reason later.

## Current Status

Fresh MicroPython firmware setup was performed and verified on 2026-04-20.

## Board

- Raspberry Pi Pico 1, non-W
- BOOTSEL drive label: `RPI-RP2`

## Firmware Used

- Firmware: MicroPython for Raspberry Pi Pico
- Version: `v1.28.0`
- Release date: 2026-04-06
- File used locally: `RPI_PICO-20260406-v1.28.0.uf2`
- Official download page: <https://micropython.org/download/RPI_PICO/>

At the time of setup, MicroPython listed `v1.28.0` as the latest stable release
for `RPI_PICO`.

## Flash Erase Tool Used

- Tool: Raspberry Pi `flash_nuke.uf2`
- Purpose: erase the Pico flash before installing MicroPython
- Official download URL: <https://datasheets.raspberrypi.com/soft/flash_nuke.uf2>

This removes old programs and files from the Pico. Use it only when a fresh
start is intended.

## Process Performed

1. Connected the Pico in BOOTSEL mode.
2. Mounted the `RPI-RP2` drive at `/media/brutus/RPI-RP2`.
3. Downloaded official MicroPython firmware for `RPI_PICO`.
4. Downloaded Raspberry Pi `flash_nuke.uf2`.
5. Copied `flash_nuke.uf2` to `RPI-RP2` to erase the Pico flash.
6. Reconnected the Pico in BOOTSEL mode.
7. Copied `RPI_PICO-20260406-v1.28.0.uf2` to `RPI-RP2`.
8. The BOOTSEL drive disappeared after flashing, which is expected.

## Local Files

The downloaded `.uf2` files are kept locally in this folder for convenience, but
they are ignored by Git.

## Verification

The firmware file was checked locally with `file` and identified as a UF2 image
for Raspberry Pi RP2040.

After flashing, USB detected the board as:

```text
2e8a:0005 MicroPython Board in FS mode
```

Thonny later found the Pico at `/dev/ttyACM0`, but Kubuntu denied access because
the user was not in the `dialout` group. Run:

```bash
sudo usermod -a -G dialout brutus
```

Then log out and back in, or reboot, before trying Thonny again.

After reboot, Thonny connected to the Pico successfully.

The next project step is the first LED blink program.
