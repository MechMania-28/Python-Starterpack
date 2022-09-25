from abc import abstractmethod
import starterpack.player.CharacterClass

import starterpack.player.Item

import starterpack.player.Position

class Strategy(object):
    """ generated source for interface Strategy """
    @abstractmethod
    def strategyInitialize(self):
        """ generated source for method strategyInitialize """

    @abstractmethod
    def moveActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method moveActionDecision """

    @abstractmethod
    def attackActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method attackActionDecision """

    @abstractmethod
    def buyActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method buyActionDecision """

    @abstractmethod
    def useActionDecision(self, gameState, myPlayerIndex):
        """ generated source for method useActionDecision """