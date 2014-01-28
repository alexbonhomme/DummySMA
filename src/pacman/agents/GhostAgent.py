'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.AgentMovable import AgentMovable


class GhostAgent(AgentMovable):

    def __init__(self, x, y, sma, ident):
        AgentMovable.__init__(self, x, y, sma)

        # ID of the ghost (to display specific Image)
        self.id = ident

    def action(self):
        pass
