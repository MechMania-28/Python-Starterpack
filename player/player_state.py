from turtle import position
from player.character_class import CharacterClass
from player.item import Item
from player.position import Position


class PlayerState:
  character_class = CharacterClass.KNIGHT
  item = Item.NONE
  position = Position()
  gold = 0
  score = 0
  effect_timer = 0
  health = 0
  
