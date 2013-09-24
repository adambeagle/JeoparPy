"""
podium.py
Author: Adam Beagle

DESCRIPTION:
    Contains the Podium class and its utility classes AnswerTimer,
    Highlight, and Score, all described below.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import pygame

from jeopgamesfc import JeopGameSurface
from ...config import ANSWER_TIME_MS
from ..constants import JEOP_BLUE
from ..resmaps import FONTS, IMAGES
from ..util import draw_centered_textline, shadow_text
from ...constants import ANSWER_TIMEOUT

###############################################################################
# Note: This class is subclassed from DirtySprite and not JeopGameSurface
# because the convert_alpha method, which returns a pygame.Surface,
# is needed to have the podium image display properly. 
class Podium(pygame.sprite.DirtySprite):
    """
    One JeoparPy player podium. Inclues a drawn name, an answer timer,
    and an updatable score.

    Call update() once per frame to keep all visuals updated.

    ATTRIBUTES:
      * dirty
      * image
      * rect

    METHODS:
      * update
      
    """
    def __init__(self, id_, img, scalar, name, nameFont, nameOffset, *groups):
        """
        Upon initialization, name and a score of '$0' will be drawn. 
        'nameOffset' is the y-offset of a name on the original podium image.
        """

        scaledSize = tuple(int(scalar*x) for x in img.get_size())
        img = pygame.transform.smoothscale(img, scaledSize)
        self.image = img.copy()
        self.rect = self.image.get_rect()
        super(Podium, self).__init__(*groups)

        self._id = id_
        self._baseImg = None
        self._highlight = pygame.sprite.GroupSingle(Highlight(scaledSize))
        self._score = JeopScore(self.rect, scalar)
        self._timer = self._init_timer(scalar)

        self._draw_name(name, nameFont, int(scalar*nameOffset))
        self.image.blit(self._score, self._score.rect)
        self.dirty = 1

    def update(self, gameState, gameData):
        """
        Update all visuals on the image attribute.
        Should be called once per frame.
        """
        gs = gameState

        if gs.state == gs.BUZZ_IN and gs.arg[0] == self._id:
            self._timer.start()
            self._draw_highlight()
            self.dirty = 1

        elif gs.state in gs.ANSWER and gs.arg[0] == self._id:
            p = gameData.players[self._id]

            self._score.update(p.score, p.scoref)
            
            self._clear_highlight()
            self.image.blit(self._score, self._score.rect)
            self.dirty = 1

        self._timer.update(gameState)
        if self._timer.dirty:
            self.image.blit(self._timer, self._timer.rect)
            self._timer.dirty = 0
            self.dirty = 1
            
    def _clear_highlight(self):
        self._highlight.clear(self.image, self._baseImg)

    def _draw_highlight(self):
        self._baseImg = self.image.copy()
        self._highlight.draw(self.image)

    def _draw_name(self, name, font, nameOffset):
        text = font.render(name, 1, (255, 255, 255))
        
        rect = text.get_rect()
        rect.centerx = self.rect.centerx
        rect.y = nameOffset

        self.image.blit(text, rect)

    def _init_timer(self, scalar):
        pos = tuple(int(scalar*x) for x in (80, 3))
        timer = AnswerTimer(
                    pygame.image.load(IMAGES['podtimer']).convert_alpha(),
                    scalar, ANSWER_TIME_MS)

        timer.rect.topleft = pos
        self.image.blit(timer, timer.rect)

        return timer
        

###############################################################################
class AnswerTimer(JeopGameSurface):
    """
    Defines a rectangular timer, with a different colored block that
    smoothly counts down from both sides, meeting in the middle when
    specified length of time reached.

    ATTRIBUTES:
      * offColor
      * on
      * onColor
      * timerLen (in ms)

    METHODS:
      * reset
      * start
      * update
      

    """
    def __init__(self, img, scalar, time, onColor=(230, 0, 0),
                 offColor=(30, 30, 30)):
        """'time' in ms."""
        size = tuple(int(scalar*x) for x in img.get_size())
        super(AnswerTimer, self).__init__(size)
        
        self._front = pygame.transform.smoothscale(img, size)
        self.offColor = offColor
        self.onColor = onColor
        self._startTime = None
        self._endTime = None
        self.dirty = 0
        
        self.timerLen = time
        self.on = False

        self._draw_off()

    def reset(self):
        """Reset and redraws the timer in its initial state."""
        self._endTime = None
        self.on = False
        self._draw_off()

    def update(self, gameState):
        """
        Update the timer image. Note this has no effect if
        timer is not turned on. 
        """
        gs = gameState

        if self.on and gs.state == gs.WAIT_ANSWER:
            currentTime = pygame.time.get_ticks()

            if currentTime >= self._endTime:
                pygame.event.post(pygame.event.Event(ANSWER_TIMEOUT))
                self.reset()
            else:
                self._draw(currentTime)
                
        elif self.on and gs.state in gs.ANSWER:
            self.reset()

    def start(self):
        """Start and redraw the timer."""
        self.on = True
        time = pygame.time.get_ticks()
        self._endTime = time + self.timerLen
        self._draw(time)

    def _draw_off(self):
        self.fill(self.offColor)
        self.blit(self._front, (0, 0))
        self.dirty = 1

    def _draw(self, currentTime):
        et = self._endTime
        ct = currentTime
        tl = self.timerLen
        centerx = self.rect.w / 2
        percDone = (et - ct) / float(tl)

        self.fill(self.offColor)

        if percDone < 1:
            size = (centerx, self.rect.h)
            rect = pygame.Rect((0, 0), size)
            rect.w = int(percDone * rect.w)

            rect.right = centerx
            self.fill(self.onColor, rect)
            rect.left = centerx
            self.fill(self.onColor, rect)

        self.blit(self._front, (0, 0))
        self.dirty = 1

###############################################################################
class Highlight(pygame.sprite.Sprite):
    """
    Defines an alpha-masked highlight sprite.
    """
    def __init__(self, size):
        super(Highlight, self).__init__()
        img = pygame.image.load(IMAGES['highlight']).convert_alpha()
        self.image = pygame.transform.smoothscale(img, size)
        
        self.rect = self.image.get_rect()

###############################################################################
class Score(JeopGameSurface):
    """
    Defines a rectangular surface with an updatable score written on it.

    Call update() to change the score and redraw the surface.
    """
    def __init__(self, pos, size, font, bgColor, shadowOffset, initial='$0'):
        """
        If 'shadowOffset' 0 or None, no shadow will be drawn.
        """
        super(Score, self).__init__(size)

        self._font = font
        self._posColor = (255, 255, 255)
        self._negColor = (230, 0, 0)
        self._bgColor = bgColor
        self._shadowOffset = shadowOffset
        self._text = initial

        self.rect = pygame.Rect(pos, size)
        self.fill(self._bgColor)
        self._draw_text(self._posColor)

    def update(self, score, scoref):
        color = self._posColor if score >= 0 else self._negColor
        self._text = scoref
        self._draw_text(color)

    def _draw_text(self, color):
        self.fill(self._bgColor)
        draw_centered_textline(self, self._text, self._font, color,
                               self._shadowOffset)
        
###############################################################################
class JeopScore(Score):
    """
    A Score specialized for a Jeoparpy game. Automatically
    sets font and positions rect.
    """
    def __init__(self, podiumRect, scalar):
        bgColor = JEOP_BLUE
        font = pygame.font.Font(FONTS['score'], int(scalar*32))
        pos = tuple(int(scalar*x) for x in (64, 30))
        size = tuple(int(scalar*x) for x in (154, 47))
        shadowOffset = max(1, int(scalar*3))
        
        super(JeopScore, self).__init__(pos, size, font, bgColor,
                                        shadowOffset)
