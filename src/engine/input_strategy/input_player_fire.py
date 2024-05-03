import pygame

import esper
from src.create.cfg_loader_executor import CFGLoaderExecutor
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_bullet_tag import CBulletTag
from src.engine.input_strategy.input_strategy import InputStrategy


def basic_fire(c_input, world, player_entity, level_path):
    if c_input.name == "PLAYER_FIRE":
        strategy_world_entity = WorldEntitiesExecutor()
        strategy_load_cfg = CFGLoaderExecutor()
        player_pos = world.component_for_entity(player_entity, CTransform)
        player_size = world.component_for_entity(player_entity, CSurface)
        player_rect = player_size.area.size
        bullet = strategy_load_cfg.cfg_executor(
            cfg_type='BULLET_CFG',
            level_path=level_path,
            mouse_pos=pygame.mouse.get_pos(),
            player_pos=player_pos.pos,
            player_size=player_rect,
            bullet_type='STANDARD_BULLET')

        if len(world.get_component(CBulletTag)) < bullet.get("max_bullets"):
            strategy_world_entity.world_entity_executor(
                world=world,
                entity_type="BULLET_ENTITY",
                image=bullet.get('image'),
                position=bullet.get('position'),
                velocity=bullet.get('velocity'),
                sound=bullet.get('sound')
            )


class InputPlayerFire(InputStrategy):

    def execute_action(self, world: esper.World, c_input: CInputCommand, **kwargs):
        basic_fire(c_input, world, kwargs.get('player_entity'), kwargs.get('level_path'))
