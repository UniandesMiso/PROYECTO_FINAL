import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.tags.c_explosion_tag import CExplosionTag
from src.ecs.components.tags.c_font_tag import FontType


def system_explosion(world: esper.World, font_cfg: dict, interface_cfg: dict):
    world_entity_strategy = WorldEntitiesExecutor()
    components = world.get_components(CAnimation, CExplosionTag)
    c_a: CAnimation
    c_t: CExplosionTag
    for entity_explosion, (c_a, c_t) in components:
        if c_a.current_frame == c_a.animations_list[c_a.current_animation].end:
            world.delete_entity(entity_explosion)
            if c_t.from_player == True:
                world_entity_strategy.world_entity_executor(
                    entity_type='FONT_ENTITY',
                    world=world,
                    font_cfg=font_cfg,
                    screen_zone=interface_cfg,
                    tag=FontType.GAME_OVER,
                )
