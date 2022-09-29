from game.character_class import CharacterClass
from game.item import Item
from game.position import Position
from game.stat_set import StatSet


class PlayerState:
  def __init__(self) -> None:
    self.character_class = CharacterClass.KNIGHT
    self.item = Item.NONE
    self.position = Position()
    self.gold = 0
    self.score = 0
    self.health = 0
    self.stat_set = StatSet()
  
