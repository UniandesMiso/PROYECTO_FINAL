import pygame

import esper
from src.create.cfg_loader_executor import CFGLoaderExecutor
from src.ecs.components.c_input_command import CInputCommand
from src.ecs.systems.s_start_spawn import system_create_starts
from src.engine.scene_executor import SceneExecutor
from src.engine.scenes_strategy.scene_strategy import SceneStrategy


class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        self.ecs_world = esper.World()
        self.strategy_load_cfg = CFGLoaderExecutor()
        self.is_running = False
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.window_cfg = self.strategy_load_cfg.cfg_executor('WINDOW_CFG')
        self.screen = self.window_cfg.get('screen')
        self._current_scene: SceneStrategy = None
        self._scene_name_to_switch: str = None
        self.scene_executor = SceneExecutor(self, self.window_cfg)

    def run(self, scene_name: str) -> None:
        self.is_running = True
        self._current_scene = self.scene_executor.scene_executor(scene_name)
        self._create()
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
            self._handle_switch_scene()
        self._do_clean()

    def switch_scene(self, new_scene_name: str):
        self._scene_name_to_switch = new_scene_name

    def _create(self):
        self._current_scene.do_create()

    def _calculate_time(self):
        self.clock.tick(self.window_cfg.get('framerate'))
        self.delta_time = self.clock.get_time() / 1000.0
        self._current_scene.do_calculate_time(self.delta_time)

    def _process_events(self):
        for event in pygame.event.get():
            self._current_scene.do_process_events(event)
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        self._current_scene.simulate(self.delta_time)

    def _draw(self):
        self.screen.fill(self.window_cfg.get('bg'))
        self._current_scene.do_draw(self.screen)
        pygame.display.flip()

    def _handle_switch_scene(self):
        if self._scene_name_to_switch is not None:
            self._current_scene.clean()
            self._current_scene = self.scene_executor.scene_executor(self._scene_name_to_switch)
            self._current_scene.do_create()
            self._scene_name_to_switch = None

    def _do_clean(self):
        if self._current_scene is not None:
            self._current_scene.clean()
        self.ecs_world.clear_database()
        pygame.quit()

    def _do_action(self, c_input: CInputCommand):
        self._current_scene.do_action(c_input)
