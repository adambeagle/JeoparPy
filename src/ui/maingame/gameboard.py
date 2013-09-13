"""
gameboard.py
Author: Adam Beagle

DESCRIPTION:
    Contains the GameBoard class, described below.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import pygame

from jeopgamesfc import JeopGameSurface
from ..config import JEOP_BLUE
from ..resmaps import FONTS
from ..util import BorderedBox, draw_centered_textblock, shadow_text

###############################################################################
class GameBoard(JeopGameSurface):
    """
    The primary JeoparPy game board: categories and clue amounts on a grid.
    
    INHERITED ATTRIBUTES:
        * baseImg
        * dirty
        * rect
    """
    def __init__(self, size, gameData):
        super(GameBoard, self).__init__(size)
        self.fill((0, 0, 0))

        self._boxes = self._init_boxes(len(gameData.categories),
                                         len(gameData.amounts) + 1)

        self._blit_categories(gameData.categories)
        self._draw_all_boxes()
        
        self.baseImg = self.copy()

    def get_clicked_clue(self, clickPos):
        """
        Returns 2-tuple (row, column) of clicked clue
        if the click position is inside a clue's rect,
        otherwise returns None.
        """
        for c, col in enumerate(self._boxes):
            for r, box in enumerate(col[1:]):
                if box.rect.collidepoint(clickPos):
                    return (c, r)

        return None

    def update(self, gameState, gameData):
        gs = gameState

        if gs.state in (gs.ANSWER_CORRECT, gs.ANSWER_TIMEOUT, gs.ANSWER_NONE):
            self.dirty = True

    def _blit_categories(self, categories):
        font = pygame.font.Font(FONTS['category'], self._scale(32))
        shadowOffset = self._scale(3)
        
        for i, c in enumerate(categories):
            lines = c.split(' ')
            draw_centered_textblock(self._boxes[i][0], lines, font,
                                    (255, 255, 255), 0, shadowOffset)

    def _draw_all_boxes(self):
        for col in self._boxes:
            for box in col:
                self.blit(box, box.rect)

    def _init_boxes(self, nCols, nRows):
        boxes = []
        size = self.rect.size
        boxW = size[0] / nCols
        boxH = size[1] / nRows
        borderW = self._scale(2)

        clueBox = BorderedBox((boxW, boxH), JEOP_BLUE,
                          borderW, (0, 0, 0))

        catBox = BorderedBox((boxW, boxH), JEOP_BLUE,
                             (borderW, borderW, borderW*3, borderW),
                             (0, 0, 0))

        for col in xrange(nCols):
            colBoxes = []

            if col == nCols - 1:
                clueBox.borderWidths = (borderW, 4*borderW, borderW, borderW)
                catBox.borderWidths = (borderW, 4*borderW, 3*borderW, borderW)
                clueBox.redraw()
                catBox.redraw()

            catBox.rect.topleft = (boxW*col, 0)
            colBoxes.append(catBox.copy())

            for row in xrange(1, nRows):
                clueBox.rect.topleft = (boxW*col, boxH*row)
                colBoxes.append(clueBox.copy())

            boxes.append(tuple(colBoxes))
        
        return tuple(boxes)

    def _init_grid(self, nCols, nRows):
        """ """
        return tuple(rects)

    def _scale(self, n):
        return int(n * self.rect.height / 720.0)
        
        
###############################################################################
