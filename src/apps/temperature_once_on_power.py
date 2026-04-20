from machine import ADC, lightsleep
from utime import sleep_ms

from waveshare_epaper_2in9 import BLACK, WHITE, EPaper2in9


ADC_MAX = 65535
ADC_REFERENCE_VOLTAGE = 3.3
SAMPLES = 8


temperature_sensor = ADC(4)


SEGMENTS = {
    "0": "ABCEFG",
    "1": "CF",
    "2": "ACDEG",
    "3": "ACDFG",
    "4": "BCDF",
    "5": "ABDFG",
    "6": "ABDEFG",
    "7": "ACF",
    "8": "ABCDEFG",
    "9": "ABCDFG",
}


def read_internal_temperature_c():
    total = 0
    for _ in range(SAMPLES):
        total += temperature_sensor.read_u16()
        sleep_ms(20)

    raw = total / SAMPLES
    voltage = raw * ADC_REFERENCE_VOLTAGE / ADC_MAX
    return 27 - (voltage - 0.706) / 0.001721


def draw_segment(display, x, y, segment, color):
    width = 48
    height = 96
    thickness = 10

    if segment == "A":
        display.fill_rect(x + thickness, y, width - 2 * thickness, thickness, color)
    elif segment == "B":
        display.fill_rect(x, y + thickness, thickness, height // 2 - thickness, color)
    elif segment == "C":
        display.fill_rect(x + width - thickness, y + thickness, thickness, height // 2 - thickness, color)
    elif segment == "D":
        display.fill_rect(x + thickness, y + height // 2 - thickness // 2, width - 2 * thickness, thickness, color)
    elif segment == "E":
        display.fill_rect(x, y + height // 2 + thickness // 2, thickness, height // 2 - thickness, color)
    elif segment == "F":
        display.fill_rect(x + width - thickness, y + height // 2 + thickness // 2, thickness, height // 2 - thickness, color)
    elif segment == "G":
        display.fill_rect(x + thickness, y + height - thickness, width - 2 * thickness, thickness, color)


def draw_digit(display, digit, x, y, color):
    for segment in SEGMENTS[digit]:
        draw_segment(display, x, y, segment, color)


def draw_decimal_point(display, x, y, color):
    display.fill_rect(x, y + 86, 10, 10, color)


def draw_large_c(display, x, y, color):
    draw_segment(display, x, y, "A", color)
    draw_segment(display, x, y, "B", color)
    draw_segment(display, x, y, "E", color)
    draw_segment(display, x, y, "G", color)


def draw_large_temperature(display, temperature_c):
    text = "{:.1f}".format(temperature_c)
    x = 8
    y = 14

    for character in text:
        if character == ".":
            draw_decimal_point(display, x, y, BLACK)
            x += 20
        elif character == "-":
            display.fill_rect(x + 10, y + 45, 28, 10, BLACK)
            x += 58
        else:
            draw_digit(display, character, x, y, BLACK)
            x += 58

    draw_large_c(display, x + 6, y, BLACK)


def show_temperature(temperature_c):
    display = EPaper2in9()
    display.fill(WHITE)
    draw_large_temperature(display, temperature_c)
    display.display_Base(display.buffer)
    display.sleep()


print("temperature_once_on_power start")
temperature = read_internal_temperature_c()
print("temperature: {:.1f} C".format(temperature))
show_temperature(temperature)
print("done; safe to unplug USB")

while True:
    lightsleep(60_000)
