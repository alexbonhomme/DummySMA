'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''

from core.SMA import SMA
from pacman.agents.WallAgent import WallAgent
from pacman.agents.PacmanAgent import PacmanAgent

class PacmanSMA(SMA):

    def __init__(self, cols, rows, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)
        self.computeDijkstraGrid()
    '''
    Place walls into the grid
    '''

    def computeDijkstraGrid(self):
        self.dijkstraGrid = [[None for _ in xrange(self.env.cols)] for _ in xrange(self.env.rows)]

    def initWalls(self):
        # TODO
        for x in xrange(self.env.rows):
            self.addAgent(WallAgent(x, 0, self))
            self.addAgent(WallAgent(x, self.env.cols - 1, self))

        for y in xrange(self.env.cols):
            self.addAgent(WallAgent(0, y, self))
            self.addAgent(WallAgent(self.env.rows - 1, y, self))

    def initPacman(self):
        x, y = self.env.randomEmptyPosition()
        self.addAgent(PacmanAgent(x, y, self))

