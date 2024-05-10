import pygame

import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.tags.c_bullet_tag import CBulletTag, TypeBullet
from src.engine.service_locator import ServiceLocator


def system_bullet_spawn(world: esper.World,
                        bullet_cfg: dict,
                        direction: int,
                        pos_x: int,
                        pos_y: int,
                        tag: CBulletTag,
                        sound: str = None):
    strategy_world_entity = WorldEntitiesExecutor()
    size_cfg: dict = bullet_cfg.get('size')
    color_cfg: dict = bullet_cfg.get('color')
    velocity: int = int(bullet_cfg.get('velocity')) * direction
    size: pygame.Vector2 = pygame.Vector2(size_cfg.get('w'), size_cfg.get('h'))
    color: pygame.Color = pygame.Color(color_cfg.get('r'), color_cfg.get('g'), color_cfg.get('b'))
    position: pygame.Vector2 = pygame.Vector2(pos_x, pos_y)
    strategy_world_entity.world_entity_executor(
        entity_type='BULLET_ENTITY',
        world=world,
        color=color,
        size=size,
        position=position,
        velocity=velocity,
        tag=tag
    )
    if sound:
        ServiceLocator.sounds_services.play(sound)
