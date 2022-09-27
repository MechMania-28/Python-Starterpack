from abc import abstractmethod
from game_state.game_state import GameState
from player.item import Item

from player.position import Position


class Strategy(object):
    @abstractmethod
    def strategy_initialize(self) -> None:
        pass
    @abstractmethod
    def move_action_decision(self, game_state: GameState, my_player_index) -> Position:
        pass

    @abstractmethod
    def attack_action_decision(self, game_state: GameState, my_player_index) -> int:
        pass

    @abstractmethod
    def buy_action_decision(self, game_state: GameState, my_player_index) -> Item:
        pass

    @abstractmethod
    def use_action_decision(self, game_state: GameState, my_player_index) -> bool:
        pass