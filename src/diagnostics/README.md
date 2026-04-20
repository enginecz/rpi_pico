# Diagnostics

These files are kept for troubleshooting only. They are not part of the normal
beginner workflow.

## Files

- [epaper_busy_probe.py](epaper_busy_probe.py): reads the e-paper BUSY pin while
  toggling reset.
- [epaper_legacy_clear_test.py](epaper_legacy_clear_test.py): older Waveshare
  2.9 inch driver clear test used during display debugging.
- [epaper_official_pico_clear_test.py](epaper_official_pico_clear_test.py):
  clear test that imports an untouched official Waveshare Pico driver copied to
  the Pico as `pico_epaper_2_9_official.py`.
- [waveshare_epaper_2in9_legacy.py](waveshare_epaper_2in9_legacy.py): older
  2.9 inch driver probe.

## Normal Path

Use these normal project files first:

1. `src/modules/waveshare_epaper_2in9.py`
2. `src/apps/epaper_clear_test.py`
3. `src/apps/epaper_hello.py`
