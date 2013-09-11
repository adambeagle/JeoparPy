"""
podiapanel.py
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

from adam.game.pygame_util import shadow_text

from config import JEOP_BLUE
from resmaps import FONTS, IMAGES

###############################################################################
class PodiaPanel(pygame.Surface):
    """
    Methods:
      *update

    Attributes:
      *dirty
      *rect
      *size
      
    """
    def __init__(self, size):
        super(PodiaPanel, self).__init__(size)
        self.size = self.get_size()
        self.rect = self.get_rect()
        self.dirty = True

        self._init_background()
        self._podiaRects = self._draw_podia(self._init_podia())

        self._blankPanel = self.copy()

        self._highlight = pygame.sprite.GroupSingle(
            Highlight(self._podiaRects[0].size))

        self._scores = self._init_scores()
        self._scores.draw(self)


    def update(self, gameState, gameData):
        self.dirty = False
        
        if gameState.state == gameState.BUZZ_IN:
            self._draw_highlight(gameState.arg)
            self.dirty = True
        
        if gameState.state in gameState.ANSWER:
            self._clear_highlight()
            score = [spr for spr in self._scores.sprites() if spr.ID == gameState.arg][0]
            score.dirty = 1
            self._scores.draw(self)
            self.dirty = True

        if gameState.state == gameState.ANSWER_CORRECT:
            self._scores.update(gameData)
            self._scores.draw(self)
            self.dirty = True
            

    def _clear_highlight(self):
        self._highlight.clear(self, self._blankPanel)

    def _draw_highlight(self, playerI):
        self._highlight.sprite.rect = self._podiaRects[playerI].copy()
        self._highlight.draw(self)

    def _draw_podia(self, podiumSfc):
        """
        Draws the 3 podia to the panel.
        Returns tuple containing the rects of the podia drawn.
        """
        rect = podiumSfc.get_rect()
        padding = (self.size[1] - 3*rect.h) / 4
        rect.centerx = self.rect.centerx
        rect.top = padding

        rects = []

        for i in xrange(3):
            self.blit(podiumSfc, rect)
            rects.append(rect.copy())
            
            rect.top += rect.h + padding

        return tuple(rects)
        
    def _init_background(self):
        img = pygame.image.load(IMAGES['rPanelBG']).convert()
        sizeScalar = float(img.get_size()[1]) / self.size[1]
        img = pygame.transform.smoothscale(img, self.size)
        self.blit(img, (0, 0))


    def _init_podia(self):
        """
        Returns the surface of a single podium, correctly
        scaled for the height of the panel.
        """
        img = pygame.image.load(IMAGES['podium']).convert_alpha()
        origSize = img.get_size()

        #Scale image to be 30% height of screen
        h = int(0.3 * self.size[1])
        w = int(origSize[0] * (float(h) / origSize[1]))
        img = pygame.transform.smoothscale(img, (w, h))
        
        return img

    def _init_scores(self):
        sprites = []

        for i in xrange(3):
            sprites.append(Score(self._podiaRects[i], i))

        return pygame.sprite.OrderedUpdates(*sprites)
        

###############################################################################
class Highlight(pygame.sprite.Sprite):
    """ """
    def __init__(self, size):
        super(Highlight, self).__init__()
        img = pygame.image.load(IMAGES['highlight']).convert_alpha()
        self.image = pygame.transform.smoothscale(img, size)
        
        self.rect = self.image.get_rect()

###############################################################################
class Score(pygame.sprite.DirtySprite):
    """ """
    def __init__(self, podiumRect, id_):
        super(Score, self).__init__()
        scalar = (float(podiumRect.w) /
                  pygame.image.load(IMAGES['podium']).get_size()[0])
        posOffset = tuple(int(scalar*x) for x in (64, 30))
        size = tuple(int(scalar*x) for x in (154, 47))
        self.rect = pygame.Rect(podiumRect.topleft, size)
        self.rect.move_ip(*posOffset)

        self.image = pygame.Surface(size)

        self._font = pygame.font.Font(FONTS['score'], int(32*scalar))

        self._text = '$0'
        self._id = id_

        self._draw_text(self._text)

    def update(self, gameData):
        scoref = gameData.players[self._id].scoref

        if not scoref == self._text:
            self._text = scoref
            self._draw_text(scoref)
            self.dirty = 1
            

    def _draw_text(self, text):
        s = text
        text = self._font.render(s, 1, (255, 255, 255))

        rect = text.get_rect()
        rect.centerx = self.rect.centerx - self.rect.x
        rect.centery = self.rect.centery - self.rect.y

        shadow, shadRect = shadow_text(s, rect, self._font, 3)

        self.image.fill(JEOP_BLUE)
        self.image.blit(shadow, shadRect)
        self.image.blit(text, rect)

    @property
    def ID(self):
        return self._id

        

###############################################################################
if __name__ == '__main__':
    #Test run
    pygame.init()
    screen = pygame.display.set_mode((800, 450))

    screen.fill((0, 0, 0))
    rp = PodiaPanel((.25*800, 450))
    
    screen.blit(rp, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)
    
    rp._draw_highlight(2)
    screen.blit(rp, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)

    rp._clear_highlight()
    rp._scores[2].dirty = 1
    rp._scores.draw(rp)
    screen.blit(rp, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)
