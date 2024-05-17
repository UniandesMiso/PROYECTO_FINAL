import pygame

import esper
from src.ecs.components.c_blink import CBlink
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform


def system_rendering(world: esper.World, screen: pygame.Surface):
    components = world.get_components(CTransform, CSurface)

    c_t: CTransform
    c_s: CSurface

    for entity, (c_t, c_s) in components:
        blink = world.component_for_entity(entity, CBlink) if world.has_component(entity, CBlink) else None
        if not blink or blink.visible:
            screen.blit(c_s.surf, c_t.pos, area=c_s.area)
