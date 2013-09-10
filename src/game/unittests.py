"""
unittests.py
Author: Adam Beagle

DESCRIPTION:
  Unit test suite for the game package.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import unittest

from JeopPlayer import JeopPlayer, ScoreError
from GameState import GameState, GameData, StateError

###############################################################################
class TestJeopPlayer(unittest.TestCase):

    def setUp(self):
        self.pName = 'Test Player'
        self.p = JeopPlayer(self.pName)

    def test_missingName(self):
        self.assertRaises(TypeError, JeopPlayer)

    def test_badNameType(self):
        self.assertRaises(TypeError, JeopPlayer, ('n', 'a', 'm', 'e'))
            
    def test_initialAttrs(self):
        self.assertEqual(self.p.Name, self.pName)
        self.assertEqual(self.p.Score, 0)
        self.assertEqual(self.p.Scoref, '$0')

    def test_setScore(self):
        self.p.Score = 10
        self.assertEqual(self.p.Score, 10)

        self.p.Score = '100'
        self.assertEqual(self.p.Score, 100)

        self.p.Score += 50.0
        self.assertEqual(type(self.p.Score), int)
        self.assertEqual(self.p.Score, 150)
        self.assertEqual(self.p.Scoref, '$150')

        self.p.Score -= 200
        self.assertEqual(self.p.Score, -50)
        self.assertEqual(self.p.Scoref, '-$50')

    def test_badScoreType(self):
        with self.assertRaises(ScoreError):
            self.p.Score = [2]
        
###############################################################################
class TestGameState(unittest.TestCase):
    def setUp(self):
        self.gs = GameState()

    def test_outOfRangeState(self):
        with self.assertRaises(StateError):
            self.gs.State = -1

        with self.assertRaises(StateError):
            self.gs.State = self.gs._numStates

    def test_badStateType(self):
        with self.assertRaises(StateError):
            self.gs.State = 'g'

    def test_setState(self):
        #Assumes at least 2 defined states exist,
        #and assumes a QUIT state exists.
        s = 0
        self.gs.State = s
        self.assertEqual(self.gs.State, s)

        s = 1
        self.gs.State = str(s)
        self.assertEqual(self.gs.State, s)

        s = self.gs.QUIT
        self.gs.State = s
        self.assertEqual(self.gs.State, s)

###############################################################################
class TestGameData(unittest.TestCase):
    def setUp(self):
        pass

###############################################################################
if __name__ == '__main__':
    unittest.main()
        

        
        
