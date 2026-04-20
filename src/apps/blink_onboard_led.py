from machine import Pin
from time import sleep


# Raspberry Pi Pico 1 has its onboard LED connected to GPIO 25.
led = Pin(25, Pin.OUT)


while True:
    led.toggle()
    sleep(0.5)

