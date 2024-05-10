from enum import Enum


class TypeBullet(Enum):
    PLAYER = 1
    ENEMY = 0


class CBulletTag:
    def __init__(self, _type: TypeBullet) -> None:
        self._type = _type
