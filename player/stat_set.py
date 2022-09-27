from tokenize import Number


class StatSet(object):

    def __init__(self) -> None:
        self.max_health = 0
        self.damage = 0
        self.speed = 0
        self.range = 0

    def __init__(self, max_health: int, damage: int, speed: int, range: int):
        self.max_health = max_health
        self.damage = damage
        self.speed = speed
        self.range = range

    def plus(self, other):
        return StatSet(self.maxHealth + other.maxHealth, self.damage + other.damage, self.speed + other.speed, self.range + other.range)
