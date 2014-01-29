'''
Created on 17 janv. 2014

@author: Alexandre Bonhomme
'''

'''
Basic agent which basically do : nothing
'''
class AgentBase(object):

    def __init__(self, x, y, sma):
        self.x = x
        self.y = y
        self.sma = sma
        self.age = 0

    def action(self):
        print("I'm a basic agent!")
