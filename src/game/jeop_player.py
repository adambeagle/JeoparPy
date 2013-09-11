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
      * name
      * score
      * scoref (score as formatted string, e.g. '-$1000')
    """
    def __init__(self, name):
        if not isinstance(name, basestring):
            raise TypeError("'name' attribute requires string, got %s: %r"
                            % (type(name), name))
        self._name = name
        self._score = 0

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
