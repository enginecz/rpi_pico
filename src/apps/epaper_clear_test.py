from time import sleep

from waveshare_epaper_2in9 import EPaper2in9


display = EPaper2in9()

print("clear white")
display.Clear(0xFF)
sleep(5)

print("clear black")
display.Clear(0x00)
sleep(5)

print("clear white")
display.Clear(0xFF)
display.sleep()
print("done")
