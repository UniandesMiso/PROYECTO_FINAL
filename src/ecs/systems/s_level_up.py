import pygame
import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.tags.c_enemy_tag import CEnemyTag


def system_level_up(world: esper.World, font_cfg: dict, level: int) -> bool:
    components = world.get_components(CEnemyTag)
    strategy_world_entity = WorldEntitiesExecutor()

    if not components:
        strategy_world_entity.world_entity_executor(
            world = world, entity_type='LEVEL_ENTITY',
            current_level = level + 1,
            screen_zone = pygame.Rect(330, 5, 20, 25),
            font_cfg = font_cfg,
        )
        return True
    return False