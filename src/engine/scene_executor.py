import src.engine.game_engine
from src.engine.scenes_strategy.menu_scene import MenuScene
from src.engine.scenes_strategy.play_scene import PlayScene
from src.engine.scenes_strategy.scene_strategy import SceneStrategy


class SceneExecutor:

    def __init__(self, game_engine: 'src.engine.game_engine.GameEngine', window_cfg: dict):
        self.game_engine = game_engine
        self.window_cfg = window_cfg
        self.scene_dict = {
            'MENU': MenuScene(self.game_engine, self.window_cfg)
        }

    def scene_executor(self, scene_name: str, **kwargs) -> SceneStrategy:
        return self.scene_dict.get(scene_name, PlayScene(self.game_engine, self.window_cfg))
