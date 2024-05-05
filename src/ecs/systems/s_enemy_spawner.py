import math

import pygame

import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_surface import CSurface
from src.engine.service_locator import ServiceLocator


def system_enemy_spawner(
        world: esper.World,
        enemies_cfg: dict,
        level_cfg: dict,
        zone_rect: pygame.Rect):
    strategy_world_entity = WorldEntitiesExecutor()

    columns = level_cfg.get('columns')
    enemy_zone_width = (zone_rect.width / columns) + level_cfg.get('padding')

    pos_y = zone_rect.y

    for _type, _enemy in enemies_cfg.items():
        if not _enemy.get('spawned'):
            level_dist = level_cfg.get('dist')
            level_enemy_cfg = next(
                filter(lambda cfg: cfg.get('type').__eq__(_type), level_dist)
            )
            enemy_rows = level_enemy_cfg.get('rows')

            image = ServiceLocator.images_services.get(_enemy.get('image'))
            img_surf: CSurface = CSurface.from_surface(image)
            img_height = img_surf.area.height

            for i in range(0, enemy_rows):
                pos_x = zone_rect.x
                for j in range(0, columns):
                    if [i, j] not in (level_enemy_cfg.get('empty_spaces')):
                        position = pygame.Vector2(pos_x, pos_y)
                        strategy_world_entity.world_entity_executor(
                            entity_type='ENEMY_ENTITY',
                            world=world,
                            position=position,
                            entity_cfg=_enemy,
                            img_surf=img_surf
                        )

                    pos_x += enemy_zone_width
                pos_y += img_height
            _enemy.update(spawned=True)
