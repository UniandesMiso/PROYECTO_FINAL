import json

import pygame

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

WINDOW_PATH = 'assets/cfg/window.json'


class CFGLoaderWindow(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(WINDOW_PATH, 'r') as window_loaded:
            json_window = json.load(window_loaded)
            json_size = json_window.get('size', dict(w=200, h=180))
            json_color = json_window.get('bg_color', dict(r=255, g=255, b=255))
            json_color_r = json_color.get('r')
            json_color_g = json_color.get('g')
            json_color_b = json_color.get('b')
            screen_size = (json_size.get('w'), json_size.get('h'))
            screen_bg = (json_color_r, json_color_g, json_color_b)

            game_screen = pygame.display.set_mode(screen_size, pygame.SCALED)
            game_framerate = json_window.get('framerate', 60)
            screen_vector = pygame.Vector2(screen_size)

        return dict(bg=screen_bg, screen=game_screen, framerate=game_framerate, screen_vector=screen_vector)
