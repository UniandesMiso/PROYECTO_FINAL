import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface


def system_animation(world: esper.World, delta_time: float, on_pause:bool):
    if not on_pause:
        components = world.get_components(CSurface, CAnimation)
        c_s: CSurface
        c_a: CAnimation
        for _, (c_s, c_a) in components:
            c_a.current_animation_time -= delta_time
            if c_a.current_animation_time <= 0:
                c_a.current_animation_time = c_a.animations_list[c_a.current_animation].framerate
                c_a.current_frame += 1
                if c_a.current_frame > c_a.animations_list[c_a.current_animation].end:
                    c_a.current_frame = c_a.animations_list[c_a.current_animation].start
                rect_surface = c_s.surf.get_rect()
                c_s.area.width = rect_surface.width / c_a.number_frames
                c_s.area.x = c_s.area.width * c_a.current_frame
