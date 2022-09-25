from player.stat_set import StatSet
import stat_set

class Item:
    """ generated source for enum Item """
    def affect(self, player):
        """ generated source for method affect """
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_0(self, player):
        """ generated source for method affect_0 """

    @affect.register(object, PlayerState)
    def affect_1(self, player):
        """ generated source for method affect_1 """
        player.setCharacterClass(CharacterClass.KNIGHT)
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_2(self, player):
        """ generated source for method affect_2 """
        player.setCharacterClass(CharacterClass.WIZARD)
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_3(self, player):
        """ generated source for method affect_3 """
        player.setCharacterClass(CharacterClass.ARCHER)
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_4(self, player):
        """ generated source for method affect_4 """

    @affect.register(object, PlayerState)
    def affect_5(self, player):
        """ generated source for method affect_5 """
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_6(self, player):
        """ generated source for method affect_6 """
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_7(self, player):
        """ generated source for method affect_7 """
        player.setEffectTimer(self.getEffectTimer())

    @affect.register(object, PlayerState)
    def affect_8(self, player):
        """ generated source for method affect_8 """
        #  Do nothing

    #  The effect the item has on a player 
    @affect.register(object, PlayerState)
    def affect_9(self, player):
        """ generated source for method affect_9 """

    #  The buff/debuff StatSet granted by this item. 
    statSet = StatSet()

    #  Represents the duration of this item's effect
    #    * -1 means permanent, 0 means one time, positive means multiple turns
    effectTimer = int()

    #  Represents the cost of the item 
    cost = int()

    def __init__(self, statSet, itemTimer, cost):
        """ generated source for method __init__ """
        self.statSet = statSet
        self.effectTimer = itemTimer
        self.cost = cost

    def getStatSet(self):
        """ generated source for method getStatSet """
        return self.statSet

    def getEffectTimer(self):
        """ generated source for method getEffectTimer """
        return self.effectTimer

    def isPermanent(self):
        """ generated source for method isPermanent """
        return (self.effectTimer == -1)

    def getCost(self):
        """ generated source for method getCost """
        return self.cost

Item.SHIELD = Item(StatSet(0, 0, 0, 0))

Item.PROCRUSTEAN_IRON = Item(StatSet(0, 0, 0, 0))

Item.HEAVY_BROADSWORD = Item(StatSet(0, 0, 0, 0))

Item.MAGIC_STAFF = Item(StatSet(0, 0, 0, 0))

Item.STEEL_TIPPED_ARROW = Item(StatSet(0, 0, 0, 0))

Item.ANEMOI_WINGS = Item(StatSet(0, 0, 2, 0), 0)

Item.STRENGTH_POTION = Item(StatSet(0, 4, 0, 0))

Item.SPEED_POTION = Item(StatSet(0, 0, 2, 0))

Item.DEXTERITY_POTION = Item(StatSet(0, 0, 0, 2))

Item.NONE = Item(StatSet(0, 0, 0, 0))
