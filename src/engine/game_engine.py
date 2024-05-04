import json

import pygame

import esper
from src.create.cfg_loader_executor import CFGLoaderExecutor
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_player_input import system_player_input
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_players_screen_bounce
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
        self.process_time = 0
        self.ecs_world = esper.World()

        self.window_cfg = self.strategy_load_cfg.cfg_executor('WINDOW_CFG')
        self.player_cfg = self.strategy_load_cfg.cfg_executor('PLAYER_CFG')
        self.enemy_cfg = self.strategy_load_cfg.cfg_executor('ENEMY_CFG')

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
        self.player_entity = self.strategy_world_entity.world_entity_executor(
            entity_type='PLAYER_ENTITY',
            world=self.ecs_world,
            player_cfg=self.player_cfg,
            screen=self.window_cfg
        )
        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_LEFT_LETTER", key=pygame.K_a
        )
        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_LEFT", key=pygame.K_LEFT
        )
        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_RIGHT_LETTER", key=pygame.K_d
        )
        self.strategy_world_entity.world_entity_executor(
            world=self.ecs_world, entity_type="INPUT_ENTITY",
            name="PLAYER_RIGHT", key=pygame.K_RIGHT
        )

    def _calculate_time(self):
        self.clock.tick(self.window_cfg.get('framerate'))
        self.delta_time = self.clock.get_time() / 1000.0
        self.process_time += self.delta_time

    def _process_events(self):
        for event in pygame.event.get():
            system_player_input(self.ecs_world, event, self._do_action)
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        #system_enemy_spawner(self.ecs_world, self.enemy_cfg, self.window_cfg)
        system_players_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        self.screen.fill(self.window_cfg.get('bg'))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        self.ecs_world.clear_database()
        pygame.quit()

    def _do_action(self, c_input: CInputCommand):
        self.strategy_input.input_executor(
            world=self.ecs_world,
            c_input=c_input,
            player_cfg=self.player_cfg,
            player_entity=self.player_entity
        )
