'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentMovable import AgentMovable
from core.agents.AgentDijkstra import AgentDijkstra
import logging as log


class ExplorerAgent(AgentMovable, AgentDijkstra):

    def __init__(self, x, y, sma, color = 'light blue'):
        AgentMovable.__init__(self, x, y, sma) # could be ignored
        AgentDijkstra.__init__(self, x, y, sma)

        self.color = color
        self.map = [[False for _ in xrange(self.sma.env.cols)] for _ in xrange(self.sma.env.rows)]

    def action(self):
        # compute the Dijkstra's grid
        unknownCells = self._computeDijkstraGrid()
        if not unknownCells:
            log.info('I finished my exploration !')
            return

        # Looking for the closest unknown cell
        minVal = unknownCells[0][2]
        nextX, nextY = unknownCells[0][0], unknownCells[0][1]
        for x, y, value in unknownCells:
            if value < minVal:
                nextX, nextY = x, y

        # Visit the cell
        self.moveTo(nextX, nextY)
        self.map[nextX][nextY] = True # Cell visited

    '''
    Override from AgentDijkstra
    Stop compute when the cell is unknown or when this is wall
    '''
    def _computeDijkstraGrid(self):
        self._initDijkstraGrid()
        self.dijkstraGrid[self.x][self.y] = 0
        listNeighbours = self._fillNeighbours(self.x, self.y, 1)

        unknownCells = []
        for position in listNeighbours:
            x, y, value = position[0], position[1], position[2]
            if not self.map[x][y]:
                unknownCells.append(position)
                continue

            positionChild = self._fillNeighbours(x, y, value)
            listNeighbours.extend(positionChild)

        return unknownCells
