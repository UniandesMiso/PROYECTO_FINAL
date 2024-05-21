import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_blink import CBlink
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_menu_tag import CMenuTag
from src.engine.service_locator import ServiceLocator
from src.utils.window_localizer_util import window_position


def build_font(
    font_cfg: dict,
) -> tuple:
    font_color_cfg: dict = font_cfg.get('color')
    font: pygame.font.Font = ServiceLocator.fonts_services.get_font(font_cfg.get("font"), font_cfg.get("size"))
    color: pygame.Color = pygame.Color(font_color_cfg.get('r'), font_color_cfg.get('g'), font_color_cfg.get('b'))
    font_surf: CSurface = CSurface.from_text(
        text=font_cfg.get("text"),
        font=font,
        color=color
    )
    return font_surf


class WorldEntityMenu(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        font_cfg: dict = kwargs.get("font_cfg")
        position: pygame.Vector2 = kwargs.get("position")
        final_position: int = position.y
        position.y+=248

        world.add_component(cuad_entity, build_font(font_cfg))
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CVelocity(kwargs.get("velocity")))
        world.add_component(cuad_entity, CMenuTag(final_position))

        if font_cfg.get('blink_rate'):
            world.add_component(cuad_entity, CBlink(font_cfg.get('blink_rate')))
        if font_cfg.get('sound'):
            ServiceLocator.sounds_services.play(font_cfg.get('sound'))
        return cuad_entity
