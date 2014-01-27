'''
Created on 21 janv. 2014

@author: Alexandre Bonhomme
'''
from core.SMA import SMA
from schelling.ColorAgent import ColorAgent

class SchellingSMA(SMA):

    def __init__(self, cols, rows, satisfactionThreshold, toric = False, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename = logFilename, toric = toric)

        self.satisfactionThreshold = satisfactionThreshold

        if hasattr(self, "logFile"):
            self.log("Average global satisfaction, Unsatisfaction\n")

    def runOnce(self):
        SMA.runOnce(self)

        if hasattr(self, "logFile"):
            stats = "{0},{1}\n".format(self.computeGlobalSatisfaction(), self.computeUnsatisfaction())
            SMA.log(self, stats)

    def initRedAgents(self, nRedAgents):
        self._initColorAgents(nRedAgents, 'light coral')

    def initBlueAgents(self, nRedAgents):
        self._initColorAgents(nRedAgents, 'light blue')

    def _initColorAgents(self, nColorAgent, color):
        for _ in xrange(0, nColorAgent):
            x, y = self.env.randomEmptyPosition()
            self.addAgent(ColorAgent(x, y, self, color, self.satisfactionThreshold))

    '''
    Return the average satisfaction of agents
    '''
    def computeGlobalSatisfaction(self):
        satisfations = 0.0

        if len(self.agentsList) <= 0:
            raise ValueError("Empty agents list")

        for agent in self.agentsList:
            satisfations += agent.satisfaction

        return satisfations / len(self.agentsList)

    '''
    Return the percent of agents who aren't satisfied
    '''
    def computeUnsatisfaction(self):
        unsatisfaction = 0.0

        if len(self.agentsList) <= 0:
            raise ValueError("Empty agents list")

        for agent in self.agentsList:
            if agent.satisfaction < self.satisfactionThreshold:
                unsatisfaction += 1

        return unsatisfaction / len(self.agentsList)
