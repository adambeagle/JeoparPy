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
from pygame.locals import USEREVENT

from audioplayer import JeopAudioPlayer
from maingame import Clue, GameBoard, OpenClueAnimation, PodiaPanel

ANIMATIONEND = USEREVENT + 1

###############################################################################
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
    def __init__(self, screen, gameData, fpsLimit):
        w, h  = size = screen.get_size()
        
        board = GameBoard((.75*w, h), gameData)
        board.dirty = True
        podia = PodiaPanel((.25*w, h), gameData)
        podia.dirty = True
        podia.rect.left = .75*w
        clue = Clue((.75*w, h))

        spr = OpenClueAnimation(board.boxSize, board.rect.copy(),
                                ANIMATIONEND, fpsLimit)

        #NOTE Order of self._sfcs is draw order
        self._sfcs = (board, podia, spr, clue) 
        self.audioplayer = JeopAudioPlayer()

    def get_clicked_clue(self, clickPos):
        return self._sfcs[0].get_clicked_clue(clickPos)

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

                if isinstance(sfc, pygame.Surface):
                    screen.blit(sfc, sfc.rect)
                else:
                    screen.blit(sfc.image, sfc.rect)
                    
                dirtyRects.append(sfc.rect)
                sfc.dirty = False

        pygame.display.update(dirtyRects)
        
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
            self._wait_until_sound_end()
        elif gs.state == gs.ANSWER_NONE:
            self._wait_until_sound_end()

    #TODO find a better way to accomplish this.
    #This version is very inconsistent
    def _wait_until_sound_end(self):
        while pygame.mixer.get_busy():
            pass

        pygame.time.wait(350)

    
