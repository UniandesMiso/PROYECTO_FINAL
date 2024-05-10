from enum import Enum


class FontType(Enum):
    STATIC = 0
    PLAYER = 1
    READY = 2
    PAUSE = 3
    GAME_OVER = 4
    SCORE = 5


class CFontTag:
    def __init__(self, font_type: FontType) -> None:
        self.font_type = font_type
        self.time = 0
