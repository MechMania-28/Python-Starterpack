from enum import Enum, auto
import json
import logging
from optparse import OptionParser
import sys


import jsonpickle
from pip import main
from action.attack_action import AttackAction
from action.buy_action import BuyAction
from action.move_action import MoveAction
from action.use_action import UseAction
from game.game_state import GameState
from networking.client import Client
from networking.comm_state import CommState
from game.character_class import CharacterClass
from game.item import Item
from game.player_state import PlayerState
from game.position import Position
from game.stat_set import StatSet
import config
from strategy.strategy_config import get_strategy

class Phase(Enum):
    USE = auto()
    MOVE = auto()
    ATTACK = auto()
    BUY = auto()



def main():

  parser = OptionParser()
  parser.add_option("--debug", "-d", dest="debug", action="store_true", help="Turn on debug mode", default=False)
  (options, _) = parser.parse_args()

  if options.debug == True:
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

  logging.info("Welcome to Mechmania 28 Python bot!")

  player_index = -1
  if len(sys.argv) >= 2 and sys.argv[1].isdigit() and int(sys.argv[1]) >= 0 and int(sys.argv[1]) < 4:
    player_index = int(sys.argv[1])
  else:
    logging.warn("Invalid or empty player number. Please specify a valid player number.")
    return

  strategy = get_strategy(player_index=player_index)


  client = Client(config.PORTS[player_index])

  client.connect()

  logging.info("Connected to Engine. Setting up for game...")
  comm_state = CommState.START

  while comm_state != CommState.END:
    logging.debug((comm_state, comm_state==CommState.START))

    if comm_state == CommState.START:
      logging.info("Waiting for wake...")
      data = client.read()
      if (data.startswith("wake")):
        comm_state = CommState.NUM_ASSIGN
        continue
      continue
    
    if comm_state == CommState.NUM_ASSIGN:
      read = client.read()
      player_index = int(read)
      logging.info(("Received player index", player_index))
      comm_state = CommState.CLASS_REPORT
      continue

    if comm_state == CommState.CLASS_REPORT:
      character_class = strategy.strategy_initialize(player_index)
      client.write(jsonpickle.encode(character_class.name))
      comm_state = CommState.END

  logging.info("Finished setup. Running game...")

  phase = Phase.USE 
  while(True):

    data = client.read()
    
    if (data.startswith("fin")) :
      break
    
    game_state = None
    
    try:
      game_state = parse_json_as_game_state(data)
    except json.JSONDecodeError as e:
      logging.warn(e)
    
    if game_state is None:
      return

    if phase == Phase.USE :
      logging.info("Turn: " + str(game_state.turn))
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
  logging.info("Completed!. Check your output at Engine\\gamelogs.")

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