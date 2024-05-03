import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy
from src.engine.service_locator import ServiceLocator

BULLET_PATH = 'assets/cfg/bullet.json'


class CFGLoaderBullet(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(BULLET_PATH, "r") as bullet_file:
            bullet_json = json.load(bullet_file)
            return {}
