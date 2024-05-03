
import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_input_command import CInputCommand
from src.engine.service_locator import ServiceLocator


class WorldEntityInputCommand(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        return cuad_entity
