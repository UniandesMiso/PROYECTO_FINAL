import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.engine.service_locator import ServiceLocator
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_flag_tag import CLevelTag
from src.utils.window_localizer_util import window_position


class WorldEntityLevel(WorldEntityStrategy):

    def create_entity(self, world: esper.World, flag_entity: int, **kwargs) -> int:
        image_source:str = 'assets\img\invaders_level_flag.png'
        image = ServiceLocator.images_services.get(image_source)
        img_surf: CSurface = CSurface.from_surface(image)
        level_zone:pygame.Rect = kwargs.get('screen_zone')
        level_cfg:dict = kwargs.get('font_cfg')
        current_level = kwargs.get('current_level')

        position = window_position(
            rect=level_zone,
            fixed=level_cfg.get('fixed'),
            surf=img_surf,
            padding=level_cfg.get('padding', 0)
        )

        world.add_component(flag_entity, img_surf)
        world.add_component(flag_entity, CTransform(position))
        world.add_component(flag_entity, CLevelTag(current_level))
        return flag_entity
