import time


class CBlink:
    def __init__(self, rate: float) -> None:
        self.last = time.time()
        self.rate = rate
        self.visible = True
