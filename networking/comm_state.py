from enum import Enum, auto


class CommState(Enum):
  START = auto()
  NUM_ASSIGN = auto()
  CLASS_REPORT = auto()
  IN_GAME = auto()
  END = auto()