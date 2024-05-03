import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

from src.engine.service_locator import ServiceLocator

PLAYER_PATH = 'assets/cfg/player.json'


class CFGLoaderPlayer(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(PLAYER_PATH, 'r') as players_loaded:
            json_player = json.load(players_loaded)

        return {}
