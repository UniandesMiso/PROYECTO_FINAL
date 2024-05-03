import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

from src.engine.service_locator import ServiceLocator

PLAYER_PATH = 'assets/cfg/player.json'


class CFGLoaderPlayer(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(PLAYER_PATH, 'r') as players_loaded:
            json_player = json.load(players_loaded)
            image = ServiceLocator.images_services.get(json_player.get('image'))
            start_pos = json_player.get('start_position')
            input_velocity = json_player.get('input_velocity')
            velocity = pygame.Vector2(0, 0)
            padding = json_player.get('padding')
        return dict(image=image, start_position=start_pos, input_velocity=input_velocity, velocity=velocity,
                    padding=padding)
