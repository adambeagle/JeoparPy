"""
gamestate.py
Author: Adam Beagle

DESCRIPTION:
  Inclues JeopGameState, GameState and StateError classes, described below.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

###############################################################################
class GameState(object):
    """
    The state of a game can be accessed and set from this object.
    Only one state is allowed at any time.

    An optional 'arg' can be set to provide additional
    information about the state.

    Inheriting classes should create states by calling _addstate().

    ATTRIBUTES:
      * arg
      * previous (read-only)
      * state

    'arg' can be set in two ways:
      * Directly, i.e. gamestate.arg = "arg"
      * As 2nd element of an interable when setting 'state'
        ex: gamestate.state = (gamestate.QUIT, "arg")
        
    """
    def __init__(self):
        """Constructor."""
        self._numStates = 0
        self._state = -1
        self._previous = -1
        self.arg = None

    def _addstate(self):
        """
        Returns the next available integer to which a state can be set,
        and updates self._numStates. Always use this when creating a new
        state to assign its value.
        
        """
        self._numStates += 1

        return self._numStates - 1

    def __repr__(self):
        if self.arg is None:
            return repr(self.state)
        else:
            return repr((self.state, self.arg))

    @property
    def previous(self):
        return self._previous
        
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        self.arg = None
        
        #If val is a container, 
        if hasattr(val, '__iter__'):
            try:
                self.arg = val[1]
            except IndexError:
                raise StateError("State must be an int or a 2-tuple " +
                                 "containing (state as int, arg).", val)

            val = val[0]

        #Attempt cast to int
        try:
            val = int(val)
        except (ValueError, TypeError):
            raise StateError("'State' expects integer, not %s." %
                             type(val).__name__, val)

        #Verify state within valid range of defined states
        if val in xrange(self._numStates):
            self._previous = self._state
            self._state = val
        else:
            raise StateError("Set of 'State' attempted with value " +
                             "that has no assigned state.", val)

        if __debug__:
            print "State change: %s" % self.state

###############################################################################
class JeopGameState(GameState):
    """
    Defines the states for a JeoparPy game.

    This and GameData are the primary interfaces
    between the main module and the game logic.

    This also serves as a centralized means of communication
    between main and the UI modules.

    METHODS:
      * transition_state_immediate_linear
    
    """
    def __init__(self):
        super(JeopGameState, self).__init__()

        #Define states
        self.BOARD_FILL = self._addstate()
        self.WAIT_BOARD_FILL = self._addstate()
        self.WAIT_CHOOSE_CLUE = self._addstate()
        self.CLICK_CLUE = self._addstate()
        self.WAIT_CLUE_OPEN = self._addstate()
        self.CLUE_OPEN = self._addstate()
        self.WAIT_CLUE_READ = self._addstate()
        self.WAIT_TRIGGER_AUDIO = self._addstate()
        self.PLAY_CLUE_AUDIO = self._addstate()
        self.WAIT_BUZZ_IN = self._addstate()
        self.BUZZ_IN = self._addstate()
        self.WAIT_ANSWER = self._addstate()
        self.ANSWER_CORRECT = self._addstate()
        self.ANSWER_INCORRECT = self._addstate()
        self.ANSWER_TIMEOUT = self._addstate()
        self.ANSWER_NONE = self._addstate()
        self.DELAY = self._addstate()
        self.GAME_END = self._addstate()        
        self.QUIT = self._addstate()

        #Define state ranges
        self.ANSWER = range(self.ANSWER_CORRECT, self.ANSWER_INCORRECT + 1)

        #Set initial state
        self.state = self.BOARD_FILL

    def transition_state_immediate_linear(self, gameData):
        """
        Handle any simple state transitions; i.e. those that always
        occur immediately and have a single next state (no branching).

        State transitions triggered by events, or whose
        next state branches on conditions occur elsewhere.
        
        """
        s = self
        
        if s.state == s.BOARD_FILL:
            s.state = s.WAIT_BOARD_FILL
            
        elif s.state == s.CLICK_CLUE:
            s.state = (s.WAIT_CLUE_OPEN, s.arg)

        elif s.state == s.PLAY_CLUE_AUDIO:
            column = s.arg[1]
            s.state = (s.WAIT_BUZZ_IN, gameData.amounts[column])

        elif s.state == s.BUZZ_IN:
            s.state = (s.WAIT_ANSWER, s.arg)

        elif s.state == s.ANSWER_CORRECT:
            s.state = s.DELAY

        elif s.state in (s.ANSWER_NONE, s.ANSWER_TIMEOUT, s.DELAY):
            s.state = s.WAIT_CHOOSE_CLUE

###############################################################################
class StateError(Exception):
    """
    Exception raised when a problem occurs setting State in GameState.
    
    """
    def __init__(self, msg='', errVal=None):
        if msg:
            self.msg = msg
        else:
            self.msg = "An error occured when trying to set 'State.'"

        self.errval = errVal

    def __str__(self):
        addendum = (" It is recommended to use the named constants " +
                    "defined in %s to set State." % __file__)
        if not self.errval == None:
            addendum += " Bad value: %r" % self.errval

        return self.msg + addendum
