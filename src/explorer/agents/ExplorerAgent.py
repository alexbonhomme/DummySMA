'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentMovable import AgentMovable


class ExplorerAgent(AgentMovable):

    def __init__(self, x, y, sma, color = 'light blue'):
        AgentMovable.__init__(self, x, y, sma)

        self.color = color
        self.dijkstraGrid = [[None for _ in xrange(self.sma.env.cols)] for _ in xrange(self.sma.env.rows)]

    def action(self):
        pass
