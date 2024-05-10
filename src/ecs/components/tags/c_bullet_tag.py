from enum import Enum


class TypeBullet(Enum):
    PLAYER = 1
    ENEMY = 0


class CBulletTag:
    def __init__(self, bullet_type: TypeBullet) -> None:
        self.bullet_type = bullet_type

