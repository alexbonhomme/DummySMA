'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
import random
import logging as log
from core.agents.AgentMovable import AgentMovable
from pacman.agents.PacmanAgent import PacmanAgent

class GhostAgent(AgentMovable):

    def __init__(self, x, y, sma, ident):
        AgentMovable.__init__(self, x, y, sma)

        # ID of the ghost (to display specific Image)
        self.id = ident

    def action(self):
        if self.isPacmanNeighbour():
            pass
        
        position = self.bestMove()
        if not position:
            log.debug('Phantom ever on the best place x: %d y: %d', self.x, self.y)
            return
        
        x, y = position
        self.moveTo(x, y)
    
    def isPacmanNeighbour(self):
        neighboursAgents = self.sma.env.neighboursAgentsOf(self.x, self.y)
        for neighbour in neighboursAgents:
            if isinstance(neighbour, PacmanAgent):
                self.stop()
                return True
            
        return False
    
    def stop(self):
        if self.sma.stopEat:
            self.sma.stop = True 

        '''
        Return neighbour position that have the smallest value (dijkstra)
        ''' 
    def bestMove(self):
        neighbours = self.sma.env.neighboursEmptyOf(self.x, self.y)
        if not neighbours:
            return
        
        neighboursSMA = []
        for neighbour in neighbours:
            x, y = neighbour
            neighboursSMA.append([self.sma.dijkstraGrid[x][y], x, y])
        
        neighboursSMA.sort()
        
        '''
        Verify if the phantom is ever on the best value
        '''
        if neighboursSMA[0][0] >= self.sma.dijkstraGrid[self.x][self.y]:
            return
        
        '''
        Random : only the three first elements of neighboursSMA may have the smallest value
        '''
        neighboursResult = [neighboursSMA[0]]
        for x in range(1,3):
            if x >= len(neighboursSMA):
                break
            
            if neighboursSMA[x][0] == neighboursSMA[0][0]:
                neighboursResult.append(neighboursSMA[x])
        
        position = random.choice(neighboursResult)
        x, y = position[1:3]
        
        return (x, y)
            