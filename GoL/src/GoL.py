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
    
    def getDimension(self):
        return (len(self._playfield), len(self._playfield[0]))
    
    def step(self):
        self._stepCount += 1
        
    def setField(self, row, column, value):
        self._playfield[row][column] = value
        
    def getField(self, row, column):
        return self._playfield[row][column]
    
    def getLiveNeighbours(self, row, column):
        return self._countNeighbours()[row][column]
    
    def getLiveCells(self):
        '''
        count live cells
        '''
        count = 0
        for row in self._playfield:
            for value in row:
                if value:
                    count += 1
        return count
        
    def _countNeighbours(self):
        '''
        count neighbours of cells and create map
        
        step through all fields of _playfield, if field contains a 1, increment 
        values in the surrounding fields of the neighbourmap
        '''
        rowcount, columncount = self.getDimension()
        neighbours = [[0 for _i in range(columncount)] for _i in range(rowcount)]
        for row in range(rowcount):
            for column in range(columncount):
                if self.getField(row, column):
                    # increase neighbours in upper row
                    if row - 1 >= 0:
                        if column - 1 >= 0:
                            neighbours[row-1][column-1] += 1
                        neighbours[row-1][column] += 1
                        if column + 1 <= columncount:
                            neighbours[row-1][column +1] += 1
                    # increase neighbours in same row
                    if column - 1 >= 0:
                        neighbours[row][column-1] += 1
                    if column + 1 <= columncount:
                        neighbours[row][column + 1] += 1
                    # increase neighbours in lower row
                    if row + 1 <= rowcount:
                        if column - 1 >= 0:
                            neighbours[row+1][column-1] += 1
                        neighbours[row+1][column] += 1
                        if column + 1 <= columncount:
                            neighbours[row+1][column +1] += 1
        return neighbours
                