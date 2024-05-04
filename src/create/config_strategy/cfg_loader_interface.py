import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy
from src.engine.service_locator import ServiceLocator

INTERFACE_PATH = 'assets/cfg/interface.json'


class CFGLoaderInterface(CFGLoaderStrategy):

    def load_cfg(self, **kwargs):
        with open(INTERFACE_PATH, "r") as fonts_loaded:
            return json.load(fonts_loaded)
