import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_menu_tag import CMenuTag
from src.engine.service_locator import ServiceLocator


class WorldEntityBanner(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        banner_cfg: dict = kwargs.get('banner_cfg')
        position: pygame.Vector2 = kwargs.get("position")
        final_position: int = position.y
        position.y+=248

        image = ServiceLocator.images_services.get(banner_cfg.get('image'))
        img_surf: CSurface = CSurface.from_surface(image)

        world.add_component(cuad_entity, img_surf)
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CVelocity(kwargs.get('velocity')))
        world.add_component(cuad_entity, CMenuTag(final_position))

        return cuad_entity
