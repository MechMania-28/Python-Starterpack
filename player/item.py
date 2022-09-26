from enum import Enum
from player.stat_set import StatSet

class ItemModel():
    def __init__(self, stat_set, item_timer, cost) -> None:
        self.stat_set = stat_set
        self.item_timer = item_timer
        self.cost = cost

class Item(Enum):
    PROCRUSTEAN_IRON = ItemModel(StatSet(0, 0, 0, 0), 1, 8)
    HEAVY_BROADSWORD = ItemModel(StatSet(0, 0, 0, 0), -1, 8)
    MAGIC_STAFF = ItemModel(StatSet(0, 0, 0, 0), 0, 8)
    STEEL_TIPPED_ARROW = ItemModel(StatSet(0, 0, 0, 0), 0, 8)
    ANEMOI_WINGS = ItemModel(StatSet(0, 0, 2, 0), -1, 10)
    STRENGTH_POTION = ItemModel(StatSet(0, 4, 0, 0), 1, 5)
    SPEED_POTION = ItemModel(StatSet(0, 0, 2, 0), 1, 5)
    DEXTERITY_POTION = ItemModel(StatSet(0, 0, 0, 2), 1, 5)
    NONE = ItemModel(StatSet(0, 0, 0, 0), -1, 100)

