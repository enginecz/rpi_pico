from time import sleep

from pico_epaper_2_9_official import EPD_2in9_Landscape


print("official Pico driver: create display")
display = EPD_2in9_Landscape()

print("official Pico driver: clear white")
display.Clear(0xFF)
sleep(5)

print("official Pico driver: clear black")
display.Clear(0x00)
sleep(5)

print("official Pico driver: clear white")
display.Clear(0xFF)

display.sleep()
print("done")
