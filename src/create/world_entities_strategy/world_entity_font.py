import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_font_tag import CFontTag, FontType
from src.engine.service_locator import ServiceLocator
from src.utils.window_localizer_util import window_position


def build_font(
        font_cfg: dict,
        screen_zone: pygame.Rect,
) -> tuple:
    font_color_cfg: dict = font_cfg.get('color')
    font: pygame.font.Font = ServiceLocator.fonts_services.get_font(font_cfg.get("font"), font_cfg.get("size"))
    color: pygame.Color = pygame.Color(font_color_cfg.get('r'), font_color_cfg.get('g'), font_color_cfg.get('b'))
    font_surf: CSurface = CSurface.from_text(
        text=font_cfg.get("text"),
        font=font,
        color=color
    )
    position: pygame.Vector2 = window_position(screen_zone, font_cfg.get('fixed'), font_surf,
                                               font_cfg.get('padding', 0))
    return font_surf, position


class WorldEntityFont(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        zone_cfg: pygame.Rect = kwargs.get("screen_zone")
        font_cfg: dict = kwargs.get("font_cfg")

        font_surf, position = build_font(font_cfg, zone_cfg)
        world.add_component(cuad_entity, font_surf)
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CFontTag(kwargs.get('tag', FontType.STATIC)))
        return cuad_entity
