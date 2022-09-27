from typing import List
from player.player_state import PlayerState

class GameState:
  def __init__(self, turn: int, player_state_list: List[PlayerState]) -> None:
    self.turn = turn
    self.player_state_list = player_state_list
