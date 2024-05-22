import pygame

from src.ecs.components.tags.c_font_tag import FontType
from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.engine.scenes_strategy.scene_strategy import SceneStrategy
from src.ecs.systems.s_start_spawn import system_start_positions, system_create_starts
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_blink import system_blink
from src.ecs.systems.s_menu import system_menu

class MenuScene(SceneStrategy):
    def do_create(self):
        system_create_starts(self.ecs_world, self.starts_cfg, self.window_cfg.get('screen_vector'))

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world,
            entity_type="INPUT_ENTITY",
            name="START_GAME",
            key=pygame.K_z,
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world,
            entity_type='BANNER_ENTITY',
            banner_cfg=self.menu_cfg.get('banner'),
            position=pygame.Vector2(57, 60),
            velocity=pygame.Vector2(0, -50),
        )

        self.strategy_world_entity.world_entity_executor(
            entity_type='MENU_ENTITY',
            world=self.ecs_world,
            font_cfg=self.font_cfg.get('up_font'),
            position=pygame.Vector2(15, 14),
            velocity=pygame.Vector2(0, -50),
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world,
            entity_type='MENU_ENTITY',
            font_cfg=self.font_cfg.get('current_score_font'),
            position=pygame.Vector2(47, 23),
            velocity=pygame.Vector2(0, -50),
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world,
            entity_type='MENU_ENTITY',
            font_cfg=self.font_cfg.get('score_font'),
            position=pygame.Vector2(78, 14),
            velocity=pygame.Vector2(0, -50),
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world,
            entity_type='MENU_ENTITY',
            font_cfg=self.font_cfg.get('hi_score_font'),
            position=pygame.Vector2(94, 23),
            velocity=pygame.Vector2(0, -50),
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world,
            entity_type='MENU_ENTITY',
            font_cfg=self.font_cfg.get('start_game_font'),
            position=pygame.Vector2(66, 161),
            velocity=pygame.Vector2(0, -50),
        )

    def do_calculate_time(self, delta_time: float):
        pass

    def do_update(self, delta_time: float):
        system_start_positions(self.ecs_world, self.window_cfg.get('screen_vector'))
        system_menu(self.ecs_world)
        system_movement(self.ecs_world, delta_time, self.on_pause)
        system_blink(self.ecs_world)

    def do_action(self, c_input: CInputCommand):
        if c_input.name == "START_GAME":
            if c_input.phase == CommandPhase.START:
                self.switch_scene('PLAY')

    def do_clean(self):
        pass

