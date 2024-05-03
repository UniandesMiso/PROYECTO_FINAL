from abc import ABC, abstractmethod

import esper


class WorldEntityStrategy(ABC):

    @abstractmethod
    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        ...
