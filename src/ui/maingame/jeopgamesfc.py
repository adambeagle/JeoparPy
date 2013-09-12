"""
jeopgamesfc.py
Author: Adam Beagle

DESCRIPTION:
    Contains JeopGameSurface class, described below.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from pygame import Surface

###############################################################################
class JeopGameSurface(Surface):
    """
    Base class for primary game surfaces. Not to be used directly.

    Calling the update() function on every frame with a GameState and
    GameData object will automatically update the surface as needed.
    
    Methods:
      *update

    Attributes:
      * baseSfc             - "Blank" surface to use to clear text, etc.
      * dirty               - When set, controller should redraw the panel.
      * dirtyRects          - List of rects that need to be updated on screen.
      * rect
      * size (read-only)
      
    """
    def __init__(self, size):
        super(JeopGameSurface, self).__init__(size)
        
        self.rect = self.get_rect()
        self._size = self.rect.size
        self.dirty = True
        self.dirtyRects = []
        self.baseSfc = None

    def update(self, gameState, gameData):
        """Update surface accordingly from current state of game."""
        
        raise NotImplementedError("Subclasses of JeopGameSurface must " +
                                  "define this method.")

    @property
    def size(self):
        return self._size
