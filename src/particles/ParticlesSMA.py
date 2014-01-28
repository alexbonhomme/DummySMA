'''
Created on 20 janv. 2014

@author: Alexandre Bonhomme
'''
import random

from core.SMA import SMA
from particles.agents.ParticleAgent import ParticleAgent
from particles.agents.WallAgent import WallAgent


class PacmanSMA(SMA):

    def __init__(self, cols, rows, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)

        self.particlesCounter = 0

    '''
    Place walls into the grid
    Has to be done before called initParticles
    '''
    def initWalls(self):
        for x in xrange(self.env.rows):
            self.addAgent(WallAgent(x, 0, self))
            self.addAgent(WallAgent(x, self.env.cols - 1, self))

        for y in xrange(self.env.cols):
            self.addAgent(WallAgent(0, y, self))
            self.addAgent(WallAgent(self.env.rows - 1, y, self))

    def initParticles(self, nParticles):
        COLORS = ["light blue", "light coral", "light cyan", "light goldenrod",
                  "light goldenrod yellow", "light gray", "light green",
                  "light grey", "light pink", "light salmon", "light sea green",
                  "light sky blue", "light slate blue", "light slate gray",
                  "light slate grey", "light steel blue", "light yellow"]

        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for _ in xrange(0, nParticles):
            color = random.choice(COLORS)
            x, y = self.env.randomEmptyPosition()
            direction = random.choice(DIRECTIONS)
            if self.addAgent(ParticleAgent(x, y, self, direction, color)):
                self.particlesCounter += 1
