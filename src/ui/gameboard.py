"""
gameboard.py
Author: Adam Beagle

DESCRIPTION:



Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from pygame import Surface

from config import JEOP_BLUE

class GameBoard(Surface):
    """ """
    def __init__(self, size):
        super(GameBoard, self).__init__(size)
        self.rect = self.get_rect()
        
        self.fill(JEOP_BLUE)
        
