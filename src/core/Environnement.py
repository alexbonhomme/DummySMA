#!/usr/bin/env python2
'''
Created on 17 janv. 2014

@author: Alexandre Bonhomme
'''
import random


class Environnement(object):

    def __init__(self, cols, rows):
        self.rows, self.cols = rows, cols
        self.grid = [[None for _ in xrange(cols)] for _ in xrange(rows)]

    def add(self, x, y, agent):
        if x < 0 or x >= self.rows:
            raise ValueError("x should be greater or equal to 0 and inferior to rows")
        if y < 0 or y >= self.cols:
            raise ValueError("y should be greater or equal to 0 and inferior to cols")

        if not self.isEmpty(x, y):
            return False

        self.grid[x][y] = agent

        return True

    def remove(self, x, y):
        if x < 0 or x >= self.rows:
            raise ValueError("x should be greater or equal to 0 and inferior to rows")
        if y < 0 or y >= self.cols:
            raise ValueError("y should be greater or equal to 0 and inferior to cols")

        agent = self.grid[x][y]
        self.grid[x][y] = None

        return agent

    def get(self, x, y):
        if x < 0 or x >= self.rows:
            raise ValueError("x should be greater or equal to 0 and inferior to rows")
        if y < 0 or y >= self.cols:
            raise ValueError("y should be greater or equal to 0 and inferior to cols")

        return self.grid[x][y]

    def neighboursAgentsOf(self, x, y):
        '''
        Add the agent reference of direct neighbours 
        '''
        def listAgentsNeighbours(x, y, neighbours):
            if not self.isEmpty(x, y):
                neighbours.append(self.grid[x][y])

        neighbours = []
        self._foreachNeighboursOf(x, y, listAgentsNeighbours, neighbours)

        return neighbours

    def neighboursEmptyOf(self, x, y):
        '''
        Just add the neighbor location it's empty
        '''
        def listEmptyNeighbours(x, y, neighbours):
            if self.isEmpty(x, y):
                neighbours.append((x, y))

        neighbours = []
        self._foreachNeighboursOf(x, y, listEmptyNeighbours, neighbours)

        return neighbours

    '''
    Apply the given function for each neighbours
    The given function has to take at least 2 arguments : x and y
    '''
    def _foreachNeighboursOf(self, x, y, func, *args):
        i, j = x, y

        rmin = i - 1 if i - 1 >= 0 else 0
        rmax = i + 1 if i + 1 < self.rows else i

        cmin = j - 1 if j - 1 >= 0 else 0
        cmax = j + 1 if j + 1 < self.cols else j

        for x in xrange(rmin, rmax + 1):
            for y in xrange(cmin, cmax + 1):
                if i == x and j == y:
                    continue

                # apply function
                func(x, y, *args)

    def isEmpty(self, x, y):
        return self.grid[x][y] is None

    def randomEmptyPosition(self):
        isFree = False
        while not isFree:
            x = random.randrange(self.rows)
            y = random.randrange(self.cols)

            if self.isEmpty(x, y):
                return x, y
