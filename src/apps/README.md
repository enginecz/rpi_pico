# Apps

Small runnable MicroPython programs live here.

## Current Apps

- [blink_onboard_led.py](blink_onboard_led.py): blinks the Raspberry Pi Pico 1
  onboard LED on GPIO 25.
- [epaper_hello.py](epaper_hello.py): first Waveshare Pico-ePaper-2.9 B/W
  display test.
- [epaper_clear_test.py](epaper_clear_test.py): simple white/black/white e-paper
  clear test for checking the display hardware.
- [home_status.py](home_status.py): first useful e-paper screen with simple
  placeholders for future home data.
- [temperature_on_button.py](temperature_on_button.py): waits for a button on
  GP15, reads the Pico internal temperature sensor, and updates the e-paper
  display.
- [temperature_once_on_power.py](temperature_once_on_power.py): measures the
  Pico internal temperature once after power-on, updates the e-paper display,
  then waits in light sleep so USB can be unplugged. The screen shows only a
  large temperature value.

## Run With Thonny

1. Connect the Pico normally by USB.
2. Open `blink_onboard_led.py` in Thonny.
3. Make sure Thonny is connected to the Pico MicroPython interpreter.
4. Press Run.

The onboard LED should blink twice per second.

## Run The E-Paper Test

1. Connect the Pico normally by USB.
2. In Thonny, open `src/modules/waveshare_epaper_2in9.py`.
3. Save it to the Pico as `waveshare_epaper_2in9.py`.
4. Open `src/apps/epaper_hello.py` in Thonny.
5. Make sure Thonny is connected to the Pico MicroPython interpreter.
6. Press Run.

The e-paper display should refresh and show a short status message.

If the display shows nothing, save the latest
`src/modules/waveshare_epaper_2in9.py` to the Pico again, then rerun
`epaper_hello.py`.

If Thonny says the device is busy, press Stop/Restart backend. If that does not
work, unplug the Pico and plug it in again without holding `BOOTSEL`, then try
saving the file again.

If `epaper_hello.py` still shows noise, run `epaper_clear_test.py`. It should
refresh white, then black, then white again.

After both display tests work, run `home_status.py` as the first useful screen.

## Run Temperature On Button

1. Connect a normally open button between GP15 and GND.
2. Save `src/apps/temperature_on_button.py` to the Pico.
3. Run it from Thonny.
4. Press the button to update the e-paper display.

The Pico internal temperature sensor measures chip temperature, not accurate
room temperature. It is useful for learning the flow before adding an external
sensor.

## Run Temperature Once On Power

Save these files to the Pico root:

- `src/main.py` as `main.py`
- `src/apps/temperature_once_on_power.py` as `temperature_once_on_power.py`

`main.py` is only a small launcher. To autostart another app later, change the
import inside `src/main.py`.

After that:

1. Unplug USB power.
2. Plug USB power in.
3. Wait for the display update.
4. Unplug USB power again.

This manually simulates the future power-latch workflow.

When this autostart mode is active, connect the Pico and press Stop/Restart
backend in Thonny while the program is still running or refreshing the e-paper
display before uploading new code. If it has already reached long light sleep,
unplug it, plug it in again, and stop it quickly during startup.

Older troubleshooting probes live in `src/diagnostics/`. Use them only if the
normal display tests stop working.
