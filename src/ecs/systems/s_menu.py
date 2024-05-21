import esper

from src.ecs.components.tags.c_menu_tag import CMenuTag
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def system_menu(world: esper.World):
    components = world.get_components(CTransform, CVelocity, CMenuTag)
    c_m: CMenuTag
    for _, (c_t,c_v,c_m) in components:
        if c_t.pos.y < c_m.final_position:
            c_v.vel.y=0
