from enum import Enum
import math
import random
from typing import Any, Type

import config

from player.position import Position

def manhattan_distance(p1: Position, p2: Position) -> int:
    return math.abs(p1.getX() - p2.getX()) + math.abs(p1.getY() - p2.getY())

def chebyshev_distance(p1: Position, p2: Position) -> int:
    return math.max(math.abs(p1.getX() - p2.getX()), math.abs(p1.getY() - p2.getY()))

def in_bounds(p: Position) -> bool:
    #  Assume board runs from 0 to BOARD_SIZE - 1
    return ((p.getX() >= 0) and (p.getX() < config.BOARD_SIZE) and (p.getY() >= 0) and (p.getY() < config.BOARD_SIZE))

def random_enum(clazz: Enum):
    return random.choice(list(clazz))