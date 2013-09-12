"""
controller.py
Author: Adam Beagle

DESCRIPTION:
    Contains Controller class, described below.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import pygame

from audioplayer import JeopAudioPlayer
from maingame import GameBoard, PodiaPanel

class Controller(object):
    """
    This class serves as the single interface between main and the
    ui modules. Main should call update() and draw() once every frame,
    in that order.

    ATTRIBUTES:
      * audioplayer

    METHODS:
      * draw
      * draw_all
      * update
      
    """
    def __init__(self, screen, gameData):
        w, h  = size = screen.get_size()
        board = GameBoard((.75*w, h), gameData)
        podia = PodiaPanel((.25*w, h), gameData)
        podia.rect.left = .75*w

        self._sfcs = (board, podia)
        self.audioplayer = JeopAudioPlayer()

    def draw(self, screen):
        """
        Redraws any surface which requires it, and updates
        the screen.
        """
        dirtyRects = []

        for sfc in self._sfcs:
            if sfc.dirty:
                if __debug__:
                    print 'draw %s' % type(sfc).__name__
                    
                screen.blit(sfc, sfc.rect)
                dirtyRects.append(sfc.rect)
                sfc.dirty = False

        pygame.display.update(dirtyRects)

    def draw_all(self, screen):
        """
        Draws all surfaces, regardless of their 'dirty' attribute.
        """
        for sfc in self._sfcs:
            screen.blit(sfc, sfc.rect)

        pygame.display.flip()
        
    def update(self, gameState, gameData):
        """Updates the ui modules based on game state and data."""
        for sfc in self._sfcs:
            sfc.update(gameState, gameData)

        self._play_update_sounds(gameState)

    def _play_update_sounds(self, gameState):
        gs = gameState

        if gs.state == gs.BOARD_FILL:
            self.audioplayer.play('fill')
        if gs.state == gs.BUZZ_IN:
            self.audioplayer.play('buzz')
        elif gs.state == gs.ANSWER_INCORRECT:
            self.audioplayer.play('wrong')
        elif gs.state == gs.ANSWER_TIMEOUT:
            self.audioplayer.play('outoftime')

    
