"""
CategoryScroll.py
Author: Adam Beagle

DESCRIPTION:
  Functions implementing part of the JeoparPy introduction sequence where
  category names scroll by, holding on each name for a set amount of time.

USAGE:
  Main should only need to call doScroll.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import pygame

from adam.game.pygame_util import ShadowText
from adam.util.sequence_util import Chunker

from config import CATEGORY_HOLD_TIME, FONTS, JEOP_BLUE

###############################################################################
def doScroll(screen, clock, categories):
    scrSize = screen.get_size()
    boxes = tuple(_buildBox(scrSize, c) for c in categories)
    step = int(7 * (scrSize[1] / 768.0))
    

    #Hold on each box, then scroll
    for box, nextBox in Chunker(boxes, 2, True):
        _blitToScreenAndUpdate(screen, box)
        pygame.time.delay(CATEGORY_HOLD_TIME)
        _animateScroll(screen, scrSize, clock, box, nextBox, step)

    #Draw final box and hold
    _blitToScreenAndUpdate(screen, boxes[-1])
    pygame.time.delay(CATEGORY_HOLD_TIME)
                        
###############################################################################
def _animateScroll(screen, scrSize, clock, box1, box2, step):
    """
    Scrolls box to the left, filling in space with box2 until
    box2 fills the screen. The boxes must be surfaces.
    'step' is the amount in pixels to shift the boxes on
    each animation step.
    """
    w, h = scrSize
    offset = step

    while offset <= w:
        #Update showing areas
        area1 = pygame.Rect(offset, 0, w - offset, h)
        area2 = pygame.Rect(0, 0, offset, h)

        #Blit and update
        screen.blit(box1, (0, 0), area1)
        screen.blit(box2, (w - offset, 0), area2)
        pygame.display.update()

        #Increment offset and tick clock/fps limiter
        offset += step
        clock.tick_busy_loop(250) 

def _blitCategoryName(sfc, category, fontSize):
    sfcRect = sfc.get_rect()
    
    font = pygame.font.Font(FONTS['category'], fontSize)
    text = font.render(category, 1, (255, 255, 255))

    rect = text.get_rect()
    rect.center = sfc.get_rect().center

    shadow, shadRect = ShadowText(category, rect, font, 5)

    sfc.blit(shadow, shadRect)
    sfc.blit(text, rect)

def _blitToScreenAndUpdate(screen, sfc):
    screen.blit(sfc, (0, 0))
    pygame.display.update()

def _buildBox(size, category):
    """
    Returns surface containing centered category text and a black border.
    'size' is size of surface to create.
    """
    outer = pygame.Surface(size)
    outer.fill((0, 0, 0))

    borderW = int(35 * (size[1] / 768.0))
    inner = pygame.Surface((size[0] - 2*borderW, size[1] - 2*borderW))
    inner.fill(JEOP_BLUE)
    _blitCategoryName(inner, category,
                      int(140 * (size[1] / 768.0)))

    outer.blit(inner, (borderW, borderW))

    return outer

###############################################################################
if __name__ == '__main__':
    #Test run
    pygame.init()
    categories=('cat 1', 'cat 2', 'cat 3')
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))
    doScroll(screen, clock, categories)

    
    
