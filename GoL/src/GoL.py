"""
A Game of Live Implementation using TestDrivenDevelopment
"""

class GoL(object):
    def __init__(self, rows, columns):
        self._playfield = [[0 for _i in range(columns)] for _i in range(rows)]
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
        
    def setField(self, row, column, value):
        self._playfield[row][column] = value
        
    def getField(self, row, column):
        return self._playfield[row][column]