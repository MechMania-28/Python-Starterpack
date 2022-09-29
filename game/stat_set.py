

class StatSet(object):

    def __init__(self, max_health: int=0, damage: int=0, speed: int=0, range: int=0):
        self.max_health = max_health
        self.damage = damage
        self.speed = speed
        self.range = range

    def plus(self, other):
        return StatSet(self.maxHealth + other.maxHealth, self.damage + other.damage, self.speed + other.speed, self.range + other.range)
