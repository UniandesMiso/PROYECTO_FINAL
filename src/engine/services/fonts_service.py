import pygame


class FontsService:
    def __init__(self):
        self._fonts = {}

    def get_font(self, path: str, size: int) -> pygame.font.Font:
        if path not in self._fonts:
            self._fonts[(path, size)] = pygame.font.Font(path, size)
        return self._fonts[(path, size)]
