'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
import logging as log
from core.agents.AgentMovable import AgentMovable


class FishAgent(AgentMovable):

    def __init__(self, x, y, sma, breedingAge):
        AgentMovable.__init__(self, x, y, sma)

        self.age = 0
        self.breedingAgeCount = self.breedingAge = breedingAge

    def action(self):
        self.age += 1
        self.breedingAgeCount -= 1

        if self.breedingAgeCount <= 0:
            self.breedingAgeCount = self.breedingAge

            neighboursEmpty = self.sma.env.neighboursEmptyOf(self.x, self.y)
            for x, y in neighboursEmpty:
                self.sma.addFishAgent(x, y, self.breedingAge)
                log.debug("Baby fish!")
                return
        else:
            self.randomMoveInNeighborhood()

