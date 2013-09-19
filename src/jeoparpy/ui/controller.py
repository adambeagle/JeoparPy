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

###############################################################################
class Controller(object):
    """
    This class serves as the single interface between main and the
    ui modules. Main should call update() and draw() once every frame,
    in that order.

    ATTRIBUTES:
      * audioplayer

    METHODS:
      * clue_has_audio_reading
      * clue_is_audioclue
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

        spr = OpenClueAnimation(board.boxSize, board.rect.copy(), fpsLimit)

        #NOTE Order of self._sfcs is draw order
        self._sfcs = (board, podia, spr, clue) 
        self.audioplayer = JeopAudioPlayer()

    def clue_has_audio_reading(self, coords):
        return coords + ('cr', ) in self.audioplayer.sounds

    def clue_is_audioclue(self, coords):
        return coords in self.audioplayer.sounds

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

                if isinstance(sfc, pygame.sprite.Sprite):
                    screen.blit(sfc.image, sfc.rect)
                else:
                    #Case: sfc is pygame.Surface
                    screen.blit(sfc, sfc.rect)

                dirtyRects.append(sfc.rect)
                sfc.dirty = False

        pygame.display.update(dirtyRects)

    def get_clicked_clue(self, clickPos):
        return self._sfcs[0].get_clicked_clue(clickPos)
        
    def update(self, gameState, gameData):
        """Updates the ui modules based on game state and data."""
        for sfc in self._sfcs:
            sfc.update(gameState, gameData)

        self._play_update_sounds(gameState)

    def _play_update_sounds(self, gameState):
        gs = gameState

        if gs.state == gs.BOARD_FILL:
            self.audioplayer.play('fill')
        elif gs.state == gs.CLUE_OPEN:
            key = gs.arg + ('cr', )
            if key in self.audioplayer.sounds:
                self.audioplayer.play(key)
        elif gs.state == gs.PLAY_CLUE_AUDIO:
            self.audioplayer.play(gs.arg)
        elif gs.state == gs.BUZZ_IN:
            self.audioplayer.stop_all()
            self.audioplayer.play('buzz')
        elif gs.state == gs.ANSWER_INCORRECT:
            self.audioplayer.play('wrong')
        elif gs.state == gs.ANSWER_TIMEOUT:
            self.audioplayer.play('outoftime')
            self.audioplayer.wait_until_sound_end(200)
        elif gs.state == gs.ANSWER_NONE:
            self.audioplayer.wait_until_sound_end(350)
