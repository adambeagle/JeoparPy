"""
GameData.py
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
from adam.util.types_util import ToNumeric

from config import AMOUNTS, CLUES_PATH, CATEGORIES_PATH, PLAYER_NAMES
from JeopPlayer import JeopPlayer

###############################################################################
class GameData(object):
    """
    Holds core data about the game. This and GameState are the primary
    interfaces between the main module and the game logic.

    Attributes:
      *Players
      *Clues
      *Categories
      *Amounts
      *WinningPlayers
    """
    def __init__(self):
        """
        Constructor. Assumes AMOUNTS, CLUES_PATH, CATEGORIES_PATH,
        and PLAYER_NAMES are set as instructed in the game
        package's config.py.
        """
        self.Players = tuple(JeopPlayer(name) for name in PLAYER_NAMES)
        
        self.Categories = self._BuildCategoriesFromFile(CATEGORIES_PATH)
        self.Clues = self._BuildCluesFromFile(CLUES_PATH, len(self.Categories))
        self.Amounts = AMOUNTS

    def _BuildCategoriesFromFile(self, path):
        """
        Returns a tuple of strings, each a category name.
        'Path' is the path, including filename, of the
        file containing the categories.
        Separate categories are expected to be on separate lines in the file.
        """
        categories = []
        
        with open(path, 'r') as f:
            for line in f:
                stripped = line.strip()
                if len(stripped) > 0:
                    categories.append(stripped)

        return tuple(categories)
                    
    def _BuildCluesFromFile(self, path, numCategories):
        """
        Returns a tuple containing tuples of each categories clues,
        which can be treated as a 2D array.
        'Path' is the path (including name) to the file containing the clues.
        Ex: returnedClues[2][4] would return the 5th clue in the 3rd category.
        """
        clues = ['']

        #Read all clues from file into clues
        with open(path, 'r') as f:
            for line in f:
                if not line == "\n":
                    clues[-1] += line
                else:
                    if not clues[-1] == '':
                        clues.append('')

        #Map clues to format (("Cat 1 clue", ...), ("Cat 2 clue", ...), ...)
        mapped = []
        numPerCat = len(clues) / numCategories
        for c in xrange(numCategories):
            start = c*numPerCat
            mapped.append(tuple(clues[start:start + numPerCat]))

        return tuple(mapped)

    @property
    def WinningPlayers(self):
        """
        Returns tuple containing names of player(s) with
        the highest score at the time of calling.
        """
        high = max((p.Score for p in self.Players))
        
        return tuple(p.Name for p in self.Players if p.Score == high)
