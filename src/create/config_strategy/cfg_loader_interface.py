import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

INTERFACE_PATH = 'assets/cfg/interface.json'


class CFGLoaderInterface(CFGLoaderStrategy):

    def load_cfg(self, **kwargs):
        with open(INTERFACE_PATH, "r") as fonts_loaded:
            json_interface = json.load(fonts_loaded)
            header_zone = json_interface.get('header_zone')
            enemies_zone = json_interface.get('enemies_zone')
            player_zone = json_interface.get('player_zone')

            return dict(
                header_zone=pygame.Rect(
                    header_zone.get('left'),
                    header_zone.get('top'),
                    header_zone.get('width'),
                    header_zone.get('height')
                ),
                enemies_zone=pygame.Rect(
                    enemies_zone.get('left'),
                    enemies_zone.get('top'),
                    enemies_zone.get('width'),
                    enemies_zone.get('height')
                ),
                player_zone=pygame.Rect(
                    player_zone.get('left'),
                    player_zone.get('top'),
                    player_zone.get('width'),
                    player_zone.get('height')
                ),

            )
