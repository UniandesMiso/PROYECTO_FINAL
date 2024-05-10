import random

import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_bullet_tag import CBulletTag, TypeBullet
from src.ecs.components.tags.c_enemy_tag import CEnemyTag
from src.ecs.systems.s_bullet_spawn import system_bullet_spawn


def has_to_fire(world: esper.World, max_on_screen: int) -> bool:
    components = world.get_components(CBulletTag)
    c_b: CBulletTag
    bullets = 0
    for _, (c_b,) in components:
        if TypeBullet.ENEMY == c_b.bullet_type:
            bullets += 1

    return bullets < max_on_screen


def system_enemy_fire(world: esper.World, bullets_cfg: dict):
    enemies_component = world.get_components(CTransform, CSurface, CEnemyTag)
    enemy_bullet_cfg: dict = bullets_cfg.get('from_enemies')

    c_p: CTransform
    c_s: CSurface
    c_e: CEnemyTag

    shooters = []
    for i in range(0, enemy_bullet_cfg.get('max_at_time')):
        shooters.append(random.randint(0, len(enemies_component)))

    index = 0
    for _, (c_p, c_s, c_e) in enemies_component:
        if has_to_fire(world, enemy_bullet_cfg.get('max_at_time')) and index in shooters:
            pos_x = c_p.pos.x + (c_s.area.width / 2) - enemy_bullet_cfg.get('size').get('w') / 2
            pos_y = c_p.pos.y + c_s.area.height
            system_bullet_spawn(world, enemy_bullet_cfg, 1, pos_x, pos_y, CBulletTag(TypeBullet.ENEMY))

        index += 1
