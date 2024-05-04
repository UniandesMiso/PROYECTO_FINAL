import pygame

from src.ecs.components.c_surface import CSurface


def window_position(rect: pygame.Rect,
                    fixed: str,
                    surf: CSurface,
                    padding: int = 0) -> pygame.Vector2:
    x_0 = rect.x + rect.w
    y_0 = rect.y + rect.h

    if 'TOP_MIDDLE'.__eq__(fixed):
        x = (x_0 - surf.area.width) / 2
        return pygame.Vector2(x, padding)
    if 'TOP_LEFT'.__eq__(fixed):
        return pygame.Vector2(padding, padding)
    if 'TOP_RIGHT'.__eq__(fixed):
        x = (x_0 - surf.area.width) - padding
        return pygame.Vector2(x, padding)
    if 'MIDDLE'.__eq__(fixed):
        x = (x_0 - surf.area.width) / 2
        y = (y_0 - surf.area.height) / 2
        return pygame.Vector2(x, y)
    if 'BOTTOM_MIDDLE'.__eq__(fixed):
        x = (x_0 - surf.area.width) / 2
        y = (y_0 - surf.area.height) - padding
        return pygame.Vector2(x, y)
    if 'BOTTOM_LEFT'.__eq__(fixed):
        y = (y_0 - surf.area.height) - padding
        return pygame.Vector2(padding, y)
    if 'BOTTOM_RIGHT'.__eq__(fixed):
        x = (x_0 - surf.area.width) - padding
        y = (y_0 - surf.area.height) - padding
        return pygame.Vector2(x, y)
