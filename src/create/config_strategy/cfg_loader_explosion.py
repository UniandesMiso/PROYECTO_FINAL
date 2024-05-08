import json

from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy

EXPLOSION_PATH = 'assets/cfg/explosions.json'


class CFGLoaderExplosion(CFGLoaderStrategy):

    def load_cfg(self, **kwargs) -> dict:
        with open(EXPLOSION_PATH, "r") as explosion_loaded:
            return json.load(explosion_loaded)
