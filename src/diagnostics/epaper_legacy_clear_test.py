from time import sleep

from waveshare_epaper_2in9_legacy import EPaper2in9Legacy


display = EPaper2in9Legacy()
display.init()

print("legacy clear white")
display.Clear(0xFF)
sleep(5)

print("legacy clear black")
display.Clear(0x00)
sleep(5)

print("legacy clear white")
display.Clear(0xFF)

display.sleep()
print("done")
