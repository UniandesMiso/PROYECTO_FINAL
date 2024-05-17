import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_blink import CBlink
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_start_tag import CStartTag


class WorldEntityStart(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        size = pygame.Vector2(1, 1)
        color: pygame.Color = kwargs.get('color')
        velocity = CVelocity(pygame.Vector2(0, kwargs.get('velocity')))
        position: pygame.Vector2 = kwargs.get('position')
        world.add_component(cuad_entity, CSurface(size, color))
        world.add_component(cuad_entity, velocity)
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CBlink(kwargs.get('blink')))
        world.add_component(cuad_entity, CStartTag())

        return cuad_entity
