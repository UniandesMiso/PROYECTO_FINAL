import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_enemy_tag import CEnemyTag
from src.engine.service_locator import ServiceLocator
from src.utils.window_localizer_util import window_position


class WorldEntityEnemy(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        enemy_cfg: dict = kwargs.get("enemy_cfg")
        screen_cfg: dict = kwargs.get("screen")
        image = ServiceLocator.images_services.get(enemy_cfg.get('image'))
        img_surf: CSurface = CSurface.from_surface(image)
        position = window_position(screen_cfg.get('screen_vector'), enemy_cfg.get('start_position'), img_surf)
        world.add_component(cuad_entity, img_surf)
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CAnimation(enemy_cfg.get('animations')))
        world.add_component(cuad_entity, CVelocity(pygame.Vector2(0, 0)))
        world.add_component(cuad_entity, CEnemyTag())
        return cuad_entity
