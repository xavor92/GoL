"""
A Game of Live Implementation using TestDrivenDevelopment
"""

class GoL(object):
    def __init__(self, xdim, ydim):
        self._playfield = [[0 for _i in range(ydim)] for _i in range(xdim)]
        self._stepCount = 0
        
    def __str__(self, *args, **kwargs):
        header = "Game of Life\nStep {0}\n".format(self._stepCount)
        representation = ""
        for row in self._playfield:
            for value in row:
                representation += str(value) + " "
            representation += '\n'
        return header + representation
        
    def getStep(self):
        return self._stepCount
    
    def step(self):
        self._stepCount += 1