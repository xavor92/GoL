"""
A Game of Live Implementation using TestDrivenDevelopment
"""

class GoL(object):
    def __init__(self, xdim, ydim):
        self._playfield = [[0 for _i in range(ydim)] for _i in range(xdim)]
        self._stepCount = 0
        
    def getStep(self):
        return self._stepCount
    
    def step(self):
        self._stepCount += 1