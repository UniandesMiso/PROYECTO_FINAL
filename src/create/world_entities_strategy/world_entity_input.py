
import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_input_command import CInputCommand
from src.engine.service_locator import ServiceLocator


class WorldEntityInputCommand(WorldEntityStrategy):

    def create_entity(self, world: esper.World, **kwargs) -> int:
        cuad_entity = world.create_entity()
        world.add_component(cuad_entity, CInputCommand(name=kwargs.get('name'), key=kwargs.get('key')))
        if kwargs.get('sound'):
            ServiceLocator.sounds_services.play(kwargs.get('sound'))
        return cuad_entity
