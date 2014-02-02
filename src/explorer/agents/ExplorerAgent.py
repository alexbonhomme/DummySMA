'''
Created on 28 janv. 2014

@author: Alexandre Bonhomme
'''
from core.agents.AgentMovable import AgentMovable
from core.agents.AgentDijkstra import AgentDijkstra


class ExplorerAgent(AgentMovable, AgentDijkstra):

    def __init__(self, x, y, sma, color = 'light blue'):
        AgentMovable.__init__(self, x, y, sma) # could be ignored
        AgentDijkstra.__init__(self, x, y, sma)

        self.color = color

    def action(self):
        # compute the Dijkstra's grid
        self.computeDijkstraGrid()
