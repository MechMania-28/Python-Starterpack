from action.action import Action
from player.position import Position


class MoveAction(Action):
  destination = Position()
  def __init__(self, executor: int, destination: Position) -> None:
    super().__init__(executor)
    self.destination = destination