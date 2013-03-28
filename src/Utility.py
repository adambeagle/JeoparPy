"""
Utility.py

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from pygame.locals import *
import collections
from ShadowText import ShadowText
from Config import FONTS, SCREEN_H

def BlitToScreen(screen, sfc, pos=(0, 0)):
    """
    Blit 'sfc' to screen and flip the display.
    Passed 'pos' can be a 2-tuple or a Rect.
    """
    screen.blit(sfc, pos)
    pygame.display.flip()
    

def CreateText(textStr, fontName, size, color=(255, 255, 255), bgColor=None, bold=False):
    """"""
    
    #adjust size for resolution
    if SCREEN_H > 768:
    	size = int(SCREEN_H * (size / 768.0))
    
    if fontName in FONTS:
        font = pygame.font.Font(FONTS[fontName], size)
    else:
        path = pygame.font.match_font(fontName)
        font = pygame.font.Font(path, size)

    if bold:
        font.set_bold(1)
        
    if bgColor:
        text = font.render(textStr, 1, color, bgColor)
    else:
        text = font.render(textStr, 1, color)
    textPos = text.get_rect()

    return text, textPos, font

def CenterSurface(srcSfc, destSfc, x=True, y=True):
    """
    Center srcSfc on destSfc on x and y axes as passed.
    Returns Rect of srcSfc.
    """
    srcRect = srcSfc.get_rect()
    destRect = destSfc.get_rect()

    if x:
        srcRect.centerx = destRect.centerx
    if y:
        srcRect.centery = destRect.centery

    return srcRect

def WaitForKeypress(key=None):
    """
    By default, return control when any key is pressed.
    If one key constant or list is passed, return only when 
    one of those keys is pressed.
    """
    if not isinstance(key, collections.Iterable):
        key = [key]

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if key and event.key in key:
                    loop = False
                elif not key:
                    loop = False

	    if event.type == QUIT:
	        sys.exit()


		    
