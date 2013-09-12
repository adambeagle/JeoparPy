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

import pygame

from config import JEOP_BLUE
from resmaps import FONTS
from util import BorderedBox, shadow_text

###############################################################################
class GameBoard(pygame.Surface):
    """
    ATTRIBUTES:
        * dirty
        * rect
    """
    def __init__(self, size, gameData):
        super(GameBoard, self).__init__(size)
        self.fill((0, 0, 0))
        
        self.rect = self.get_rect()
        self.dirty = 1

        self._boxes = self._init_boxes(len(gameData.categories),
                                         len(gameData.amounts) + 1)

        self._blit_categories(gameData.categories)
        self._draw_all_boxes()

    def _blit_categories(self, categories):
        font = pygame.font.Font(FONTS['category'], self._scale(32))
        shadowOffset = self._scale(3)
        
        for i, c in enumerate(categories):
            lines = c.split(' ')
            self._boxes[0][i].draw_centered_textblock(lines, font,
                                                      (255, 255, 255), 0,
                                                      shadowOffset)

    def _draw_all_boxes(self):
        for row in self._boxes:
            for box in row:
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

        #Transpose boxes into format ((row), (row), ...)
        boxes = zip(*boxes[::1])
        
        return tuple(boxes)

    def _init_grid(self, nCols, nRows):
        """ """
        return tuple(rects)

    def _scale(self, n):
        return int(n * self.rect.height / 720.0)
        
        
###############################################################################
