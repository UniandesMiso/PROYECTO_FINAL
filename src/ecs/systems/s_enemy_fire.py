import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_enemy_tag import CEnemyTag


def system_enemy_fire(world: esper.World, player_entity:int):
    world_entity_strategy = WorldEntitiesExecutor()

    enemies_component = world.get_components(CTransform, CSurface, CEnemyTag)
    player_pos: CTransform = world.component_for_entity(player_entity, CTransform)

