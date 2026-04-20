# Button On GP15

## Purpose

This button is the first manual input for low-power display updates.

The first use is `src/apps/temperature_on_button.py`: press the button, measure
the Pico internal temperature sensor, update the e-paper display, then put the
display back to sleep.

## Wiring

Use a normally open push button.

| Button Side | Connect To |
| --- | --- |
| One side | GP15 |
| Other side | GND |

No external resistor is required for this first version. The program enables
the Pico's internal pull-up resistor.

## Logic

- Button not pressed: GP15 reads `1`
- Button pressed: GP15 is connected to GND and reads `0`

This is called active-low logic.

## Pin Choice

GP15 is used because the e-paper display already reserves GP8, GP9, GP10, GP11,
GP12, and GP13.

## Power Notes

This is only the first low-power software step. The Pico is still powered while
waiting for the button. The program uses `lightsleep()` between button checks,
but the Pico board, regulator, USB circuitry, and power LED still consume power.

For a later battery-focused version, use external power control so the button
turns the Pico on, the Pico updates the e-paper display, and then the Pico turns
itself off.
