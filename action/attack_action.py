from mimetypes import init
from action.action import Action


class AttackAction(Action):
  target = 0
  def __init__(self, executor: int, target: int) -> None:
    super().__init__(executor)
    self.target = target