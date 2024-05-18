import src.engine.game_engine
from src.engine.scenes_strategy.play_scene import PlayScene
from src.engine.scenes_strategy.scene_strategy import SceneStrategy


class SceneExecutor:

    def __init__(self, game_engine: 'src.engine.game_engine.GameEngine', window_cfg: dict):
        self.scene_dict = {
            'PLAY': PlayScene(game_engine, window_cfg)
        }

    def scene_executor(self, scene_name: str, **kwargs) -> SceneStrategy:
        return self.scene_dict.get(scene_name)
