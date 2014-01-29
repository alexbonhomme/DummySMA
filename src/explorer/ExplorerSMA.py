'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''

from core.SMA import SMA
from core.agents.WallAgent import WallAgent

class ExplorerSMA(SMA):

    def __init__(self, cols, rows, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)

    def initWalls(self):
        pass

    def initExplorers(self, nExplorers):
        pass
