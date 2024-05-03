import pygame

from src.ecs.components.c_surface import CSurface


def window_position(screen: pygame.Vector2, fixed: str, surf: CSurface, padding: int = 0) -> pygame.Vector2:
    if 'TOP_MIDDLE'.__eq__(fixed):
        x = (screen.x - surf.area.width) / 2
        return pygame.Vector2(x, padding)
    if 'TOP_LEFT'.__eq__(fixed):
        return pygame.Vector2(padding, padding)
    if 'TOP_RIGHT'.__eq__(fixed):
        x = (screen.x - surf.area.width) - padding
        return pygame.Vector2(x, padding)
    if 'MIDDLE'.__eq__(fixed):
        x = (screen.x - surf.area.width) / 2
        y = (screen.y - surf.area.height) / 2
        return pygame.Vector2(x, y)
    if 'BOTTOM_MIDDLE'.__eq__(fixed):
        x = (screen.x - surf.area.width) / 2
        y = (screen.y - surf.area.height) - padding
        return pygame.Vector2(x, y)
    if 'BOTTOM_LEFT'.__eq__(fixed):
        y = (screen.y - surf.area.height) - padding
        return pygame.Vector2(padding, y)
    if 'BOTTOM_RIGHT'.__eq__(fixed):
        x = (screen.x - surf.area.width) - padding
        y = (screen.y - surf.area.height) - padding
        return pygame.Vector2(x, y)
