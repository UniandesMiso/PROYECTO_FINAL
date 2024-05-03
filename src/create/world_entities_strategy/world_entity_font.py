import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_font_tag import CFontTag, FontType
from src.engine.service_locator import ServiceLocator
from src.utils.window_localizer_util import window_position


class WorldEntityFont(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        return cuad_entity
