import pygame

from src.ecs.components.c_surface import CSurface


def window_position(rect: pygame.Rect,
                    fixed: str,
                    surf: CSurface,
                    padding: int) -> pygame.Vector2:
    if 'TOP_LEFT'.__eq__(fixed):
        y = rect.top
        x = rect.left
        return pygame.Vector2(x, y)

    if 'TOP_MIDDLE'.__eq__(fixed):
        y = rect.top
        x = (rect.left + rect.width - surf.area.width) / 2
        return pygame.Vector2(x, y)

    if 'TOP_RIGHT'.__eq__(fixed):
        y = rect.top
        x = rect.left + rect.width - surf.area.width
        return pygame.Vector2(x, y)

    if 'MIDDLE_LEFT'.__eq__(fixed):
        y = rect.top + (rect.height - surf.area.height) / 2
        x = rect.left
        return pygame.Vector2(x, y)

    if 'MIDDLE'.__eq__(fixed):
        y = rect.top + (rect.height - surf.area.height) / 2
        x = (rect.left + rect.width - surf.area.width) / 2
        return pygame.Vector2(x, y)

    if 'MIDDLE_RIGHT'.__eq__(fixed):
        y = rect.top + (rect.height - surf.area.height) / 2
        x = rect.left + rect.width - surf.area.width
        return pygame.Vector2(x, y)

    if 'BOTTOM_LEFT'.__eq__(fixed):
        y = rect.top + rect.height - surf.area.height
        x = rect.left
        return pygame.Vector2(x, y)

    if 'BOTTOM_MIDDLE'.__eq__(fixed):
        y = rect.top + rect.height - surf.area.height
        x = (rect.left + rect.width - surf.area.width) / 2
        return pygame.Vector2(x, y)

    if 'BOTTOM_RIGHT'.__eq__(fixed):
        y = rect.top + rect.height - surf.area.height
        x = rect.left + rect.width - surf.area.width
        return pygame.Vector2(x, y)
