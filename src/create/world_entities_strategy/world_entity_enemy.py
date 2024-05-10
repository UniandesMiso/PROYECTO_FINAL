import pygame

import esper
from src.create.world_entities_strategy.world_entity_strategy import WorldEntityStrategy
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_enemy_tag import CEnemyTag


class WorldEntityEnemy(WorldEntityStrategy):

    def create_entity(self, world: esper.World, cuad_entity: int, **kwargs) -> int:
        enemy_cfg: dict = kwargs.get("entity_cfg")
        position: pygame.Vector2 = kwargs.get('position')

        world.add_component(cuad_entity, kwargs.get('img_surf'))
        world.add_component(cuad_entity, CTransform(position))
        world.add_component(cuad_entity, CVelocity(kwargs.get('velocity')))
        world.add_component(cuad_entity, CEnemyTag(enemy_cfg.get('dead_points', 0)))
        if enemy_cfg.get('animations'):
            world.add_component(cuad_entity, CAnimation(enemy_cfg.get('animations')))
        return cuad_entity
