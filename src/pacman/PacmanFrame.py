'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL

from gui.FrameTk import FrameTk
from pacman.agents.PacmanAgent import PacmanAgent
from particles.agents.WallAgent import WallAgent


class PacmanFrame(FrameTk):

    def __init__(self, height, width, box_size, sma):
        FrameTk.__init__(self, height, width, box_size, title = 'Pacman', bg = 'black')

        self.sma = sma

    def drawPacman(self, x, y):
        # TODO
        pass

    def drawWall(self, x, y, color = 'purple'):
        self.canvas.create_rectangle(x, \
                                     y, \
                                     x + self.BOX_SIZE, \
                                     y + self.BOX_SIZE, \
                                     fill = color)

    def _draw(self):
        title = "Pacman - Tick " + str(self.sma.ticksCounter)
        self.main.wm_title(title)

        self.canvas.delete(ALL)

        grid = self.sma.env.grid
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]
                if isinstance(element, PacmanAgent):
                    self.drawPacman(x * self.BOX_SIZE, y * self.BOX_SIZE)
                elif isinstance(element, WallAgent):
                    self.drawWall(x * self.BOX_SIZE, y * self.BOX_SIZE)

        self.canvas.update_idletasks()
