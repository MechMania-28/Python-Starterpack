import player.character_class

import player.item

import player.position
from strategy.strategy import Strategy

import util.utility

import java.util.concurrent.ThreadLocalRandom

import strategy

class RandomStrategy(Strategy):
    """ generated source for class RandomStrategy """
    def strategyInitialize(self):
        """ generated source for method strategyInitialize """
        return CharacterClass.WIZARD

    def moveActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method moveActionDecision """
        while True:
            if Utility.manhattanDistance(Position(randomX, randomY), gameState.getPlayerStateByIndex(myPlayerIndex).getPosition()) <= gameState.getPlayerStateByIndex(myPlayerIndex).getCharacterClass().getStatSet().getSpeed():
                return Position(randomX, randomY)

    def attackActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method attackActionDecision """
        res = 0
        i = 0
        while i < 4:
            print "distance of " + i + ": ",
            print Utility.squareDistance(gameState.getPlayerStateByIndex(myPlayerIndex).getPosition(), gameState.getPlayerStateByIndex(i).getPosition())
            print "my range: " + gameState.getPlayerStateByIndex(myPlayerIndex).getCharacterClass().getStatSet().getRange()
            if i != myPlayerIndex:
                if Utility.squareDistance(gameState.getPlayerStateByIndex(myPlayerIndex).getPosition(), gameState.getPlayerStateByIndex(i).getPosition()) <= gameState.getPlayerStateByIndex(myPlayerIndex).getCharacterClass().getStatSet().getRange():
                    return i
                res = i
            i += 1
        return res

    def buyActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method buyActionDecision """
        return Item.NONE

    def useActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method useActionDecision """
        return False