'''
Created on 20 janv. 2014

@author: Alexandre Bonhomme
'''
from core.AgentBase import AgentBase

class WallAgent(AgentBase):

    def __init__(self, x, y, sma):
        AgentBase.__init__(self, x, y, sma)

    def action(self):
        pass
