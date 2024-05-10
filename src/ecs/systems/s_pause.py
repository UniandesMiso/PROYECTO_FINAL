import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.tags.c_font_tag import FontType, CFontTag


def system_pause(world: esper.World, font_cfg: dict, zone: dict, pause: bool):
    strategy_world_entity = WorldEntitiesExecutor()
    components = world.get_components(CFontTag)
    c_f: CFontTag

    pause_entity = -1

    for entity, (c_f,) in components:
        if FontType.PAUSE == c_f.font_type:
            pause_entity = entity
            break

    if world.entity_exists(pause_entity):
        world.delete_entity(pause_entity)
        return

    if pause:
        strategy_world_entity.world_entity_executor(
            entity_type='FONT_ENTITY',
            world=world,
            font_cfg=font_cfg,
            screen_zone=zone,
            tag=FontType.PAUSE
        )
