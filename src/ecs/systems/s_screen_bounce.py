import esper
import pygame

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_enemy_tag import CEnemyTag
from src.ecs.components.tags.c_player_tag import CPlayerTag


def system_enemy_screen_bounce(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CVelocity, CSurface, CEnemyTag)
    screen_rect = screen.get_rect()

    c_t: CTransform
    c_v: CVelocity
    c_s: CSurface
    c_e: CEnemyTag

    for _, (c_t, c_v, c_s, c_e) in components:
        cuad_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        if cuad_rect.left < 0 or cuad_rect.right > screen_rect.width:
            c_v.vel.x *= -1
            cuad_rect.clamp_ip(screen_rect)
            #c_t.pos.x = cuad_rect.x


def system_players_screen_bounce(world: esper.World, screen: pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CVelocity, CSurface, CPlayerTag)

    c_t: CTransform
    c_v: CVelocity
    c_s: CSurface
    c_p: CPlayerTag

    for _, (c_t, c_v, c_s, c_p) in components:
        cuad_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        if (cuad_rect.left < 0 or cuad_rect.right > screen_rect.width) or (
                cuad_rect.top < 0 or cuad_rect.bottom > screen_rect.height):
            cuad_rect.clamp_ip(screen_rect)
            c_t.pos.y = cuad_rect.y
            c_t.pos.x = cuad_rect.x
