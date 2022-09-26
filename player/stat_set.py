class StatSet(object):
    """ generated source for class StatSet """
    max_health = int()
    damage = int()
    speed = int()
    range = int()

    def __init__(self, max_health, damage, speed, range):
        """ generated source for method __init__ """
        self.max_health = max_health
        self.damage = damage
        self.speed = speed
        self.range = range

    def plus(self, other):
        """ generated source for method plus """
        return StatSet(self.maxHealth + other.maxHealth, self.damage + other.damage, self.speed + other.speed, self.range + other.range)

    def get_max_health(self):
        """ generated source for method getMaxHealth """
        return self.maxHealth

    def get_damage(self):
        """ generated source for method getDamage """
        return self.damage

    def get_speed(self):
        """ generated source for method getSpeed """
        return self.speed

    def get_range(self):
        """ generated source for method getRange """
        return self.range