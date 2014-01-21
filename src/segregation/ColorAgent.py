'''
Created on 21 janv. 2014

@author: Alexandre Bonhomme
'''
from core.AgentMovable import AgentMovable
import logging as log


class ColorAgent(AgentMovable):

    def __init__(self, x, y, sma, color, satisfactionThreshold):
        AgentMovable.__init__(self, x, y, sma)

        self.color = color
        self.satisfaction = 0.0
        self.satisfactionThreshold = satisfactionThreshold

    '''
    Agent move only if is satisfaction level is under the threshold.
    He could be stuck if no empty place are found
    '''
    def action(self):
        self.satisfaction = self._computeSatisfaction()

        if self.satisfaction < self.satisfactionThreshold:
            x, y = self.sma.env.randomEmptyPosition()
            if not self.sma.env.moveTo(x, y):
                log.warn('Agent stuck! x: %d y: %d', self.x, self.y)

    '''
    Compute the satisfaction percentage by counting the number of
    neighbours agents which has a different color.
    '''
    def _computeSatisfaction(self):
        neighbours = self.sma.env.neighboursAgentsOf(self.x, self.y)

        others = 0
        for agent in neighbours:
            if agent.color != self.color:
                others += 1

        return float(others) / 8.0
