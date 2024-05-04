import esper
from src.create.world_entities_executor import WorldEntitiesExecutor


def system_enemy_spawner(world: esper.World, enemies: dict, screen: dict):
    strategy_world_entity = WorldEntitiesExecutor()
    for _type, _enemy in enemies.items():
        strategy_world_entity.world_entity_executor(
            entity_type='ENEMY_ENTITY',
            world=world,
            enemy_type=_type,
            enemy_cfg=_enemy,
            screen=screen
        )
