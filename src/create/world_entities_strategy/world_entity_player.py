import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_player_state import CPlayerState
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_player_tag import CPlayerTag
from src.engine.service_locator import ServiceLocator


class WorldEntityPlayer(WorldEntityStrategy):

    def create_entity(self, world: esper.World, **kwargs) -> int:
        cuad_entity = world.create_entity()
        img_surf: pygame.Surface = CSurface.from_surface(kwargs.get('image')) if kwargs.get('image') else None
        world.add_component(cuad_entity, img_surf)
        world.add_component(cuad_entity, CTransform(kwargs.get('position')))
        world.add_component(cuad_entity, CVelocity(kwargs.get('velocity')))
        world.add_component(cuad_entity, CAnimation(kwargs.get('animations')))
        world.add_component(cuad_entity, CPlayerState())
        world.add_component(cuad_entity, CPlayerTag())
        if kwargs.get('sound'):
            ServiceLocator.sounds_services.play(kwargs.get('sound'))
        return cuad_entity
