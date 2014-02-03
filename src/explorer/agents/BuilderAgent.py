'''
Created on 3 fevr. 2014

@author: Alexandre Bonhomme
'''
import random

from core.agents.AgentMovable import AgentMovable
from core.agents.AgentWall import AgentWall
import logging as log

class BuilderAgent(AgentMovable):

    MIN_PATH_LEN = 5
    MAX_PATH_LEN = 15

    def __init__(self, x, y, sma, totalSteps):
        AgentMovable.__init__(self, x, y, sma)

        self.partialStep = 0
        self.totalSteps = totalSteps
        self.currentStep = 0

    '''
    Mine a all wall which is in the path of the agent
    The direction is randomly selected over the neighbours of Von Neumann.
    The paths length is randomly selected between two bounds
    '''
    def action(self):
        if self.currentStep >= self.totalSteps:
            self.sma.removeAllAgent()
            self.sma.initExplorers(self.sma.explorers)
            return

        self.currentStep += 1

        if self.partialStep == 0:
            self.partialStep = random.randrange(self.MIN_PATH_LEN, self.MAX_PATH_LEN, 1)
            self.direction = random.choice(self._vonNeumannDirection())

        self.partialStep -= 1
        x, y = self.x + self.direction[0], self.y + self.direction[1]
        try:
            cell = self.sma.env.get(x, y)
            if isinstance(cell, AgentWall):
                # we mine the wall
                self.sma.env.remove(x, y)

            # we take his place
            self.moveTo(x, y)

        # if we're out of bound we check wait the next iteration
        except:
            self.partialStep = 0
            return

    '''
    Return possible directions in the neighbours of Von Neumann
    '''
    def _vonNeumannDirection(self):
        neighbours = []

        if self.x - 1 >= 0:
            neighbours.append([-1, 0])
        if self.x + 1 < self.sma.env.rows:
            neighbours.append([1, 0])

        if self.y - 1 >= 0:
            neighbours.append([0, -1])
        if self.y + 1 < self.sma.env.cols:
            neighbours.append([0, 1])

        return neighbours
