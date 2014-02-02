'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''

import random

from core.SMA import SMA
from core.agents.WallAgent import WallAgent
from explorer.agents.ExplorerAgent import ExplorerAgent
import logging as log


class ExplorerSMA(SMA):

    def __init__(self, cols, rows, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)

    '''
        Places some obstacles 
    '''
    def initWalls(self, minWallSize, maxWallSize, nWalls):
        # Horizontal walls
        for x in xrange(self.env.rows):
            self.addAgent(WallAgent(x, 0, self))
            self.addAgent(WallAgent(x, self.env.cols - 1, self))

        # Vertical walls
        for y in xrange(self.env.cols):
            self.addAgent(WallAgent(0, y, self))
            self.addAgent(WallAgent(self.env.rows - 1, y, self))

        '''
        Put some random shapes
        '''
        for _ in xrange(nWalls):
            # take a random position
            x, y = self.env.randomEmptyPosition()
            self.addAgent(WallAgent(x, y, self))

            # random size
            size = random.randint(minWallSize, maxWallSize)
            for _ in xrange(size):
                # random free neighbours (vonNeumann)

                n = self._vonNeumannEmptyNeighbours(x, y)
                if not n:
                    continue

                x, y = random.choice(n)
                self.addAgent(WallAgent(x, y, self))


    '''
    Return the coordinate of free neighbours (using VonNeumann)
    '''
    def _vonNeumannEmptyNeighbours(self, x, y):
        neighbours = []

        if x - 1 >= 0 and self.env.isEmpty(x - 1, y):
            neighbours.append([x - 1, y])
        if x + 1 < self.env.rows and self.env.isEmpty(x + 1, y):
            neighbours.append([x + 1, y])
        if y - 1 >= 0 and self.env.isEmpty(x, y - 1):
            neighbours.append([x, y - 1])
        if y + 1 < self.env.cols and self.env.isEmpty(x, y + 1):
            neighbours.append([x, y + 1])

        return neighbours

    '''
    Place some ExplorerAgent in the Env
    '''
    def initExplorers(self, nExplorers):
        for _ in xrange(nExplorers):
            x, y = self.env.randomEmptyPosition()
            self.addAgent(ExplorerAgent(x, y, self))
