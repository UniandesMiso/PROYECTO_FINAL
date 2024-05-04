import esper
from src.create.world_entities_executor import WorldEntitiesExecutor


def system_enemy_spawner(world: esper.World, enemies: list, screen: dict):
    strategy_world_entity = WorldEntitiesExecutor()
    for enemy in enemies:
        strategy_world_entity.world_entity_executor(
            entity_type='ENEMY_ENTITY',
            world=world,
            enemy_type=enemy.get('type', 1),
            position=enemy.get('start_position'),
            image=enemy.get('image'),
            screen=screen
        )
