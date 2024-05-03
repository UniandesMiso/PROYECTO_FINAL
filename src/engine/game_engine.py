import json

import pygame

import esper
from src.create.cfg_loader_executor import CFGLoaderExecutor
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.ecs.systems.s_player_input import system_player_input
from src.ecs.systems.s_rendering import system_rendering
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
        self.pause_entity = -1
        self.ecs_world = esper.World()

        self.window = self.strategy_load_cfg.cfg_executor('WINDOW_CFG')

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
        ...

    def _calculate_time(self):
        self.clock.tick(self.window.get('framerate'))
        self.delta_time = self.clock.get_time() / 1000.0 if not self.on_pause else 0
        self.process_time += self.delta_time

    def _process_events(self):
        for event in pygame.event.get():
            system_player_input(self.ecs_world, event, self._do_action)
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        ...

    def _draw(self):
        system_rendering(self.ecs_world, self.window.get('screen'))
        pygame.display.flip()

    def _clean(self):
        self.ecs_world.clear_database()
        pygame.quit()

    def _do_action(self, c_input: CInputCommand):
        ...
