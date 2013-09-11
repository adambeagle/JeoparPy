"""
gamestate.py
Author: Adam Beagle

DESCRIPTION:
  Inclues GameState and StateError classes, described below.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

##############################################################################
class GameState(object):
    """
    The state of the game can be accessed and set from this object.
    Only one state is allowed at any time.

    This and GameData are the primary interfaces
    between the main module and the game logic.

    This also serves as a centralized means of communication
    between main and the UI modules.

    ATTRIBUTES:
      *State
    """
    def __init__(self):
        """Constructor."""
        self._numStates = 0

        #TODO define all states
        self.QUIT = self._addstate()
        self.GAME_END = self._addstate()
        self.WAIT = self._addstate()
        self.CLUE_OPEN = self._addstate()
       
        self._state = self.WAIT

    def _addstate(self):
        """
        Returns the next available integer to which a state can be set,
        and updates self._numStates. Always use this when creating a new
        state to assign its value.
        """
        self._numStates += 1

        return self._numStates - 1
        
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        try:
            val = int(val)
        except (ValueError, TypeError):
            raise StateError("'State' expects integer, not %s." %
                             type(val).__name__, val)

        if val in xrange(self._numStates):
            self._state = val
        else:
            raise StateError("Set of 'State' attempted with invalid value.",
                             val)

##############################################################################
class StateError(Exception):
    """
    Exception raised when a problem occurs setting State in GameState.
    """
    def __init__(self, msg='', errVal=None):
        if msg:
            self.Msg = msg
        else:
            self.Msg = "An error occured when trying to set 'State.'"

        self.ErrVal = errVal

    def __str__(self):
        addendum = (" It is recommended to use the named constants " +
                    "defined in %s to set State." % __file__)
        if not self.ErrVal == None:
            addendum += " Bad value: %r" % self.ErrVal

        return self.Msg + addendum
