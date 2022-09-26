import math
import random

import config

import player.position

class Utility(object):
    """ generated source for class Utility """
    @classmethod
    def manhattanDistance(cls, p1, p2):
        """ generated source for method manhattanDistance """
        return math.abs(p1.getX() - p2.getX()) + math.abs(p1.getY() - p2.getY())

    @classmethod
    def squareDistance(cls, p1, p2):
        """ generated source for method squareDistance """
        return math.max(math.abs(p1.getX() - p2.getX()), math.abs(p1.getY() - p2.getY()))

    @classmethod
    def randomInt(cls, min, max):
        """ generated source for method randomInt """
        return random.randint(min, max + 1)

    @classmethod
    def inBounds(cls, p):
        """ generated source for method inBounds """
        #  Assume board runs from 0 to BOARD_SIZE - 1
        return ((p.getX() >= 0) and (p.getX() < config.BOARD_SIZE) and (p.getY() >= 0) and (p.getY() < config.BOARD_SIZE))

    @classmethod
    def randomEnum(cls, clazz):
        """ generated source for method randomEnum """
        x = random.nextInt(clazz.getEnumConstants().length)
        return clazz.getEnumConstants()[x]