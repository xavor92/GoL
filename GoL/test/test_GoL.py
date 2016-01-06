"""
Tests for Conways Game of Life

"""

import unittest
from GoL import GoL

class InitTest(unittest.TestCase):
    def test_WeCanInitializeAGoL(self):
        ''' We can initialize a GoL with a given Size
        '''
        self.GoL = GoL(xdim = 10, ydim = 10)
        self.assertTrue(isinstance(self.GoL, GoL))
        
    def test_GoLHasCorrectDimensions(self):
        self.GoL = GoL(xdim = 10, ydim = 10)
        self.assertTrue( len(self.GoL._playfield) == 10)
        for row in self.GoL._playfield:
            self.assertTrue(len(row) == 10)
        
        
class FunctionTests(unittest.TestCase):
    def setUp(self):
        super(FunctionTests, self).setUp()
        self.GoL = GoL(10, 10)
    
    def test_WeCanPrintTheGame(self):
        printtext = str(self.GoL)
        empty_field = "0 0 0 0 0 0 0 0 0 0 \n" * 10
        self.assertIn('Game of Life', printtext)
        self.assertIn('Step', printtext)
        self.assertIn( empty_field, printtext)
        
    def test_WeCanStepTheGoL(self):
        self.GoL.step()
        
    def test_StepCountIncreases(self):
        StepCount = self.GoL.getStep()
        self.GoL.step()
        self.assertTrue(StepCount + 1 == self.GoL.getStep())
        
        