'''
Created on 9 fevr. 2014

@author: Alexandre Bonhomme
'''
from gui.FrameTk import FrameTk


class FrameWall(FrameTk):

    def __init__(self, height, width, box_size, title = "Wall", bg = None):
        FrameTk.__init__(self, height, width, box_size, title, bg)

    def _drawWall(self, x, y, color):
        self.canvas.create_rectangle(x, \
                                     y, \
                                     x + self.BOX_SIZE, \
                                     y + self.BOX_SIZE, \
                                     fill = color)
