from action.action import Action


class UseAction(Action):
  use = False
  def __init__(self, executor: int, use: bool) -> None:
    super().__init__(executor)
    self.use = use