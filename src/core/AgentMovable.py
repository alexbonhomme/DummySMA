'''
Created on 20 janv. 2014

@author: Alexandre Bonhomme
'''
import random

from core.AgentBase import AgentBase

'''
A movable agent. This kind of agent can move on the Environnement grid
'''
class AgentMovable(AgentBase):

    def __init__(self, x, y, sma):
        AgentBase.__init__(self, x, y, sma)

    def action(self):
        print("I'm a movable agent!")

    '''
    Move to the given coordinates (and update the grid)
    '''
    def moveTo(self, x, y):
        env = self.sma.env

        # updating position
        if env.add(x, y, self):
            env.remove(self.x, self.y)
            self.x, self.y = x, y

            return True

        return False

    '''
    Move randomly around his place. (Moore neighborhood)
    '''
    def randomMove(self):
        movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        isMoved = False
        while not isMoved:
            x, y = random.choice(movements)
            movements.remove((x, y))
            if len(movements) == 0:
                return False

            try:
                isMoved = self.moveTo(self.x + x, self.y + y)
            except ValueError:
                isMoved = False
