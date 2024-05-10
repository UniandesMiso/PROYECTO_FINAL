import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_bullet_tag import CBulletTag, TypeBullet
from src.ecs.components.tags.c_player_tag import CPlayerTag


def system_player_dead(world: esper.World, explosion: dict):
    world_entity_strategy = WorldEntitiesExecutor()

    bullet_component = world.get_components(CTransform, CSurface, CBulletTag)
    player_component = world.get_components(CTransform, CSurface, CPlayerTag)

    c_b_t: CTransform
    c_b_s: CSurface
    c_p_t: CTransform
    c_p_s: CSurface
    c_p_tg: CPlayerTag
    c_b_tg: CBulletTag

    for player_entity, (c_p_t, c_p_s, c_p_tg) in player_component:
        player_rect = CSurface.get_area_relative(c_p_s.area, c_p_t.pos)
        for entity_b, (c_b_t, c_b_s, c_b_tg) in bullet_component:
            if TypeBullet.ENEMY == c_b_tg.bullet_type:
                bullet_rect = CSurface.get_area_relative(c_b_s.area, c_b_t.pos)
                if player_rect.colliderect(bullet_rect):
                    world.delete_entity(player_entity)
                    world.delete_entity(entity_b)
                    world_entity_strategy.world_entity_executor(
                        world=world,
                        entity_type="EXPLOSION_ENTITY",
                        position=c_p_t.pos,
                        explosion_cfg=explosion
                    )
