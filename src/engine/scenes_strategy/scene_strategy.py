from abc import ABC, abstractmethod

import pygame

import esper
from src.create.cfg_loader_executor import CFGLoaderExecutor
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.systems.s_player_input import system_player_input
from src.ecs.systems.s_rendering import system_rendering
from src.engine.input_executor import InputExecutor
import src.engine.game_engine

class SceneStrategy(ABC):

    def __init__(self, game_engine: 'src.engine.game_engine', window_cfg: dict):
        self.window_cfg = window_cfg
        self.ecs_world = esper.World()
        self._game_engine: 'src.engine.game_engine' = game_engine
        self.strategy_load_cfg = CFGLoaderExecutor()
        self.strategy_world_entity = WorldEntitiesExecutor()
        self.strategy_input = InputExecutor()
        self.interface_cfg = self.strategy_load_cfg.cfg_executor('INTERFACE_CFG')
        self.level_cfg = self.strategy_load_cfg.cfg_executor('LEVEL_CFG')
        self.player_cfg = self.strategy_load_cfg.cfg_executor('PLAYER_CFG')
        self.enemy_cfg = self.strategy_load_cfg.cfg_executor('ENEMY_CFG')
        self.explode_cfg = self.strategy_load_cfg.cfg_executor('EXPLOSION_CFG')
        self.font_cfg = self.strategy_load_cfg.cfg_executor('FONT_CFG')
        self.starts_cfg = self.strategy_load_cfg.cfg_executor('STARTS_CFG')
        self.pause_entity = -1
        self.player_entity = -1
        self.player_spawned = False
        self.on_pause = False
        self.appear_player_time = 0
        self.appear_pause_time = 1
        self.last_score = 0

        self.screen = self.window_cfg.get('screen')

    def do_process_events(self, event: pygame.event):
        system_player_input(self.ecs_world, event, self.do_action)

    def simulate(self, delta_time):
        self.do_update(delta_time)
        self.ecs_world._clear_dead_entities()

    def clean(self):
        self.ecs_world.clear_database()
        self.do_clean()

    def switch_scene(self, new_scene_name: str):
        self._game_engine.switch_scene(new_scene_name)

    @abstractmethod
    def do_create(self):
        ...

    @abstractmethod
    def do_calculate_time(self, delta_time: float):
        ...

    @abstractmethod
    def do_update(self, delta_time: float):
        ...

    def do_draw(self, screen):
        system_rendering(self.ecs_world, screen)

    @abstractmethod
    def do_action(self, action: CInputCommand):
        ...

    @abstractmethod
    def do_clean(self):
        ...
