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
import sys
from ShadowText import ShadowText
from Utility import CreateText, CenterSurface, BlitToScreen, WaitForKeypress
from Config import SOUNDS, IMGS, SCREEN_SIZE, SCREEN_H, SUBTITLE

######################################################################
def DoIntro(screen, background):
    """Draw Jeopardy intro animation to screen"""
    #start music
    music = pygame.mixer.Sound(SOUNDS['intro'])
    music.play()

    #declarations
    clock = pygame.time.Clock()
    bgImg = pygame.image.load(IMGS['introBG']).convert()
    bgImg = pygame.transform.scale(bgImg, SCREEN_SIZE).convert()
    bannerColor = (0, 0, 50)
    alpha = 0

    #title text
    text, textPos, font = CreateText('JEOPARPY!', 'title', 150,
                               (230, 230, 230), bannerColor)
    textPos = CenterSurface(text, background)

    #title banner
    h = int(SCREEN_H * (175.0 / 768))
    banner = pygame.Surface((background.get_width(), h))
    banner.fill(bannerColor)
    bannerPos = CenterSurface(banner, background, x=0, y=1)

    #draw initial image
    background.blit(bgImg, (0, 0))
    background.blit(banner, bannerPos)
    BlitToScreen(screen, background)

    #hold initial image
    pygame.time.delay(3000)

    #fade in text
    while alpha < 255:
        text.set_alpha(alpha)
        _Redraw(background, bgImg, banner, bannerPos)
        background.blit(text, textPos)
        BlitToScreen(screen, background)
        alpha += 1
        clock.tick_busy_loop(36)
        
    #create substring and shadow
    subStr = SUBTITLE
    sub, subPos, subFont = CreateText(subStr, 'subtitle', 52)
    subPos = CenterSurface(sub, background, x=1, y=0)
    subPos.top = textPos.bottom + int(SCREEN_H * (20.0 / 768))
    shadow, shadPos = ShadowText(subStr, subPos, subFont, 2)
    background.blit(shadow, shadPos)
    background.blit(sub, subPos)
    BlitToScreen(screen, background)

    #wait for keypress to go on
    titleLoop = True
    pygame.event.clear()
    WaitForKeypress([K_SPACE, K_RETURN])

    music.set_volume(0.65)

    #draw rules
    img = pygame.image.load(IMGS['rules']).convert()
    img.set_alpha(240)
    rect = CenterSurface(img, background)
    _Redraw(background, bgImg, banner, bannerPos)
    background.blit(img, rect)
    BlitToScreen(screen, background)

    #wait for keypress, then end
    WaitForKeypress([K_SPACE, K_RETURN])
    music.stop()
    pygame.time.delay(200)


#------------------------------------------------------------------ 
def _Redraw(background, bgImg, banner, bannerPos):
    """Redraw background image and banner to background"""
    background.fill((0, 0, 0))
    background.blit(bgImg, (0, 0))
    background.blit(banner, bannerPos)

    return background



