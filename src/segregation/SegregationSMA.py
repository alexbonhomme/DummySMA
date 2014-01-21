'''
Created on 21 janv. 2014

@author: Alexandre Bonhomme
'''
from core.SMA import SMA
from segregation.ColorAgent import ColorAgent


class SegregationSMA(SMA):

    def __init__(self, cols, rows, satisfactionThreshold, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)

        self.satisfactionThreshold = satisfactionThreshold

    def initRedAgents(self, nRedAgents):
        self._initColorAgents(nRedAgents, 'light coral')

    def initBlueAgents(self, nRedAgents):
        self._initColorAgents(nRedAgents, 'light blue')

    def _initColorAgents(self, nColorAgent, color):
        for _ in xrange(0, nColorAgent):
            x, y = self.env.randomEmptyPosition()
            self.addAgent(ColorAgent(x, y, self, color, self.satisfactionThreshold))
