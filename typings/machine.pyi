class Pin:
    IN: int
    OUT: int
    PULL_UP: int

    def __init__(self, pin: int, mode: int = ..., pull: int = ...) -> None: ...
    def value(self, value: int | None = ...) -> int: ...
    def __call__(self, value: int | None = ...) -> int: ...


class ADC:
    def __init__(self, channel: int | Pin) -> None: ...
    def read_u16(self) -> int: ...


class SPI:
    def __init__(
        self,
        channel: int,
        baudrate: int = ...,
        polarity: int = ...,
        phase: int = ...,
        sck: Pin | None = ...,
        mosi: Pin | None = ...,
        miso: Pin | None = ...,
    ) -> None: ...
    def init(self, baudrate: int = ...) -> None: ...
    def write(self, data: bytes | bytearray) -> None: ...


def lightsleep(ms: int | None = ...) -> None: ...
