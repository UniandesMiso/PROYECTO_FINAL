import esper
from src.create.world_entities_executor import WorldEntitiesExecutor


def system_player_spawn(world: esper.World, player_cfg: dict, interface_cfg: dict, last_score=0):
    player_zone: dict = interface_cfg.get('player_zone')
    strategy_world_entity = WorldEntitiesExecutor()

    return strategy_world_entity.world_entity_executor(
        entity_type='PLAYER_ENTITY',
        world=world,
        entity_cfg=player_cfg,
        zone_cfg=player_zone,
        last_score=last_score
    )
