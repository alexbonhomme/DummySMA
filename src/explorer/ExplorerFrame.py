'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL

from gui.FrameTk import FrameTk
from explorer.agents.ExplorerAgent import ExplorerAgent
from core.agents.AgentWall import AgentWall
import logging as log

class ExplorerFrame(FrameTk):

    def __init__(self, height, width, box_size, sma):
        FrameTk.__init__(self, height, width, box_size, title = 'Explorer', bg = 'black')

        self.sma = sma

    def drawExplorer(self, x, y, color):
        self.canvas.create_rectangle(x, \
                                     y, \
                                     x + self.BOX_SIZE, \
                                     y + self.BOX_SIZE, \
                                     fill = color)

    def drawWall(self, x, y, color = 'brown'):
        self.canvas.create_rectangle(x, \
                                     y, \
                                     x + self.BOX_SIZE, \
                                     y + self.BOX_SIZE, \
                                     fill = color)

    def drawDijkstraGrid(self, grid):
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]

                if element is not None:
                    self.drawText(x * self.BOX_SIZE, y * self.BOX_SIZE, element, color = 'white')

    def _draw(self):
        title = "Explorer - Tick " + str(self.sma.ticksCounter)
        self.main.wm_title(title)

        self.canvas.delete(ALL)

        grid = self.sma.env.grid
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]
                if isinstance(element, ExplorerAgent):
                    self.drawExplorer(x * self.BOX_SIZE, y * self.BOX_SIZE, element.color)
                    self.drawDijkstraGrid(element.dijkstraGrid)

                elif isinstance(element, AgentWall):
                    self.drawWall(x * self.BOX_SIZE, y * self.BOX_SIZE)

        self.canvas.update_idletasks()
