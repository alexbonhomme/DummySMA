'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.AgentMovable import AgentMovable


class GhostAgent(AgentMovable):

    def __init__(self, x, y, sma):
        AgentMovable.__init__(self, x, y, sma)

    def action(self):
        pass
