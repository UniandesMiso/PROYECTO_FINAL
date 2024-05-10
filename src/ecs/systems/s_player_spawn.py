import pygame

import esper
from src.create.world_entities_executor import WorldEntitiesExecutor


def system_player_spawn(world: esper.World, player_cfg: dict, interface_cfg: dict):
    player_zone: dict = interface_cfg.get('player_zone')
    strategy_world_entity = WorldEntitiesExecutor()

    strategy_world_entity.world_entity_executor(
        world=world, entity_type="INPUT_ENTITY",
        name="PLAYER_LEFT_LETTER", key=pygame.K_a
    )
    strategy_world_entity.world_entity_executor(
        world=world, entity_type="INPUT_ENTITY",
        name="PLAYER_LEFT", key=pygame.K_LEFT
    )
    strategy_world_entity.world_entity_executor(
        world=world, entity_type="INPUT_ENTITY",
        name="PLAYER_RIGHT_LETTER", key=pygame.K_d
    )
    strategy_world_entity.world_entity_executor(
        world=world, entity_type="INPUT_ENTITY",
        name="PLAYER_RIGHT", key=pygame.K_RIGHT
    )
    strategy_world_entity.world_entity_executor(
        world=world, entity_type="INPUT_ENTITY",
        name="PLAYER_FIRE", key=pygame.K_z
    )
    return strategy_world_entity.world_entity_executor(
        entity_type='PLAYER_ENTITY',
        world=world,
        entity_cfg=player_cfg,
        zone_cfg=player_zone
    )
