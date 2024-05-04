import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

from src.engine.service_locator import ServiceLocator

LEVEL_PATH = 'assets/cfg/levels/level_01.json'


class CFGLoaderLevel(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(LEVEL_PATH, 'r') as level_loaded:
            return json.load(level_loaded)
