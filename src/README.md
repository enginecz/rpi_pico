# Source

This folder contains MicroPython code for the Pico.

Current beginner apps:

- [main.py](main.py): tiny autostart launcher to copy to the Pico root as
  `main.py`. Change its import to choose which app starts on power-up.
- [apps/blink_onboard_led.py](apps/blink_onboard_led.py)
- [apps/epaper_clear_test.py](apps/epaper_clear_test.py)
- [apps/epaper_hello.py](apps/epaper_hello.py)
- [apps/home_status.py](apps/home_status.py)
- [apps/temperature_on_button.py](apps/temperature_on_button.py)
- [apps/temperature_once_on_power.py](apps/temperature_once_on_power.py)

## Subfolders

- `apps/`: small runnable programs or examples.
- `diagnostics/`: troubleshooting scripts kept out of the normal beginner
  workflow.
- `lib/`: simple shared helper code.
- `modules/`: hardware-specific modules, one module per device or hat where
  practical.
