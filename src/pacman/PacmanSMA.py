'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''

from core.SMA import SMA
from core.agents.AgentWall import AgentWall
from pacman.agents.GhostAgent import GhostAgent
from pacman.agents.PacmanAgent import PacmanAgent


class PacmanSMA(SMA):

    def __init__(self, cols, rows, nbPhantom, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)
        self._initDijkstraGrid()
        if nbPhantom < 0 and nbPhantom > 4:
            pass
        
        self.nbPhantom = nbPhantom
    '''
    Place walls into the grid
    '''

    def _initDijkstraGrid(self):
        self.dijkstraGrid = [[None for _ in xrange(self.env.cols)] for _ in xrange(self.env.rows)]


    def computeDijkstraGrid(self, x, y):
        self._initDijkstraGrid()
        self.dijkstraGrid[x][y] = 0
        listNeighbours = self._fillNeighbours(x, y, 1)

        for position in listNeighbours:
            positionChild = self._fillNeighbours(position[0], position[1], position[2])
            listNeighbours.extend(positionChild)

    '''
    Fill the empty neighbours of x,y with value param
    Return list of position of neighbours which has change
    '''
    def _fillNeighbours(self, x, y, value):
        i, j = x, y
        neighboursChange = []

        rmin = i - 1 if i - 1 >= 0 else 0
        rmax = i + 1 if i + 1 < self.env.rows else i

        cmin = j - 1 if j - 1 >= 0 else 0
        cmax = j + 1 if j + 1 < self.env.cols else j

        for x in xrange(rmin, rmax + 1):
            for y in xrange(cmin, cmax + 1):
                if self.dijkstraGrid[x][y] == None:
                    self.dijkstraGrid[x][y] = value
                    neighboursChange.append((x, y, value + 1))

        return neighboursChange


    def initWalls(self):
        # TODO
        for x in xrange(self.env.rows):
            self.addAgent(AgentWall(x, 0, self))
            self.addAgent(AgentWall(x, self.env.cols - 1, self))

        for y in xrange(self.env.cols):
            self.addAgent(AgentWall(0, y, self))
            self.addAgent(AgentWall(self.env.rows - 1, y, self))

    def initPacman(self):
        x, y = self.env.randomEmptyPosition()
        self.addAgent(PacmanAgent(x, y, self))

    def initGhosts(self):
        for i in xrange(self.nbPhantom):
            x, y = self.env.randomEmptyPosition()
            self.addAgent(GhostAgent(x, y, self, i))
