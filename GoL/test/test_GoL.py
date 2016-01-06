"""
Tests for Conways Game of Life

"""

import unittest
import GoL

class Mytests(unittest.TestCase):
    def test_WeHaveAnObjectPlayfield(self):
        ''' Playfield needs to exists
        '''
        self.assertTrue(isinstance(GoL.playfield, object))