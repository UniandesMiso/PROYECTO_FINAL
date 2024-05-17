import time

import esper
from src.ecs.components.c_blink import CBlink


def system_blink(world: esper.World):
    components = world.get_components(CBlink)
    c_b: CBlink
    current_time = time.time()
    for _, (c_b,) in components:
        if current_time - c_b.last >= c_b.rate:
            c_b.last = current_time
            c_b.visible = not c_b.visible
