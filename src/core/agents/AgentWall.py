'''
Created on 20 janv. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentBase import AgentBase

class AgentWall(AgentBase):

    def __init__(self, x, y, sma):
        AgentBase.__init__(self, x, y, sma)

    '''
        Do nothing.
    '''
    def action(self):
        pass
