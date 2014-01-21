'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
from core.SMA import SMA
from wator.agents.FishAgent import FishAgent
from wator.agents.SharkAgent import SharkAgent
import logging as log


class WatorSMA(SMA):

    def __init__(self, cols, rows, logFilename = None):
        SMA.__init__(self, cols, rows, logFilename)

        self.fishesCounter = 0
        self.sharksCounter = 0

        if hasattr(self, "logFile"):
            self.log("Ticks,Fishes,Sharks\n")

        # self.fishesFile = open("fishes_age.csv", 'w')
        # self.sharksFile = open("sharks_age.csv", 'w')

    '''
    Call the SMA.runOnce() function and perform some logging
    '''
    def runOnce(self):
        SMA.runOnce(self)
        if hasattr(self, "logFile"):
            stats = "{0},{1},{2}\n".format(self.ticksCounter, self.fishesCounter, self.sharksCounter)
            SMA.log(self, stats)

        log.info("Tick: %d - Fishes: %d - Sharks: %d", self.ticksCounter, self.fishesCounter, self.sharksCounter)

    '''
    Add some FishAgent to the agents list
    '''
    def initFishes(self, nFishes, breedingAge):
        self.fishesBreedingAge = breedingAge

        for _ in xrange(0, nFishes):
            x, y = self.env.randomEmptyPosition()
            self.addFishAgent(x, y, breedingAge)

    '''
    Add some SharkAgent to the agents list
    '''
    def initSharks(self, nSharks, breedingAge, starvationTime):
        self.sharksBreedingAge = breedingAge
        self.sharkStarvationTime = starvationTime

        for _ in xrange(0, nSharks):
            x, y = self.env.randomEmptyPosition()
            self.addSharkAgent(x, y, breedingAge, starvationTime)

    '''
    Add a FishAgent to the agents list and increase the fishes counter
    '''
    def addFishAgent(self, x, y, breedingAge):
        if self.addAgent(FishAgent(x, y, self, breedingAge)):
            self.fishesCounter += 1

    '''
    Remove a FishAgent to the agents list and decrease the fishes counter
    '''
    def removeFishAgent(self, agent):
        if self.removeAgent(agent):
            self.fishesCounter -= 1
            # self.logTo(self.fishesFile, str(agent.age) + "\n")

    '''
    Add a SharkAgent to the agents list and increase the sharks counter
    '''
    def addSharkAgent(self, x, y, breedingAge, starvationTime):
        if self.addAgent(SharkAgent(x, y, self, breedingAge, starvationTime)):
            self.sharksCounter += 1

    '''
    Remove a SharkAgent to the agents list and decrease the sharks counter
    '''
    def removeSharkAgent(self, agent):
        if self.removeAgent(agent):
            self.sharksCounter -= 1
            # self.logTo(self.sharksFile, str(agent.age) + "\n")

