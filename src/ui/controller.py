"""
controller.py
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

from gameboard import GameBoard
from podiapanel import PodiaPanel

class Controller(object):
    """ """
    def __init__(self, screen, gameData):
        w, h  = size = screen.get_size()
        self._board = GameBoard((.75*w, h), gameData)
        self._podia = PodiaPanel((.25*w, h), gameData)
        self._podia.rect.left = .75*w

    def draw(self, screen):
        dirtyRects = []
        
        if self._podia.dirty:
            print 'draw podia' #debug
            screen.blit(self._podia, self._podia.rect)
            dirtyRects.append(self._podia.rect)

        if self._board.dirty:
            screen.blit(self._board, self._board.rect)
            dirtyRects.append(self._board.rect)

        pygame.display.update(dirtyRects)

    def draw_all(self, screen):
        screen.blit(self._board, self._board.rect)
        screen.blit(self._podia, self._podia.rect)
        pygame.display.flip()
        
    def update(self, gameState, gameData):
        self._podia.update(gameState, gameData)

    
