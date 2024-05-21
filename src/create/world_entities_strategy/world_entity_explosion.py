import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_explosion_tag import CExplosionTag
from src.engine.service_locator import ServiceLocator


class WorldEntityExplosion(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        explosion_cfg: dict = kwargs.get('explosion_cfg')

        image = ServiceLocator.images_services.get(explosion_cfg.get('image'))
        img_surf: CSurface = CSurface.from_surface(image)

        world.add_component(cuad_entity, img_surf)
        world.add_component(cuad_entity, CTransform(kwargs.get('position')))
        world.add_component(cuad_entity, CVelocity(pygame.Vector2(0, 0)))
        world.add_component(cuad_entity, CAnimation(explosion_cfg.get('animations')))
        world.add_component(cuad_entity, CExplosionTag(kwargs.get('from_player', False)))
        ServiceLocator.sounds_services.play(explosion_cfg.get('sound'))

        return cuad_entity
