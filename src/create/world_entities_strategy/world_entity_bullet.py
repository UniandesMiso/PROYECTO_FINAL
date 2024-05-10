import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_bullet_tag import CBulletTag


class WorldEntityBullet(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        size: pygame.Vector2 = kwargs.get('size')
        color: pygame.Color = kwargs.get('color')
        velocity: pygame.Vector2 = pygame.Vector2(0, kwargs.get('velocity'))
        position: pygame.Vector2 = kwargs.get('position')
        world.add_component(cuad_entity, CSurface(size, color))
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CVelocity(velocity))
        world.add_component(cuad_entity, kwargs.get('tag'))
        return cuad_entity
