'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
from Tkinter import ALL
from PIL import Image, ImageTk


from gui.FrameTk import FrameTk
from wator.agents.FishAgent import FishAgent
from wator.agents.SharkAgent import SharkAgent


class WatorFrame(FrameTk):

    def __init__(self, height, width, box_size, sma):
        FrameTk.__init__(self, height, width, box_size, title = "Wator", bg = "light blue")

        image = Image.open("../resources/shark_nemo.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_SHARK = ImageTk.PhotoImage(image)

        image = Image.open("../resources/fish_nemo.png")
        image = image.resize((self.BOX_SIZE, self.BOX_SIZE), Image.ANTIALIAS)
        self.IMG_FISH = ImageTk.PhotoImage(image)

        self.sma = sma

    '''
    Draw a fish image over the canvas
    '''
    def drawFish(self, x, y):
        self.drawTkImage(x, y, self.IMG_FISH)

    '''
    Draw a shark image over the canvas
    '''
    def drawShark(self, x, y):
        self.drawTkImage(x, y, self.IMG_SHARK)

    '''
    Draw all agents in the grid over the canvas
    '''
    def _draw(self):
        title = "Wator - Tick " + str(self.sma.ticksCounter) + \
            "  Fishes " + str(self.sma.fishesCounter) + \
            "  Sharks " + str(self.sma.sharksCounter)
        self.main.wm_title(title)

        self.canvas.delete(ALL)

        grid = self.sma.env.grid
        rows, cols = self.sma.env.rows, self.sma.env.cols
        for x in xrange(0, rows):
            for y in xrange(0, cols):
                element = grid[x][y]

                if isinstance(element, FishAgent):
                    self.drawFish(x * self.BOX_SIZE , y * self.BOX_SIZE)
                elif isinstance(element, SharkAgent):
                    self.drawShark(x * self.BOX_SIZE, y * self.BOX_SIZE)

        self.canvas.update_idletasks()
