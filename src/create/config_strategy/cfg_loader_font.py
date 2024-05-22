import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy
from src.engine.service_locator import ServiceLocator

FONT_PATH = 'assets/cfg/fonts.json'


class CFGLoaderFont(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(FONT_PATH, "r") as bullet_file:
            return json.load(bullet_file)

