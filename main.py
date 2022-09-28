from cmath import e
from distutils.log import debug
from enum import Enum, auto
import json
import logging
import sys


import jsonpickle
from pip import main
from action.attack_action import AttackAction
from action.buy_action import BuyAction
from action.move_action import MoveAction
from action.use_action import UseAction
from config import Config
from game.game_state import GameState
from networking.client import Client
from networking.comm_state import CommState
from player.character_class import CharacterClass
from player.item import Item
from player.player_state import PlayerState
from player.position import Position
from player.stat_set import StatSet

from strategy.starter_strategy import  StarterStrategy
from strategy.strategies_for_each_bot import strategy_as_bot0, strategy_as_bot1, strategy_as_bot2, strategy_as_bot3

class Phase(Enum):
    USE = auto()
    MOVE = auto()
    ATTACK = auto()
    BUY = auto()

def main():

  strategy = StarterStrategy()

  if len(sys.argv) >= 3 and sys.argv[2] == 'debug':
    logging.basicConfig(    
      format='%(asctime)s %(levelname)-8s %(module)-8s %(message)s',
      level=logging.DEBUG,
      datefmt='%Y-%m-%d %H:%M:%S'
    )
  else:
    logging.basicConfig(    
      format='%(asctime)s %(levelname)-8s %(module)-8s %(message)s',
      level=logging.INFO,
      datefmt='%Y-%m-%d %H:%M:%S'
    )

  player_index = -1
  if len(sys.argv) >= 2 and sys.argv[1].isdigit():
    player_index = int(sys.argv[1])
  else:
    logging.warn("Invalid player index.")
    return

  client = Client(Config.ports[player_index])

  client.connect()



  logging.debug("start")



  comm_state = CommState.START


  while comm_state != CommState.END:
    logging.debug((comm_state, comm_state==CommState.START))

    if comm_state == CommState.START:
      logging.debug("Waiting for wake...")
      data = client.read()
      if (data.startswith("wake")):
        comm_state = CommState.NUM_ASSIGN
        continue
      continue
    
    if comm_state == CommState.NUM_ASSIGN:
      read = client.read()
      player_index = int(read)
      logging.debug(("Received player index", player_index))
      comm_state = CommState.CLASS_REPORT

      if player_index == 0 and strategy_as_bot0 != None:
          strategy = strategy_as_bot0
      if player_index == 1 and strategy_as_bot1 != None:
          strategy = strategy_as_bot1
      if player_index == 2 and strategy_as_bot2 != None:
          strategy = strategy_as_bot2
      if player_index == 3 and strategy_as_bot3 != None:
          strategy = strategy_as_bot3

      continue

    if comm_state == CommState.CLASS_REPORT:
      character_class = strategy.strategy_initialize()
      client.write(jsonpickle.encode(character_class.name))
      comm_state = CommState.END


  phase = Phase.USE 
  while(True):

    data = client.read()
    
    if (data.startswith("fin")) :
      logging.info("Exiting.")
      break

    game_state = parse_json_as_game_state(data)

    if phase == Phase.USE :
      use_action = UseAction(player_index, strategy.use_action_decision(game_state, player_index))
      logging.debug(jsonpickle.encode(use_action))
      client.write(jsonpickle.encode(use_action, unpicklable=False))
      phase = Phase.MOVE
      continue
    if phase == Phase.MOVE :
      move_action = MoveAction(player_index, strategy.move_action_decision(game_state, player_index))
      client.write(jsonpickle.encode(move_action, unpicklable=False))
      phase = Phase.ATTACK
      continue
    if phase == Phase.ATTACK :
      attack_action = AttackAction(player_index, strategy.attack_action_decision(game_state, player_index))
      client.write(jsonpickle.encode(attack_action, unpicklable=False))
      phase = Phase.BUY
      continue
    if phase == Phase.BUY :
      buy_action = BuyAction(player_index, strategy.buy_action_decision(game_state, player_index))
      client.write(jsonpickle.encode(buy_action, unpicklable=False))
      phase = Phase.USE
    
  client.disconnect()

""" parse json string into a GameState Object."""
def parse_json_as_game_state(data: str) -> GameState:
  gamestate_dict = json.loads(data)

  player_state_list = []
  for player_state_dict in gamestate_dict['player_states']:
    player_state = PlayerState()
    
    player_state.character_class = CharacterClass[player_state_dict['class']]

    position_dict = player_state_dict['position']
    player_state.position = Position(x=position_dict['x'], y=position_dict['y'])

    player_state.gold = player_state_dict['gold']
    player_state.score = player_state_dict['score']
    player_state.health = player_state_dict['health']

    player_state.item = Item[player_state_dict['item']]

    stat_set_dict = player_state_dict['stat_set']
    stat_set = StatSet(
      max_health=stat_set_dict['maxHealth'],
      speed=stat_set_dict['speed'],
      damage=stat_set_dict['damage'],
      range=stat_set_dict['range']
    )
    player_state.stat_set = stat_set

    player_state_list.append(player_state)

  game_state = GameState(turn=gamestate_dict['turn'], player_state_list=player_state_list)
  return game_state

if __name__ == '__main__':
  main()