'''
Created on 17 janv. 2014

@author: Alexandre Bonhomme
'''
from random import shuffle

from core.Environnement import Environnement


'''
This class manager the turn to speak between agents
'''
class SMA(object):

    def __init__(self, cols, rows, logFilename = None, toric = False):
        self.agentsList = []
        self.ticksCounter = 0
        if logFilename:
            self.logFile = open(logFilename, 'w')

        self.env = Environnement(cols, rows, toric)
        self.stop = False

    '''
    Add an agent and update the grid
    '''
    def addAgent(self, agent):
        if self.env.add(agent.x, agent.y, agent):
            self.agentsList.append(agent)
            return True

        return False

    '''
    Remove an agent and update the grid
    '''
    def removeAgent(self, agent):
        a = self.env.remove(agent.x, agent.y)
        if a is not None:
            self.agentsList.remove(a)
            return True

        return False

    '''
    Remove all agents from the SMA and the list of all previous agents
    '''
    def removeAllAgent(self):
        agents = self.agentsList
        for a in self.agentsList:
            self.env.remove(a.x, a.y)

        self.agentsList = []

        return agents

    '''
    Call the action() function over each agents
    '''
    def runOnce(self):
        shuffle(self.agentsList)
        map(lambda agent: agent.action(), self.agentsList)
        self.ticksCounter += 1

    '''
    Stop the execution
    '''
    def stopExec(self):
        self.stop = True

    '''
    Logging functions
    '''
    def log(self, msg):
        if self.logFile:
            self.logFile.write(msg)
            self.logFile.flush()

    def logTo(self, fileID, msg):
        fileID.write(msg)
        fileID.flush()
