import pygame

from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.ecs.components.tags.c_font_tag import FontType
from src.ecs.systems.s_animation import system_animation
from src.ecs.systems.s_blink import system_blink
from src.ecs.systems.s_bullet_screen import system_bullet_screen
from src.ecs.systems.s_enemy_dead import system_enemy_dead
from src.ecs.systems.s_enemy_fire import system_enemy_fire
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_explosion import system_explosion
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_player_dead import system_player_dead
from src.ecs.systems.s_player_spawn import system_player_spawn
from src.ecs.systems.s_ready_font import system_ready_font
from src.ecs.systems.s_screen_bounce import system_players_screen_bounce, system_enemy_screen_bounce
from src.ecs.systems.s_start_spawn import system_start_positions, system_create_starts
from src.engine.scenes_strategy.scene_strategy import SceneStrategy


class PlayScene(SceneStrategy):

    def do_create(self):
        system_create_starts(self.ecs_world, self.starts_cfg, self.window_cfg.get('screen_vector'))
        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_LEFT", key=pygame.K_LEFT
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_RIGHT", key=pygame.K_RIGHT
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_FIRE", key=pygame.K_z
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="GAME_PAUSE", key=pygame.K_p
        )

        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="GAME_OVER", key=pygame.K_z
        )

        self.strategy_world_entity.world_entity_executor(
            entity_type='FONT_ENTITY',
            world=self.ecs_world,
            font_cfg=self.font_cfg.get('ready_font'),
            screen_zone=self.interface_cfg.get('player_zone'),
            tag=FontType.READY
        )

        self.strategy_world_entity.world_entity_executor(
            entity_type='FONT_ENTITY',
            world=self.ecs_world,
            font_cfg=self.font_cfg.get('up_font'),
            screen_zone=self.interface_cfg.get('player_on'),
            tag=FontType.PLAYER
        )

        self.strategy_world_entity.world_entity_executor(
            entity_type='FONT_ENTITY',
            world=self.ecs_world,
            font_cfg=self.font_cfg.get('current_score_font'),
            screen_zone=self.interface_cfg.get('player_on'),
            tag=FontType.SCORE
        )

        self.strategy_world_entity.world_entity_executor(
            entity_type='FONT_ENTITY',
            world=self.ecs_world,
            font_cfg=self.font_cfg.get('score_font'),
            screen_zone=self.interface_cfg.get('hi_score')
        )

        self.strategy_world_entity.world_entity_executor(
            entity_type='FONT_ENTITY',
            world=self.ecs_world,
            font_cfg=self.font_cfg.get('hi_score_font'),
            screen_zone=self.interface_cfg.get('hi_score')
        )

    def do_calculate_time(self, delta_time: float):
        self.appear_player_time += delta_time
        self.appear_pause_time += delta_time

    def do_update(self, delta_time: float):
        system_start_positions(self.ecs_world, self.window_cfg.get('screen_vector'))
        system_ready_font(self.ecs_world, self.font_cfg.get('ready_font'), delta_time)
        dead, score_on_dead = system_player_dead(self.ecs_world, self.explode_cfg.get('player'))
        if not self.game_over and not self.player_spawned and self.appear_player_time > self.player_cfg.get('time_to_appear'):
            self.player_entity = system_player_spawn(self.ecs_world, self.player_cfg, self.interface_cfg,
                                                     self.last_score)
            self.player_spawned = True
        if dead:
            self.game_over = True
            self.font_cfg['current_score_font']['text'] = self.last_score = score_on_dead
        if not self.game_over and self.player_spawned:
            system_enemy_fire(self.ecs_world, self.level_cfg.get('bullets'))

        system_enemy_spawner(
            self.ecs_world,
            self.enemy_cfg,
            self.level_cfg.get('enemies'),
            self.interface_cfg.get('enemies_zone')
        )

        system_movement(self.ecs_world, delta_time, self.on_pause)
        system_players_screen_bounce(self.ecs_world, self.screen)
        system_enemy_screen_bounce(self.ecs_world, self.screen)
        system_bullet_screen(self.ecs_world, self.screen)
        system_enemy_dead(
            self.ecs_world,
            self.explode_cfg.get('enemies'),
            self.font_cfg.get('current_score_font'),
            self.interface_cfg.get('player_on')
        )
        system_explosion(self.ecs_world, self.font_cfg.get('game_over_font'), self.interface_cfg.get('game_over_zone'))
        system_blink(self.ecs_world)
        system_animation(self.ecs_world, delta_time, self.on_pause)

    def do_action(self, c_input: CInputCommand):
        if c_input.name == "GAME_OVER":
            if c_input.phase == CommandPhase.START:
                if not self.game_over: return
                self.game_over = False
                self.player_spawned = False
                self.appear_player_time = 0
                self.switch_scene('MENU')
        elif c_input.name == "GAME_PAUSE":
            if c_input.phase == CommandPhase.START:
                self.on_pause = not self.on_pause
                if self.ecs_world.entity_exists(self.pause_entity):
                    self.ecs_world.delete_entity(self.pause_entity)
                else:
                    self.pause_entity = self.strategy_world_entity.world_entity_executor(
                        entity_type='FONT_ENTITY',
                        world=self.ecs_world,
                        font_cfg=self.font_cfg.get('paused_font'),
                        screen_zone=self.window_cfg.get('screen_rect'),
                        tag=FontType.PAUSE
                    )
        elif not self.on_pause and self.ecs_world.entity_exists(self.player_entity):
            self.strategy_input.input_executor(
                world=self.ecs_world,
                c_input=c_input,
                player_cfg=self.player_cfg,
                player_entity=self.player_entity,
                level_cfg=self.level_cfg
            )

    def do_clean(self):
        pass
