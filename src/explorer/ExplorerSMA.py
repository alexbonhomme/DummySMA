'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''

from core.MazeSMA import MazeSMA
from explorer.agents.ExplorerAgent import ExplorerAgent


class ExplorerSMA(MazeSMA):

    def __init__(self, cols, rows, logFilename = None):
        MazeSMA.__init__(self, cols, rows, logFilename)

    '''
    Place some ExplorerAgent in the Env
    '''
    def initExplorers(self, nExplorers):
        for _ in xrange(nExplorers):
            x, y = self.env.randomEmptyPosition()
            self.addAgent(ExplorerAgent(x, y, self))
