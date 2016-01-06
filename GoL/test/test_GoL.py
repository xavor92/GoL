"""
Tests for Conways Game of Life

"""

import unittest
from GoL import GoL

class InitTest(unittest.TestCase):
    def test_WeCanInitializeAGoL(self):
        ''' We can initialize a GoL with a given Size
        '''
        self.GoL = GoL(rows = 10, columns = 10)
        self.assertTrue(isinstance(self.GoL, GoL))
        
    def test_GoLHasCorrectDimensions(self):
        self.GoL = GoL(rows = 10, columns = 10)
        self.assertTrue( len(self.GoL._playfield) == 10)
        for row in self.GoL._playfield:
            self.assertTrue(len(row) == 10)
        
        
class FunctionTests(unittest.TestCase):
    def setUp(self):
        super(FunctionTests, self).setUp()
        self.GoL = GoL(10, 10)
    
    def test_WeCanPrintTheGame(self):
        printtext = str(self.GoL)
        empty_field = ". . . . . . . . . . \n" * 10
        self.assertIn('Game of Life', printtext)
        self.assertIn('Step', printtext)
        self.assertIn(empty_field, printtext)
        self.GoL.setField(row = 0, column = 0, value = 1)
        printtext = str(self.GoL)
        self.assertIn('X', printtext)
        
    def test_WeCanStepTheGoL(self):
        self.GoL.step()
        
    def test_StepCountIncreases(self):
        StepCount = self.GoL.getStep()
        self.GoL.step()
        self.assertTrue(StepCount + 1 == self.GoL.getStep())
        
    def test_WeCanSetGetFields(self):
        self.GoL.setField(row = 2, column = 0, value = 1)
        self.assertTrue(self.GoL.getField(2, 0) == 1)
        
    def test_WeCanGetLiveNeighbours(self):
        self.GoL.setField(row = 0, column = 0, value = 1)
        self.GoL.setField(row = 1, column = 0, value = 1)
        self.GoL.setField(row = 0, column = 1, value = 1)
        self.assertEqual(self.GoL.getLiveNeighbours(0,0), 2)
        self.assertEqual(self.GoL.getLiveNeighbours(1,1), 3)
        self.assertEqual(self.GoL.getLiveNeighbours(0,2), 1)
        self.assertEqual(self.GoL.getLiveNeighbours(5,5), 0)
        self.assertEqual(self.GoL.getLiveNeighbours(0,9), 0)
        
    def test_WeCanCountLiveCells(self):
        self.GoL.setField(row = 0, column = 0, value = 1)
        self.assertEqual(self.GoL.getLiveCells(), 1)
        self.GoL.setField(row = 1, column = 0, value = 1)
        self.assertEqual(self.GoL.getLiveCells(), 2)
        self.GoL.setField(row = 0, column = 1, value = 1)
        self.assertEqual(self.GoL.getLiveCells(), 3)
        
    def test_singleCellDiesInOneStep(self):
        self.GoL.setField(row = 0, column = 0, value = 1)
        self.GoL.step()
        self.assertEqual(self.GoL.getLiveCells(), 0)
        self.GoL.setField(row = 0, column = 0, value = 1)
        self.GoL.setField(row = 5, column = 5, value = 1)
        self.GoL.step()
        self.assertEqual(self.GoL.getLiveCells(), 0)
        
    def test_SquareStaysAlive(self):
        self.GoL.setField(row = 0, column = 0, value = 1)
        self.GoL.setField(row = 1, column = 0, value = 1)
        self.GoL.setField(row = 0, column = 1, value = 1)
        self.GoL.setField(row = 1, column = 1, value = 1)
        self.assertEqual(self.GoL.getLiveCells(), 4)
        self.GoL.step()
        self.assertEqual(self.GoL.getLiveCells(), 4)
        self.assertTrue(self.GoL.getField(0, 0) == 1)
        self.assertTrue(self.GoL.getField(1, 0) == 1)
        self.assertTrue(self.GoL.getField(0, 1) == 1)
        self.assertTrue(self.GoL.getField(1, 1) == 1)
        
        