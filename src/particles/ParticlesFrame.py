'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL

from gui.FrameTk import FrameTk
from particles.agents.ParticleAgent import ParticleAgent
from particles.agents.WallAgent import WallAgent


class ParticlesFrame(FrameTk):

    def __init__(self, height, width, box_size, sma):
        FrameTk.__init__(self, height, width, box_size, title = 'Particles', bg = 'white')

        self.sma = sma

    def drawParticle(self, x, y, color = 'Blue'):
        self.canvas.create_oval(x, \
                                y, \
                                x + self.BOX_SIZE, \
                                y + self.BOX_SIZE, \
                                width = 0, \
                                fill = color)

    def drawWall(self, x, y, color = 'Black'):
        self.canvas.create_rectangle(x, \
                                     y, \
                                     x + self.BOX_SIZE, \
                                     y + self.BOX_SIZE, \
                                     fill = color)

    def _draw(self):
        title = "Particles - Tick " + str(self.sma.ticksCounter) + \
            "  Particles " + str(self.sma.particlesCounter)
        self.main.wm_title(title)

        self.canvas.delete(ALL)

        grid = self.sma.env.grid
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]
                if isinstance(element, ParticleAgent):
                    self.drawParticle(x * self.BOX_SIZE, y * self.BOX_SIZE, element.color)
                elif isinstance(element, WallAgent):
                    self.drawWall(x * self.BOX_SIZE, y * self.BOX_SIZE)

        self.canvas.update_idletasks()
