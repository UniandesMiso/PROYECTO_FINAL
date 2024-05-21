import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

INTERFACE_PATH = 'assets/cfg/interface.json'


class CFGLoaderInterface(CFGLoaderStrategy):

    def load_cfg(self, **kwargs):
        with open(INTERFACE_PATH, "r") as fonts_loaded:
            json_interface: dict = json.load(fonts_loaded)
            player_on = json_interface.get('player_on')
            hi_score = json_interface.get('hi_score')
            enemies_zone = json_interface.get('enemies_zone')
            player_zone = json_interface.get('player_zone')
            game_over_zone = json_interface.get('game_over_zone')

            return dict(
                player_on=pygame.Rect(
                    player_on.get('left'),
                    player_on.get('top'),
                    player_on.get('width'),
                    player_on.get('height')
                ),
                hi_score=pygame.Rect(
                    hi_score.get('left'),
                    hi_score.get('top'),
                    hi_score.get('width'),
                    hi_score.get('height')
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
                game_over_zone=pygame.Rect(
                    game_over_zone.get('left'),
                    game_over_zone.get('top'),
                    game_over_zone.get('width'),
                    game_over_zone.get('height')
                ),
            )
