import esper
from src.ecs.components.tags.c_font_tag import CFontTag, FontType


def system_ready_font(world: esper.World, font_cfg: dict, delta_time: float):
    components = world.get_components(CFontTag)
    max_view_time: int = font_cfg.get("max_view_time", 0)
    c_f_t: CFontTag
    game_ready = False
    for entity, (c_f_t,) in components:
        if FontType.READY == c_f_t.font_type:
            if c_f_t.time > max_view_time:
                world.delete_entity(entity)
                game_ready = True
                break
            else:
                c_f_t.time += delta_time
    return game_ready
