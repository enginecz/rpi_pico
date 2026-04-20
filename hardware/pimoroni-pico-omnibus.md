# Pimoroni Pico Omnibus

## Module

- Manufacturer: Pimoroni
- Product: Pico Omnibus
- Type: dual expander board for Raspberry Pi Pico add-ons
- Current use: connects the Raspberry Pi Pico to the Waveshare Pico-ePaper-2.9

## Purpose

The Pico Omnibus lets the project use Pico add-on boards while still leaving
another labelled connector area available for prototyping or future modules.

## How It Is Used In This Project

Current hardware stack:

```text
Raspberry Pi Pico 1
-> Pimoroni Pico Omnibus
-> Waveshare Pico-ePaper-2.9 B/W V2
```

## Beginner Notes

- The Omnibus is an expander, not a controller.
- It exposes the Pico pins on more than one connector.
- Add-ons connected through the Omnibus still share the same Pico pins.
- Future modules must be checked for pin conflicts before connecting them.
- Use the printed pin labels on the Omnibus to confirm orientation and pin names.

## Pin Conflict Rule

If the e-paper display uses a Pico pin, another module should not use that same
pin unless the interface is designed to be shared. For this project, treat the
e-paper pins as reserved until we intentionally design a shared bus.

## Source

- Pimoroni product page: <https://shop.pimoroni.com/products/pico-omnibus>

