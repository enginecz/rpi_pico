from waveshare_epaper_2in9 import BLACK, WHITE, EPaper2in9


display = EPaper2in9()

display.fill(WHITE)

display.text("Pico Home Status", 8, 8, BLACK)
display.hline(8, 22, 280, BLACK)

display.text("Time", 8, 34, BLACK)
display.text("--:--", 88, 34, BLACK)

display.text("Temperature", 8, 54, BLACK)
display.text("--.- C", 120, 54, BLACK)

display.text("System", 8, 74, BLACK)
display.text("OK", 88, 74, BLACK)

display.text("Next", 8, 98, BLACK)
display.text("Add sensor", 88, 98, BLACK)

display.rect(232, 34, 48, 48, BLACK)
display.line(232, 34, 280, 82, BLACK)
display.line(280, 34, 232, 82, BLACK)

display.display_Base(display.buffer)
display.sleep()
