'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
import random

from core.AgentMovable import AgentMovable
import logging as log
from wator.agents.FishAgent import FishAgent


class SharkAgent(AgentMovable):

    def __init__(self, x, y, sma, breedingAge, starvationTime):
        AgentMovable.__init__(self, x, y, sma)

        self.age = 0
        self.breedingAgeCount = self.breedingAge = breedingAge
        self.starvationTimeCount = self.starvationTime = starvationTime

    def action(self):
        self.age += 1
        self.breedingAgeCount -= 1
        self.starvationTimeCount -= 1

        # am I dead ?
        if self.starvationTimeCount <= 0:
            self.sma.removeSharkAgent(self)
            log.debug("I'm DEAD!")
            return

        # make a baby shark!
        if self.breedingAgeCount <= 0:
            self.breedingAgeCount = self.breedingAge

            neighboursEmpty = self.sma.env.neighboursEmptyOf(self.x, self.y)
            for x, y in neighboursEmpty:
                self.sma.addSharkAgent(x, y, self.breedingAge, self.starvationTime)
                log.debug("Baby shark!")
                return

        # looking for food
        neighbours = self.sma.env.neighboursAgentsOf(self.x, self.y)
        fishes = []
        for agent in neighbours:
            if isinstance(agent, FishAgent):
                fishes.append(agent)

        if len(fishes) > 0:
            self.starvationTimeCount = self.starvationTime

            self.sma.removeFishAgent(random.choice(fishes))
            self.moveTo(agent.x, agent.y)
            log.debug("I eat a Fish! Miam!")

        # else
        self.randomMove()
