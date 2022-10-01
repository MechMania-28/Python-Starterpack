from enum import Enum

from game.stat_set import StatSet


class CharacterClass(Enum):
  KNIGHT = StatSet(9, 6, 2, 1)
  WIZARD = StatSet(6, 5, 3, 2)
  ARCHER = StatSet(3, 3, 4, 3)