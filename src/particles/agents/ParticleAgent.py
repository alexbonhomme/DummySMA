'''
Created on 20 janv. 2014

@author: Alexandre Bonhomme
'''
from core.AgentMovable import AgentMovable
from particles.agents.WallAgent import WallAgent
import logging as log


class ParticleAgent(AgentMovable):

    def __init__(self, x, y, sma, direction, color = "blue"):
        AgentMovable.__init__(self, x, y, sma)

        self.xDir, self.yDir = direction
        self.color = color

    def action(self):
        x, y = self.x + self.xDir, self.y + self.yDir

        # easy movement
        if self.moveTo(x, y):
            return

        # else, we deal with the rebound
        self._reboundOn(x, y)

    def _reboundOn(self, x, y):
        agent = self.sma.env.get(x, y)
        if isinstance(agent, WallAgent):
            wall = agent

            # vertical walls
            if wall.x == 0 or wall.x == self.sma.env.rows - 1:
                self.xDir = -self.xDir

            # horizontal walls
            if wall.y == 0 or wall.y == self.sma.env.cols - 1:
                self.yDir = -self.yDir

        elif isinstance(agent, ParticleAgent):
            particle = agent

            '''
             Switch direction
            '''
            tmpDir = (self.xDir, self.yDir)
            self.xDir, self.yDir = particle.xDir, particle.yDir
            particle.xDir, particle.yDir = tmpDir


        # rebounding
        x, y = self.x + self.xDir, self.y + self.yDir
        if not self.moveTo(x, y):
            log.debug('Particles stuck! x:%d y:%d xDir:%d yDir:%d', self.x, self.y, self.xDir, self.yDir)
            # self._reboundOn(x, y)
        else:
            self.x, self.y = x, y
