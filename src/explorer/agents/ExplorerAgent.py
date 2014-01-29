'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentMovable import AgentMovable


class ExplorerAgent(AgentMovable):

    def __init__(self, x, y, sma):
        AgentMovable.__init__(self, x, y, sma)

        self.color
        self.dijkstraGrid = [[None for _ in xrange(self.env.cols)] for _ in xrange(self.env.rows)]

    def action(self):
        pass
