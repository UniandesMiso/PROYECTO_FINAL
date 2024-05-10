import pygame

import esper
from src.create.cfg_loader_executor import CFGLoaderExecutor
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.tags.c_font_tag import FontType
from src.ecs.systems.s_animation import system_animation
from src.ecs.systems.s_bullet_screen import system_bullet_screen
from src.ecs.systems.s_enemy_dead import system_enemy_dead
from src.ecs.systems.s_enemy_fire import system_enemy_fire
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_explosion import system_explosion
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_player_dead import system_player_dead
from src.ecs.systems.s_player_input import system_player_input
from src.ecs.systems.s_player_spawn import system_player_spawn
from src.ecs.systems.s_ready_font import system_ready_font
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_players_screen_bounce, system_enemy_screen_bounce
from src.engine.input_executor import InputExecutor


class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        self.strategy_load_cfg = CFGLoaderExecutor()
        self.strategy_world_entity = WorldEntitiesExecutor()
        self.strategy_input = InputExecutor()
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.on_pause = True
        self.delta_time = 0
        self.ecs_world = esper.World()

        self.window_cfg = self.strategy_load_cfg.cfg_executor('WINDOW_CFG')
        self.interface_cfg = self.strategy_load_cfg.cfg_executor('INTERFACE_CFG')
        self.level_cfg = self.strategy_load_cfg.cfg_executor('LEVEL_CFG')
        self.player_cfg = self.strategy_load_cfg.cfg_executor('PLAYER_CFG')
        self.enemy_cfg = self.strategy_load_cfg.cfg_executor('ENEMY_CFG')
        self.explode_cfg = self.strategy_load_cfg.cfg_executor('EXPLOSION_CFG')
        self.font_cfg = self.strategy_load_cfg.cfg_executor('FONT_CFG')

        self.pause_entity = -1
        self.player_entity = -1
        self.screen = self.window_cfg.get('screen')

    def run(self) -> None:
        self._create()
        self.is_running = True
        self.on_pause = False
        while self.is_running:
            self._process_events()
            self._calculate_time()
            self._update()
            self._draw()
        self._clean()

    def _create(self):

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

    def _calculate_time(self):
        self.clock.tick(self.window_cfg.get('framerate'))
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            system_player_input(self.ecs_world, event, self._do_action)
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        if system_ready_font(self.ecs_world, self.font_cfg.get('ready_font'), self.delta_time):
            self.player_entity = system_player_spawn(self.ecs_world, self.player_cfg, self.interface_cfg)

        system_enemy_spawner(
            self.ecs_world,
            self.enemy_cfg,
            self.level_cfg.get('enemies'),
            self.interface_cfg.get('enemies_zone')
        )

        system_movement(self.ecs_world, self.delta_time)
        system_players_screen_bounce(self.ecs_world, self.screen)
        system_enemy_screen_bounce(self.ecs_world, self.screen)
        system_bullet_screen(self.ecs_world, self.screen)
        system_enemy_dead(
            self.ecs_world,
            self.explode_cfg.get('enemies'),
            self.font_cfg.get('current_score_font'),
            self.interface_cfg.get('player_on')
        )
        system_player_dead(self.ecs_world, self.explode_cfg.get('player'))
        system_enemy_fire(self.ecs_world, self.level_cfg.get('bullets'))
        system_explosion(self.ecs_world)
        system_animation(self.ecs_world, self.delta_time)
        self.ecs_world._clear_dead_entities()

    def _draw(self):
        self.screen.fill(self.window_cfg.get('bg'))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        self.ecs_world.clear_database()
        pygame.quit()

    def _do_action(self, c_input: CInputCommand):
        if self.ecs_world.entity_exists(self.player_entity):
            self.strategy_input.input_executor(
                world=self.ecs_world,
                c_input=c_input,
                player_cfg=self.player_cfg,
                player_entity=self.player_entity,
                level_cfg=self.level_cfg
            )

