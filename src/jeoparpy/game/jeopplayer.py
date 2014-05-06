"""
jeopplayer.py

DESCRIPTION:
  Holds JeopPlayer and ScoreError classes, described below.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""

###############################################################################
class JeopPlayer(object):
    """
    Defines a Jeoparpy player (or team).

    ATTRIBUTES:
      * hasAnswered
      * name (read-only)
      * score
      * scoref (score as formatted string, e.g. '-$1000'. Read-only.)
    """
    def __init__(self, name):
        self._name = str(name)
        self._score = 0
        self.hasAnswered = False
        
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        try:
            self._score = int(val)
        except (ValueError, TypeError):
            raise ScoreError(self.name, val)

    @property
    def scoref(self):
        neg = '-' * int(self.score < 0)
        return "%s$%d" % (neg, abs(self.score))

###############################################################################
class ScoreError(Exception):
    """
    Exception raised when an invalid set of JeopPlayer.Score is attempted.
    """
    def __init__(self, player, errVal, msg=None):
        """If msg is None, a default message will be used."""
        self.player = player
        self.errval = errVal

        if msg == None:
            self.msg = ("An error occured setting the score for player " + 
                        "'%s.' Scores must be int or castable to int." %
                        self.player)
        else:
            self.msg == msg

    def __str__(self):
            return self.msg + " Bad value: %r" % self.errval
