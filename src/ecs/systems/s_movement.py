import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_start_tag import CStartTag


def system_movement(world: esper.World, delta_time: float, on_pause: bool):
    components = world.get_components(CTransform, CVelocity)
    c_t: CTransform
    c_v: CVelocity
    for entity, (c_t, c_v) in components:
        if on_pause and not world.has_component(entity, CStartTag):
            delta_time = 0
        c_t.pos.x += c_v.vel.x * delta_time
        c_t.pos.y += c_v.vel.y * delta_time
