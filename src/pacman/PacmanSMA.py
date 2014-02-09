'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''

from core.MazeSMA import MazeSMA
from pacman.agents.GhostAgent import GhostAgent
from pacman.agents.PacmanAgent import PacmanAgent


class PacmanSMA(MazeSMA):

    def __init__(self, cols, rows, logFilename = None):
        MazeSMA.__init__(self, cols, rows, logFilename)
        self._initDijkstraGrid()

    def initPacman(self):
        x, y = self.env.randomEmptyPosition()
        self.addAgent(PacmanAgent(x, y, self))

    def initGhosts(self, nGhosts = 4):
        if nGhosts < 1 or nGhosts > 4:
            raise "The number of ghosts should be include in [1, 4]"

        for i in xrange(nGhosts):
            x, y = self.env.randomEmptyPosition()
            self.addAgent(GhostAgent(x, y, self, i))

    '''
    Initialize the Dijkstra grid with Node values
    '''
    def _initDijkstraGrid(self):
        self.dijkstraGrid = [[None for _ in xrange(self.env.cols)] for _ in xrange(self.env.rows)]

    '''
    Compute the Dijkstra grid around the given position
    '''
    def _computeDijkstraGrid(self, x, y):
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

