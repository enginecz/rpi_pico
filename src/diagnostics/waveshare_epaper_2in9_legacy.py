from machine import Pin, SPI
from time import sleep_ms, ticks_diff, ticks_ms


# Close MicroPython port of:
# E-Paper_code/RaspberryPi_JetsonNano/python/lib/waveshare_epd/epd2in9.py
#
# This is intentionally kept separate from waveshare_epaper_2in9.py.
# It is a hardware probe for panels that do not respond correctly to the
# Waveshare 2.9 V2 init sequence.

EPD_WIDTH = 128
EPD_HEIGHT = 296

RST_PIN = 12
DC_PIN = 8
CS_PIN = 9
BUSY_PIN = 13
CLK_PIN = 10
MOSI_PIN = 11

BUSY_TIMEOUT_MS = 60_000


class EPaper2in9Legacy:
    lut_full_update = [
        0x50, 0xAA, 0x55, 0xAA, 0x11, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0xFF, 0xFF, 0x1F, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]

    lut_partial_update = [
        0x10, 0x18, 0x18, 0x08, 0x18, 0x18,
        0x08, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x13, 0x14, 0x44, 0x12,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]

    def __init__(self):
        self.reset_pin = Pin(RST_PIN, Pin.OUT)
        self.dc_pin = Pin(DC_PIN, Pin.OUT)
        self.cs_pin = Pin(CS_PIN, Pin.OUT)
        self.busy_pin = Pin(BUSY_PIN, Pin.IN, Pin.PULL_UP)

        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT

        self.cs_pin(1)
        self.dc_pin(0)
        self.reset_pin(1)

        self.spi = SPI(
            1,
            baudrate=4_000_000,
            polarity=0,
            phase=0,
            sck=Pin(CLK_PIN),
            mosi=Pin(MOSI_PIN),
        )
        self._one_byte = bytearray(1)

    def reset(self):
        self.reset_pin(1)
        sleep_ms(200)
        self.reset_pin(0)
        sleep_ms(5)
        self.reset_pin(1)
        sleep_ms(200)

    def send_command(self, command):
        self.dc_pin(0)
        self.cs_pin(0)
        self._one_byte[0] = command
        self.spi.write(self._one_byte)
        self.cs_pin(1)

    def send_data(self, data):
        self.dc_pin(1)
        self.cs_pin(0)
        self._one_byte[0] = data
        self.spi.write(self._one_byte)
        self.cs_pin(1)

    def ReadBusy(self, step="busy", raise_on_timeout=True):
        print("legacy e-Paper busy:", step, "pin:", self.busy_pin())
        started_at = ticks_ms()
        while self.busy_pin() == 1:
            if ticks_diff(ticks_ms(), started_at) > BUSY_TIMEOUT_MS:
                if raise_on_timeout:
                    raise RuntimeError("legacy e-paper busy timeout during " + step)
                print(
                    "legacy e-Paper busy timeout ignored:",
                    step,
                    "pin:",
                    self.busy_pin(),
                )
                return False
            sleep_ms(200)
        print("legacy e-Paper busy release:", step, "pin:", self.busy_pin())
        return True

    def TurnOnDisplay(self):
        self.send_command(0x22)
        self.send_data(0xC4)
        self.send_command(0x20)
        self.send_command(0xFF)
        self.ReadBusy("display refresh")

    def SetWindow(self, x_start, y_start, x_end, y_end):
        self.send_command(0x44)
        self.send_data((x_start >> 3) & 0xFF)
        self.send_data((x_end >> 3) & 0xFF)
        self.send_command(0x45)
        self.send_data(y_start & 0xFF)
        self.send_data((y_start >> 8) & 0xFF)
        self.send_data(y_end & 0xFF)
        self.send_data((y_end >> 8) & 0xFF)

    def SetCursor(self, x, y):
        self.send_command(0x4E)
        self.send_data((x >> 3) & 0xFF)
        self.send_command(0x4F)
        self.send_data(y & 0xFF)
        self.send_data((y >> 8) & 0xFF)
        self.ReadBusy("set cursor", raise_on_timeout=False)

    def init(self, lut=None):
        if lut is None:
            lut = self.lut_full_update

        self.reset()

        self.send_command(0x01)
        self.send_data((EPD_HEIGHT - 1) & 0xFF)
        self.send_data(((EPD_HEIGHT - 1) >> 8) & 0xFF)
        self.send_data(0x00)

        self.send_command(0x0C)
        self.send_data(0xD7)
        self.send_data(0xD6)
        self.send_data(0x9D)

        self.send_command(0x2C)
        self.send_data(0xA8)

        self.send_command(0x3A)
        self.send_data(0x1A)

        self.send_command(0x3B)
        self.send_data(0x08)

        self.send_command(0x11)
        self.send_data(0x03)

        self.send_command(0x32)
        for value in lut:
            self.send_data(value)

        return 0

    def Clear(self, color=0xFF):
        self.SetWindow(0, 0, self.width - 1, self.height - 1)
        for y in range(self.height):
            self.SetCursor(0, y)
            self.send_command(0x24)
            for _ in range(self.width // 8):
                self.send_data(color)
        self.TurnOnDisplay()

    def sleep(self):
        self.send_command(0x10)
        self.send_data(0x01)
        sleep_ms(2000)


EPD = EPaper2in9Legacy
