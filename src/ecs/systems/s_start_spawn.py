import random

import pygame

import esper
from src.create.world_entities_executor import WorldEntitiesExecutor
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_start_tag import CStartTag


def system_create_starts(world: esper.World, starts_cfg: dict, screen_vector: pygame.Vector2):
    strategy_world_entity = WorldEntitiesExecutor()
    colors: list = starts_cfg.get('star_colors')
    velocity_speed = starts_cfg.get('vertical_speed')
    blink_rate = starts_cfg.get('blink_rate')
    screen_width = screen_vector.x
    screen_height = screen_vector.y

    for i in range(0, starts_cfg.get('number_of_stars', 0)):
        color: dict = random.choice(colors)
        position_x: int = random.randint(1, screen_width)
        position_y: int = random.randint(0, screen_height)
        strategy_world_entity.world_entity_executor(
            world=world,
            entity_type="START_ENTITY",
            velocity=random.randint(velocity_speed.get('min'), velocity_speed.get('max')),
            blink=random.choice([blink_rate.get('min'), blink_rate.get('max')]),
            color=pygame.Color(color.get('r'), color.get('g'), color.get('b')),
            position=pygame.Vector2(position_x, position_y)
        )


def system_start_positions(world: esper.World, screen_vector: pygame.Vector2):
    components = world.get_components(CTransform, CStartTag)
    c_t: CTransform
    c_s: CStartTag
    for _, (c_t, c_s) in components:
        if c_t.pos.y > screen_vector.y:
            c_t.pos.y = 0
