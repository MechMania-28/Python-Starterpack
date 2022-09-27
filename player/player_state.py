from turtle import position
from player.character_class import CharacterClass
from player.item import Item
from player.position import Position
from player.stat_set import StatSet


class PlayerState:
  def __init__(self) -> None:
    self.character_class = CharacterClass.KNIGHT
    self.item = Item.NONE
    self.position = Position()
    self.gold = 0
    self.score = 0
    self.health = 0
    self.stat_set = StatSet()
  
