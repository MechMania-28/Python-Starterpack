from action.action import Action
from game.item import Item


class BuyAction(Action):
  item = Item.NONE.name
  

  def __init__(self, executor: int, item: Item) -> None:
    super().__init__(executor)
    self.item = item.name