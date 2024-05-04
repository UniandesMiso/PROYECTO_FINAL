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
from src.utils.window_localizer_util import window_position


class WorldEntityPlayer(WorldEntityStrategy):


    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        player_cfg: dict = kwargs.get("entity_cfg")
        screen_cfg: dict = kwargs.get("screen_cfg")
        zone_cfg: dict = kwargs.get("zone_cfg")

        left = zone_cfg.get('start_point').get('x')
        top = zone_cfg.get('start_point').get('y')
        width = zone_cfg.get('size').get('w')
        height = zone_cfg.get('size').get('h')
        zone_rect = pygame.Rect(left, top, width, height)

        image = ServiceLocator.images_services.get(player_cfg.get('image'))
        img_surf: CSurface = CSurface.from_surface(image)

        position = window_position(
            rect=zone_rect,
            fixed=player_cfg.get('position'),
            surf=img_surf,
            padding=player_cfg.get('padding')
        )

        world.add_component(cuad_entity, img_surf)
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CVelocity(pygame.Vector2(0, 0)))
        world.add_component(cuad_entity, CPlayerTag())

        return cuad_entity
