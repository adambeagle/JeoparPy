"""
gamedata.py
Author: Adam Beagle

DESCRIPTION:
  Holds GameData class, described below.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""
from sys import stderr

from constants import AMOUNTS_PATH, CATEGORIES_PATH, CLUES_PATH, PLAYERS_PATH
from jeop_player import JeopPlayer
from ..util import get_stripped_nonempty_file_lines, to_numeric

###############################################################################
class GameData(object):
    """
    Holds core data about the game. This and GameState are the primary
    interfaces between the main module and the game logic.

    The attributes in this class should not need to be changed during a
    single game after being initialized (attribute's attributes, like player
    scores, can be changed).

    ATTRIBUTES:
      * allPlayersAnswered (read-only)
      * amounts
      * categories
      * clues
      * players
      * winners (read-only)

    METHODS:
      * clear_players_answered
      
    """
    def __init__(self):
        """
        Constructor.
        """
        
        
        self.categories = get_stripped_nonempty_file_lines(CATEGORIES_PATH)
        
        self.clues = self._build_clues_from_file(CLUES_PATH,
                                                 len(self.categories))
        
        self.amounts = self._build_amounts_from_file(AMOUNTS_PATH)

        self.players = self._build_players_from_file(PLAYERS_PATH)

    def clear_players_answered(self):
        """Sets all players' hasAnswered attribute to False."""
        for p in self.players:
            p.hasAnswered = False

    def _build_amounts_from_file(self, path):
        """ """
        try:
            return tuple(int(a) for a in
                         get_stripped_nonempty_file_lines(path))
        except (TypeError, ValueError):
            raise TypeError("Problem with values in amounts file. " +
                            "Make sure all lines contain only integers. " +
                            "Bad file: %s" % path)
                            
    def _build_clues_from_file(self, path, numCategories):
        """
        Returns a tuple containing tuples of each categories clues,
        which can be treated as a 2D array.
        'Path' is the path (including name) to the file containing the clues.
        Ex: returnedClues[2][4] would return the 5th clue in the 3rd category.
        """
        clues = []
        clue = []

        #Read all clues from file into clues
        with open(path, 'r') as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    clue.append(stripped)
                elif clue:
                    clues.append(tuple(clue))
                    clue = []

        #Last clue could be leftover beacuse EOF reached
        if clue:
            clues.append(tuple(clue))

        return self._map_clues(clues, numCategories)

    def _build_players_from_file(self, path):
        playerNames = get_stripped_nonempty_file_lines(path)
        if len(playerNames) > 3:
            playerNames = playerNames[:3]
            print >>stderr, ("WARNING: Too many players provided. " +
                             "Extraneous player names ignored. " +
                             "Bad file: %s" % path)
        elif len(playerNames) < 3:
            missing = 3 - len(playerNames)
            playerNames += tuple('Player ' + str(i + 2)
                                 for i in xrange(missing))
        
        return tuple(JeopPlayer(name) for name in playerNames)

    def _map_clues(self, clues, numCategories):
        """
        Map clues from format (clue 0, clue 1, clue 2, ...) to format
        ((Category 1 clues), (Category 2 clues), ...).
        
        """
        mapped = []
        numPerCat = len(clues) / numCategories
        for c in xrange(numCategories):
            start = c*numPerCat
            mapped.append(tuple(clues[start:start + numPerCat]))

        return tuple(mapped)

    @property
    def allPlayersAnswered(self):
        for p in self.players:
            if not p.hasAnswered:
                return False

        return True

    @property
    def winners(self):
        """
        Returns tuple containing tuple(s) of (player #, name) for
        the player(s) with the highest score at the time of calling.
        """
        high = max((p.score for p in self.players))
        
        return tuple((i, p.name) for i, p in enumerate(self.players) if p.score == high)
