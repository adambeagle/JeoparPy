"""
gamestate.py

DESCRIPTION:
  Includes Enum, GameState, JeopGameState, and StateError classes,
  described below.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
from ..config import DEBUG

###############################################################################
class Enum(object):
    """
    Defines an enum-like object.
    A list of names is given which become the enum's elements.
    Elements' integer values assigned in order in which names are passed.

    Ex: days = Enum(('SUNDAY', 'MONDAY', 'TUESDAY'), 1)
        print days.SUNDAY -> '1'
        print days.MONDAY -> '2'
        print days.TUESDAY -> 3
    """
    def __init__(self, names, start=0):
        ns = range(start, start + len(names))
        self.__dict__ = dict(zip(names, ns))

class GameState(Enum):
    """
    The state of a game can be accessed and set from this object.
    Only one state is allowed at any time.

    An optional 'arg' can be set to provide additional
    information about the state.

    ATTRIBUTES:
      * arg
      * previous (read-only)
      * state

    'arg' can be set in two ways:
      * Directly, i.e. gamestate.arg = "arg"
      * As 2nd element of an interable when setting 'state'
        ex: gamestate.state = (gamestate.QUIT, "arg")
    """
    def __init__(self, stateNames):
        """
        Constructor. The names contained in 'stateNames' become the
        objects attribute names that define states (see Enum).
        """
        super(GameState, self).__init__(stateNames)
        self._numStates = len(set(stateNames))
        self._state = -1
        self._previous = -1
        self.arg = None

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

        if DEBUG:
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
        #Define states
        states = (
            'BOARD_FILL',
            'WAIT_BOARD_FILL',
            'WAIT_CHOOSE_CLUE',
            'CLICK_CLUE',
            'WAIT_CLUE_OPEN',
            'CLUE_OPEN',
            'WAIT_CLUE_READ',
            'WAIT_TRIGGER_AUDIO',
            'PLAY_CLUE_AUDIO',
            'START_CLUE_TIMER',
            'WAIT_BUZZ_IN',
            'BUZZ_IN',
            'WAIT_ANSWER',
            'ANSWER_CORRECT',
            'ANSWER_INCORRECT',
            'ANSWER_TIMEOUT',
            'ANSWER_NONE',
            'DELAY',
            'GAME_END',
            'QUIT')
        
        super(JeopGameState, self).__init__(states)

        #Define state ranges
        self.ANSWER = range(self.ANSWER_CORRECT, self.ANSWER_INCORRECT + 1)

        #Set initial state
        self.state = self.BOARD_FILL

    def transition_state_immediate_linear(self, gameData):
        """
        Handle any simple state transitions; i.e. those that always
        occur immediately and have a single next state (no branching).

        State transitions triggered by events, or whose next state
        branches on conditions occur elsewhere.
        """
        s = self
        
        if s.state == s.BOARD_FILL:
            s.state = s.WAIT_BOARD_FILL
            
        elif s.state == s.CLICK_CLUE:
            s.state = (s.WAIT_CLUE_OPEN, s.arg)
            
        elif s.state == s.START_CLUE_TIMER:
            s.state = (s.WAIT_BUZZ_IN, s.arg)

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
