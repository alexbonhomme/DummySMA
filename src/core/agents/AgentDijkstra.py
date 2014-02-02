'''
Created on 2 fevr. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentBase import AgentBase


class AgentDijkstra(AgentBase):

    def __init__(self, x, y, sma):
        AgentBase.__init__(self, x, y, sma)

        self.dijkstraGrid = None
        self._initDijkstraGrid()

    def action(self):
        print("I'm a Dijkstra agent!")

    '''
    Initialize the grid with None values
    '''
    def _initDijkstraGrid(self):
        self.dijkstraGrid = [[None for _ in xrange(self.sma.env.cols)] for _ in xrange(self.sma.env.rows)]

    '''
    Compute the Dijkstra around the current position
    '''
    def computeDijkstraGrid(self):
        self._initDijkstraGrid()
        self.dijkstraGrid[self.x][self.y] = 0
        listNeighbours = self._fillNeighbours(self.x, self.y, 1)

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
        rmax = i + 1 if i + 1 < self.sma.env.rows else i

        cmin = j - 1 if j - 1 >= 0 else 0
        cmax = j + 1 if j + 1 < self.sma.env.cols else j

        for x in xrange(rmin, rmax + 1):
            for y in xrange(cmin, cmax + 1):
                if self.dijkstraGrid[x][y] == None:
                    self.dijkstraGrid[x][y] = value
                    neighboursChange.append((x, y, value + 1))

        return neighboursChange
