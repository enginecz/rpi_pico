from waveshare_epaper_2in9 import BLACK, WHITE, EPaper2in9


display = EPaper2in9()

display.fill(WHITE)
display.text("Pico Home", 8, 12, BLACK)
display.text("ePaper OK", 8, 32, BLACK)
#display.rect(0, 0, 132, 48, BLACK)
display.hline(8, 64, 260, BLACK)
display.text("Waveshare Pico-ePaper-2.9", 8, 82, BLACK)
display.text("Pico Omnibus", 8, 104, BLACK)
display.rect(208, 12, 32, 32, BLACK)
display.fill_rect(0, 0, 32, 32, BLACK)

display.display_Base(display.buffer)
display.sleep()
