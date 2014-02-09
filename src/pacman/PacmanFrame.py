'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL

from PIL import ImageTk, Image

from core.agents.AgentWall import AgentWall
from gui.FrameWall import FrameWall
from pacman.agents.GhostAgent import GhostAgent
from pacman.agents.PacmanAgent import PacmanAgent


class PacmanFrame(FrameWall):

    def __init__(self, height, width, box_size, sma, dijkstra = False):
        FrameWall.__init__(self, height, width, box_size, title = 'Pacman', bg = 'black')

        image = Image.open("../resources/pacman.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_PACMAN = ImageTk.PhotoImage(image)

        self.IMG_GHOSTS = []
        image = Image.open("../resources/ghost_1.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_GHOSTS.append(ImageTk.PhotoImage(image))

        image = Image.open("../resources/ghost_2.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_GHOSTS.append(ImageTk.PhotoImage(image))

        image = Image.open("../resources/ghost_3.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_GHOSTS.append(ImageTk.PhotoImage(image))

        image = Image.open("../resources/ghost_4.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_GHOSTS.append(ImageTk.PhotoImage(image))

        self.sma = sma
        self.dijkstra = dijkstra

    def _drawPacman(self, x, y):
        self.drawTkImage(x, y, self.IMG_PACMAN)

    def _drawGhost(self, x, y, ident):
        if ident < 0 or ident >= 4:
            raise ValueError("ident should be >= 0 and < 4")

        self.drawTkImage(x, y, self.IMG_GHOSTS[ident])

    def _draw(self):
        title = "Pacman - Tick " + str(self.sma.ticksCounter)
        self.main.wm_title(title)

        self.canvas.delete(ALL)

        grid = self.sma.env.grid
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]
                if isinstance(element, AgentWall):
                    self._drawWall(x * self.BOX_SIZE, y * self.BOX_SIZE, color = 'purple')

                elif isinstance(element, GhostAgent):
                    self._drawGhost(x * self.BOX_SIZE, y * self.BOX_SIZE, element.id)

                elif isinstance(element, PacmanAgent):
                    self._drawPacman(x * self.BOX_SIZE, y * self.BOX_SIZE)

                elif self.dijkstra:
                    self.drawText(x * self.BOX_SIZE, y * self.BOX_SIZE, self.sma.dijkstraGrid[x][y], 'white')

        self.canvas.update_idletasks()
