
import esper
from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_bullet_tag import CBulletTag, TypeBullet
from src.ecs.systems.s_bullet_spawn import system_bullet_spawn
from src.engine.input_strategy.input_strategy import InputStrategy


def has_to_fire(world: esper.World, phase: CommandPhase, max_on_screen: int) -> bool:
    components = world.get_components(CBulletTag)
    c_b: CBulletTag
    bullets = 0
    for _, (c_b,) in components:
        if TypeBullet.PLAYER == c_b.bullet_type:
            bullets += 1

    return phase == CommandPhase.START and bullets < max_on_screen


def basic_fire(c_input, world, bullet_cfg: dict, pos_x: int, pos_y: int, sound: str):
    pos_x -= bullet_cfg.get('size').get('w') / 2
    if c_input.name == "PLAYER_FIRE":
        if has_to_fire(world, c_input.phase, bullet_cfg.get("max_at_time")):
            system_bullet_spawn(world, bullet_cfg, -1, pos_x, pos_y, CBulletTag(TypeBullet.PLAYER), sound)


class InputPlayerFire(InputStrategy):

    def execute_action(self, world: esper.World, c_input: CInputCommand, **kwargs):
        level_cfg: dict = kwargs.get('level_cfg')
        player_cfg: dict = kwargs.get('player_cfg')
        player_pos: CTransform = world.component_for_entity(kwargs.get('player_entity'), CTransform)
        player_surface: CSurface = world.component_for_entity(kwargs.get('player_entity'), CSurface)

        bullets: dict = level_cfg.get('bullets')
        pos_x = player_pos.pos.x + (player_surface.area.width / 2)
        pos_y = player_pos.pos.y

        basic_fire(c_input, world, bullets.get('from_player'), pos_x, pos_y, player_cfg.get('shoot_sound'))
