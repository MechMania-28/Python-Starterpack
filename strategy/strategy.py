from abc import abstractmethod
from game.game_state import GameState
from game.item import Item

from game.position import Position


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