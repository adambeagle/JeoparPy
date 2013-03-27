"""
Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from pygame.locals import *
from ShadowText import ShadowText
from Utility import CreateText, CenterSurface, BlitToScreen
from Config import JEOP_BLUE, CATEGORIES, FONTS, SCREEN_H

########################################################################
def DoScroll(screen, background):
    """Draws scroll animation through all CATEGORIES to screen"""
    w = background.get_width()
    step = int(SCREEN_H * (-10 / 768.0))
    holdTime = 2500
    bgSize = background.get_size()
    borderWidth = int(SCREEN_H * (30 / 768.0))
    lastBox = None
    #clock = pygame.time.Clock()

    stop = len(CATEGORIES) - 1
    
    #for each box (minus the last one), draw box, hold, and scroll to next box
    for i in range(stop):
        #create showing category box
        box1 = _CreateBox(bgSize, borderWidth, i).convert()

        #create box 2; category to scroll to
        box2 = _CreateBox(bgSize, borderWidth, i + 1).convert()
        if i == stop - 1:
            lastBox = box2

        #draw box1 and wait
        background.blit(box1, (0, 0))
        BlitToScreen(screen, background)
        pygame.time.delay(holdTime)

        #scroll to next box
        x1 = step
        x2 = w + step

        while x2 > 0 + abs(step):
		background.fill(JEOP_BLUE)
		background.blit(box1, (x1, 0))
		background.blit(box2, (x2, 0))
		x1 += step
		x2 += step

		BlitToScreen(screen, background)
		#clock.tick_busy_loop(100)


    #draw last box and wait
    background.blit(lastBox, (0, 0))
    BlitToScreen(screen, background)
    pygame.time.delay(holdTime)

    
########################################################################
def _CreateBox(size, borderWidth, categoryI):
    """Returns Surface of category box with borders and text already drawn"""
    sfc = pygame.Surface(size)
    sfc.fill(JEOP_BLUE)
    _DrawBorders(borderWidth, sfc)
    _DrawText(sfc, categoryI)
    
    return sfc


########################################################################
def _DrawBorders(borderWidth, sfc):
    """Draws black border of width specified on all sides of sfc"""
    bW = borderWidth
    color = (0, 0, 0)
    w, h = sfc.get_size()
    
    #draw left border
    side = pygame.Surface((bW, h))
    side.fill(color)
    sfc.blit(side, (0, 0))

    #draw right border
    sfc.blit(side, (w - bW, 0))

    #draw top border
    top = pygame.Surface((w, bW))
    top.fill(color)
    sfc.blit(top, (0, 0))

    #draw bottom border
    sfc.blit(top, (0, h - bW))
    

########################################################################
def _DrawText(sfc, categoryI):
    """Draws text from CATEGORIES constant onto sfc"""
    cat = CATEGORIES[categoryI]
    
    text, textPos, font = CreateText(cat, 'category',  120)
    textPos = CenterSurface(text, sfc)

    shadow, shadPos = ShadowText(cat, textPos, font, 7)
    
    sfc.blit(shadow, shadPos)
    sfc.blit(text, textPos)

 
