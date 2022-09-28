from strategy.new_strategy import NewStrategy
from strategy.starter_strategy import StarterStrategy
from strategy.strategy import Strategy

def get_strategy(player_index: int) -> Strategy:
  return StarterStrategy()