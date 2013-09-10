"""
JeopPlayer.py
Author: Adam Beagle

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
      * Name
      * Score
      * Scoref (score as formatted string, e.g. '-$1000')
    """
    def __init__(self, name):
        if not isinstance(name, basestring):
            raise TypeError("'name' attribute requires string, got %s: %r"
                            % (type(name), name))
        self._name = name
        self._score = 0

    @property
    def Name(self):
        return self._name

    @property
    def Score(self):
        return self._score

    @Score.setter
    def Score(self, score):
        try:
            self._score = int(score)
        except (ValueError, TypeError):
            raise ScoreError(self.Name, score)

    @property
    def Scoref(self):
        neg = '-' * int(self.Score < 0)
        return "%s$%d" % (neg, abs(self.Score))

###############################################################################
class ScoreError(Exception):
    """
    Exception raised when an invalid set of JeopPlayer.Score is attempted.
    """
    def __init__(self, player, errVal, msg=None):
        """If msg is None, a default message will be used."""
        self.Player = player
        self.ErrVal = errVal

        if msg == None:
            self.Msg = ("An error occured setting the score for player " + 
                        "'%s.' Scores must be int or castable to int." %
                        self.Player)
        else:
            self.Msg == msg

    def __str__(self):
            return self.Msg + " Bad value: %r" % self.ErrVal
