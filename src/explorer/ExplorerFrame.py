'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL

from core.agents.AgentWall import AgentWall
from explorer.agents.BuilderAgent import BuilderAgent
from explorer.agents.ExplorerAgent import ExplorerAgent
from gui.FrameWall import FrameWall


class ExplorerFrame(FrameWall):

    def __init__(self, height, width, box_size, sma):
        FrameWall.__init__(self, height, width, box_size, title = 'Explorer', bg = 'black')

        self.sma = sma

    def drawExplorer(self, x, y, color):
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
                    self.drawWall(x * self.BOX_SIZE, y * self.BOX_SIZE, color = 'brown')

                elif isinstance(element, BuilderAgent):
                    self.drawExplorer(x * self.BOX_SIZE, y * self.BOX_SIZE, 'white')

        self.canvas.update_idletasks()
