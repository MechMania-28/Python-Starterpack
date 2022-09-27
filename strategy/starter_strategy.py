from random import Random
from game.game_state import GameState
import player.character_class

from player.item import Item

from player.position import Position
from strategy.strategy import Strategy

class StarterStrategy(Strategy):
    def strategy_initialize(self):
        return player.character_class.CharacterClass.WIZARD

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        return Position()

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return Random().randint(0, 3)

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False