"""
categoryscroll.py
Author: Adam Beagle

DESCRIPTION:
  Functions implementing part of the JeoparPy introduction sequence where
  category names scroll by, holding on each name for a set amount of time.

USAGE:
  Main should only need to call do_scroll.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import pygame

from config import CATEGORY_HOLD_TIME, JEOP_BLUE
from resmaps import FONTS
from util import BorderedBox, draw_centered_textblock, shadow_text
from ..util import chunker

###############################################################################
def do_scroll(screen, clock, categories):
    scrSize = screen.get_size()
    boxes = tuple(_build_box(scrSize, c) for c in categories)
    step = _scale(6, scrSize[1])

    #Hold on each box, then scroll
    for box, nextBox in chunker(boxes, 2, True):
        _blit_to_screen_and_update(screen, box)
        pygame.time.delay(CATEGORY_HOLD_TIME)
        _animate_scroll(screen, scrSize, clock, box, nextBox, step)

    #Draw final box and hold
    _blit_to_screen_and_update(screen, boxes[-1])
    pygame.time.delay(CATEGORY_HOLD_TIME)
                        
###############################################################################
def _animate_scroll(screen, scrSize, clock, box1, box2, step):
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

def _blit_to_screen_and_update(screen, sfc):
    screen.blit(sfc, (0, 0))
    pygame.display.update()

def _build_box(size, category):
    """
    Returns surface containing centered category text and a black border.
    'size' is size of surface to create.
    """
    borderW = _scale(33, size[1])
    box = BorderedBox(size, JEOP_BLUE, borderW, (0, 0, 0))
    
    font = pygame.font.Font(FONTS['category'], _scale(150, size[1]))

    draw_centered_textblock(box, category.split(' '), font,
                            (255, 255, 255), 0, _scale(7, size[1]))

    return box

def _scale(n, rel):
    return  int(n * (rel / 720.0))

###############################################################################
if __name__ == '__main__':
    #Test run
    pygame.init()
    categories=('cat 1', 'cat 2', 'cat 3')
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))
    do_scroll(screen, clock, categories)

    
    
