'''
Created on 21 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL
from gui.FrameTk import FrameTk
from schelling.ColorAgent import ColorAgent


class SchellingFrame(FrameTk):

    def __init__(self, height, width, box_size, sma):
        FrameTk.__init__(self, height, width, box_size, title = 'Schelling model', bg = 'black')

        self.sma = sma

    def drawColorAgent(self, x, y, color):
        self.canvas.create_rectangle(x, \
                                     y, \
                                     x + self.BOX_SIZE, \
                                     y + self.BOX_SIZE, \
                                     fill = color)

    def _draw(self):
        title = "Schelling model - Tick " + str(self.sma.ticksCounter)
        self.main.wm_title(title)

        self.canvas.delete(ALL)

        grid = self.sma.env.grid
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]
                if isinstance(element, ColorAgent):
                    self.drawColorAgent(x * self.BOX_SIZE, y * self.BOX_SIZE, element.color)

        self.canvas.update_idletasks()
