'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentMovable import AgentMovable


class PacmanAgent(AgentMovable):

    def __init__(self, x, y, sma):
        AgentMovable.__init__(self, x, y, sma)

    def action(self):
        self.randomMoveInNeighborhood()
