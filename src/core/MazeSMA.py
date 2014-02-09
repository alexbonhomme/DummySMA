'''
Created on 9 fevr. 2014

@author: Alexandre Bonhomme
'''
import random

from core.SMA import SMA
from core.agents.AgentWall import AgentWall
from explorer.agents.BuilderAgent import BuilderAgent


class MazeSMA(SMA):

    def __init__(self, cols, rows, logFilename, toric = False):
        SMA.__init__(self, cols, rows, logFilename, toric)

    '''
    Init builder agents to mine the maze and filled the grid with walls
    and the number of step they has to perform
    '''
    def initBuilder(self, nBuilder, nSteps):
        self.env.grid = [[AgentWall(self.env.rows, self.env.cols, self)
                            for _ in xrange(self.env.cols)]
                                for _ in xrange(self.env.rows)]

        for _ in xrange(nBuilder):
            x, y = random.randrange(self.env.rows), random.randrange(self.env.cols)

            # remove wall
            self.env.remove(x, y)

            # adding agent
            self.addAgent(BuilderAgent(x, y, self, nSteps))

    '''
    Places some obstacles 
    '''
    def initWalls(self, minWallSize, maxWallSize, nWalls):
        # Horizontal walls
        for x in xrange(self.env.rows):
            self.addAgent(AgentWall(x, 0, self))
            self.addAgent(AgentWall(x, self.env.cols - 1, self))

        # Vertical walls
        for y in xrange(self.env.cols):
            self.addAgent(AgentWall(0, y, self))
            self.addAgent(AgentWall(self.env.rows - 1, y, self))

        '''
        Put some random shapes
        '''
        for _ in xrange(nWalls):
            # take a random position
            x, y = self.env.randomEmptyPosition()
            self.addAgent(AgentWall(x, y, self))

            # random size
            size = random.randint(minWallSize, maxWallSize)
            for _ in xrange(size):
                # random free neighbours (vonNeumann)

                n = self._vonNeumannEmptyNeighbours(x, y)
                if not n:
                    continue

                x, y = random.choice(n)
                self.addAgent(AgentWall(x, y, self))


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
