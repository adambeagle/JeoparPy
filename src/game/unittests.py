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

from jeop_player import JeopPlayer, ScoreError
from gamedata import GameData
from gamestate import GameState, StateError

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
        self.assertEqual(self.p.name, self.pName)
        self.assertEqual(self.p.score, 0)
        self.assertEqual(self.p.scoref, '$0')

    def test_setScore(self):
        self.p.score = 10
        self.assertEqual(self.p.score, 10)

        self.p.score = '100'
        self.assertEqual(self.p.score, 100)

        self.p.score += 50.0
        self.assertEqual(type(self.p.score), int)
        self.assertEqual(self.p.score, 150)
        self.assertEqual(self.p.scoref, '$150')

        self.p.score -= 200
        self.assertEqual(self.p.score, -50)
        self.assertEqual(self.p.scoref, '-$50')

    def test_badScoreType(self):
        with self.assertRaises(ScoreError):
            self.p.score = [2]
        
###############################################################################
class TestGameState(unittest.TestCase):
    def setUp(self):
        self.gs = GameState()

    def test_outOfRangeState(self):
        with self.assertRaises(StateError):
            self.gs.state = -1

        with self.assertRaises(StateError):
            self.gs.state = self.gs._numStates

    def test_badStateType(self):
        with self.assertRaises(StateError):
            self.gs.state = 'gg'

        with self.assertRaises(StateError):
            self.gs.state = None

    def test_badStateTuple(self):
        with self.assertRaises(StateError):
            self.gs.state = ('arg', 0)

        with self.assertRaises(StateError):
            self.gs.state = (0, )

    def test_setStateInt(self):
        #Assumes at least 2 defined states exist,
        #and assumes a QUIT state exists.
        self._onetest_setint(0)
        self._onetest_setint(1)
        self._onetest_setint(self.gs.QUIT)

    def test_setStateTuple(self):
        #Assumes at least 2 defined states exist,
        #and assumes a QUIT state exists.
        self._onetest_settuple(0, 'arg')
        self._onetest_settuple(1, 5)
        self._onetest_settuple(self.gs.QUIT, [3, 4])

    def _onetest_setint(self, s):
        self.gs.state = s
        self.assertEqual(self.gs.state, s)

    def _onetest_settuple(self, s, arg):
        self.gs.state = (s, arg)
        self.assertEqual(self.gs.state, s)
        self.assertEqual(self.gs.arg, arg)
        self.assertEqual(type(self.gs.arg), type(arg))
        

###############################################################################
class TestGameData(unittest.TestCase):
    def setUp(self):
        pass

###############################################################################
if __name__ == '__main__':
    unittest.main()
        

        
        
