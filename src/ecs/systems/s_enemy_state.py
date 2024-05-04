import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_enemy_state import CEnemyState, EnemyState
from src.ecs.components.c_velocity import CVelocity


def _do_idle_state(c_v: CVelocity, c_a: CAnimation, c_e: CEnemyState):
    _set_animation(c_a, 1)
    if c_v.vel.magnitude_squared() > 0:
        c_e.state = EnemyState.MOVE


def _do_move_state(c_v: CVelocity, c_a: CAnimation, c_e: CEnemyState):
    _set_animation(c_a, 0)
    if c_v.vel.magnitude_squared() <= 0:
        c_e.state = EnemyState.IDLE


def _set_animation(c_a: CAnimation, state: int):
    if c_a.current_animation == state:
        return

    c_a.current_animation = state
    c_a.current_animation_time = 0
    c_a.current_frame = c_a.animations_list[c_a.current_animation].start


def system_enemy_state(world: esper.World):
    components = world.get_components(CVelocity, CAnimation, CEnemyState)
    c_v: CVelocity
    c_a: CAnimation
    c_e: CEnemyState

    for _, (c_v, c_a, c_e) in components:
        if c_e.state == EnemyState.IDLE:
            _do_idle_state(c_v, c_a, c_e)
        if c_e.state == EnemyState.MOVE:
            _do_move_state(c_v, c_a, c_e)
