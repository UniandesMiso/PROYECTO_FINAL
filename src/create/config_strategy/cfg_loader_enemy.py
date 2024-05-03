import json
import random

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy
from src.engine.service_locator import ServiceLocator

ENEMIES_PATH = 'assets/cfg/enemies.json'


class CFGLoaderEnemy(CFGLoaderStrategy):

    def load_cfg(self, **kwargs):
        with open(ENEMIES_PATH, 'r') as enemies_loaded:
            json_enemy = json.load(enemies_loaded)
        return {}
