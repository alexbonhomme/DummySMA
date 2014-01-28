'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.AgentMovable import AgentMovable
from explorer.agents.WallAgent import WallAgent


class MazeBuilderAgent(AgentMovable):

    def __init__(self, x, y, sma):
        AgentMovable.__init__(self, x, y, sma)

        self.visitedCase = []

    def action(self):
        pass

    def _initGridWalls(self):
        '''
        We first place the external walls
        '''
        for x in xrange(self.env.rows):
            self.addAgent(WallAgent(x, 0, self.sma))
            self.addAgent(WallAgent(x, self.env.cols - 1, self.sma))

        for y in xrange(self.env.cols):
            self.addAgent(WallAgent(0, y, self.sma))
            self.addAgent(WallAgent(self.env.rows - 1, y, self.sma))

        '''
        Now we build the grid walls
        '''
        for x in xrange(2, self.env.rows - 2):
            for y in xrange(2, self.env.cols - 2):
                self.addAgent(WallAgent(x, y, self.sma))
