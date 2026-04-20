from machine import Pin
from time import sleep


busy = Pin(13, Pin.IN)
reset = Pin(12, Pin.OUT)

print("initial busy:", busy.value())

print("reset high")
reset.value(1)
sleep(1)
print("busy:", busy.value())

print("reset low")
reset.value(0)
sleep(1)
print("busy:", busy.value())

print("reset high")
reset.value(1)
sleep(1)
print("busy:", busy.value())

print("done")
