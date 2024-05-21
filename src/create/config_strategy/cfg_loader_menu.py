import json

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

MENU_PATH = 'assets/cfg/menu.json'


class CFGLoaderMenu(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(MENU_PATH, "r") as menu_loaded:
            return json.load(menu_loaded)
