from src.create.config_strategy.cfg_loader_font import CFGLoaderFont
from src.create.config_strategy.cfg_loader_enemy import CFGLoaderEnemy
from src.create.config_strategy.cfg_loader_explosion import CFGLoaderExplosion
from src.create.config_strategy.cfg_loader_interface import CFGLoaderInterface
from src.create.config_strategy.cfg_loader_level import CFGLoaderLevel
from src.create.config_strategy.cfg_loader_none import CFGLoaderNone
from src.create.config_strategy.cfg_loader_player import CFGLoaderPlayer
from src.create.config_strategy.cfg_loader_starts import CFGLoaderStarts
from src.create.config_strategy.cfg_loader_strategy import CFGLoaderStrategy
from src.create.config_strategy.cfg_loader_window import CFGLoaderWindow


class CFGLoaderExecutor:

    def __init__(self):
        self.str_dict = {
            'LEVEL_CFG': CFGLoaderLevel(),
            'PLAYER_CFG': CFGLoaderPlayer(),
            'ENEMY_CFG': CFGLoaderEnemy(),
            'FONT_CFG': CFGLoaderFont(),
            'EXPLOSION_CFG': CFGLoaderExplosion(),
            'INTERFACE_CFG': CFGLoaderInterface(),
            'WINDOW_CFG': CFGLoaderWindow(),
            'STARTS_CFG': CFGLoaderStarts()
        }

    def cfg_executor(self, cfg_type, **kwargs) -> dict:
        cfg_loader: CFGLoaderStrategy = self.str_dict.get(cfg_type, CFGLoaderNone())
        return cfg_loader.load_cfg(**kwargs)
