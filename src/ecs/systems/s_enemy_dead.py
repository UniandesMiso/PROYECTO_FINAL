import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_bullet_tag import CBulletTag, TypeBullet
from src.ecs.components.tags.c_enemy_tag import CEnemyTag
from src.ecs.systems.s_player_score import system_player_score


def system_enemy_dead(world: esper.World, explosion: dict, font_cfg: dict, interface_cfg: dict):
    world_entity_strategy = WorldEntitiesExecutor()

    bullet_component = world.get_components(CTransform, CSurface, CBulletTag)
    enemies_component = world.get_components(CTransform, CSurface, CEnemyTag)

    c_b_t: CTransform
    c_b_s: CSurface
    c_e_t: CTransform
    c_e_s: CSurface
    c_e_tg: CEnemyTag
    c_b_tg: CBulletTag

    for enemy_entity, (c_e_t, c_e_s, c_e_tg) in enemies_component:
        enemy_rect = CSurface.get_area_relative(c_e_s.area, c_e_t.pos)
        for entity_b, (c_b_t, c_b_s, c_b_tg) in bullet_component:
            if TypeBullet.PLAYER == c_b_tg.bullet_type:
                bullet_rect = CSurface.get_area_relative(c_b_s.area, c_b_t.pos)
                if enemy_rect.colliderect(bullet_rect):
                    world.delete_entity(enemy_entity)
                    world.delete_entity(entity_b)
                    world_entity_strategy.world_entity_executor(
                        world=world,
                        entity_type="EXPLOSION_ENTITY",
                        position=c_e_t.pos,
                        explosion_cfg=explosion
                    )
                    system_player_score(world, font_cfg, interface_cfg, c_e_tg.dead_points)
