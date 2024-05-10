import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.tags.c_font_tag import CFontTag, FontType
from src.ecs.components.tags.c_player_tag import CPlayerTag


def system_player_score(world: esper.World, font_cfg: dict, interface_cfg: dict, points: int):
    strategy_world_entity = WorldEntitiesExecutor()
    player_components = world.get_components(CPlayerTag)
    font_components = world.get_components(CFontTag)
    c_p_t: CPlayerTag
    c_f_t: CFontTag

    for _, (c_p_t,) in player_components:
        c_p_t.current_score += points
        font_cfg['text'] = str(c_p_t.current_score)

    for entity, (c_f_t,) in font_components:
        if FontType.SCORE == c_f_t.font_type:
            world.delete_entity(entity)
            strategy_world_entity.world_entity_executor(
                entity_type='FONT_ENTITY',
                world=world,
                font_cfg=font_cfg,
                screen_zone=interface_cfg,
                tag=FontType.SCORE
            )
