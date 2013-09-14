"""
intro.py
Author: Adam Beagle

DESCRIPTION:
  Functions implementing the beginning of the JeoparPy introduction sequence.
  Intro music plays, the title fades in over a background, and the subtitle
  appears. Upon pressing any key, the rules screen appears. Pressing a key
  again ends the sequence.

USAGE:
  Main should only need to call do_intro.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file..

"""

import pygame
from pygame.locals import KEYDOWN, QUIT

from constants import SUBTITLE
from resmaps import FONTS, IMAGES, SOUNDS
from util import shadow_text, wait_for_keypress

###############################################################################
def do_intro(screen, clock, audioplayer):
    """
    Draws JeoparPy title animation to screen.
    Note control of application passed completely to this function from main.
    """
    #Declarations
    scrSize = screen.get_size()
    bannerColor = (0, 0, 50)
    music = audioplayer.sounds['intro']

    background, bgRect = _build_background(scrSize)
    background.blit(*_build_banner(bgRect, bannerColor))
    rules, rulesRect = _build_rules(bgRect)
    title, titleRect = _build_title_text(bgRect, bannerColor)

    #Start intro sequence
    pygame.event.set_allowed(None)
    screen.blit(background, (0, 0))
    pygame.display.update()
    music.play()

    #Fade in title (control passed to function)
    _fade_in_title(screen, background, title, titleRect, bannerColor, clock)

    #Draw subtitle and wait for keypress
    _blit_subtitle(background, bgRect, titleRect)
    pygame.event.set_allowed([KEYDOWN, QUIT])
    _update_and_wait_for_keypress(screen, background)
    
    #Draw rules and wait for keypress
    music.set_volume(0.7)
    background.blit(rules, rulesRect)
    _update_and_wait_for_keypress(screen, background)

    music.fadeout(1000)
    pygame.time.delay(1000)
    
###############################################################################
def _update_and_wait_for_keypress(screen, background):
    screen.blit(background, (0, 0))
    pygame.display.update()
    wait_for_keypress()
    
def _blit_subtitle(background, scrRect, titleRect):
    """
    Creates subtitle and its shadow, then blits both onto background.
    'scrRect' is Rect the size of entire screen.
    'titleRect' is Rect of title text.
    """
    #Render subtitle text
    size = int(52 * (scrRect.h / 768.0))
    offset = int(20 * (scrRect.h / 768.0))
    font = pygame.font.Font(FONTS['subtitle'], size)
    text = font.render(SUBTITLE, 1, (255, 255, 255))

    #Position subtitle
    rect = text.get_rect()
    rect.centerx = scrRect.centerx
    rect.y = titleRect.bottom + offset

    #Create shadow
    shadow, shadRect = shadow_text(SUBTITLE, rect, font, 2)

    #Blit both to background
    background.blit(shadow, shadRect)
    background.blit(text, rect)

def _build_background(scrSize):
    background = pygame.image.load(IMAGES['introBG']).convert()
    background = pygame.transform.smoothscale(background, scrSize)

    return background, background.get_rect()

def _build_banner(scrRect, color):
    """
    Returns 2-tuple containing title banner surface
    and its Rect, already positioned to be drawn.
    Arguments are a pygame.Rect object the size of the screen,
    and the color of the banner.
    """
    size = (scrRect.w, int(scrRect.h * (175.0 / 768)))
    banner = pygame.Surface(size)
    banner.fill(color)
    
    rect = banner.get_rect()
    rect.centery = scrRect.centery

    return (banner, rect)

def _build_rules(scrRect):
    offset = int(50 * (scrRect.h / 768.0))
    rect = scrRect.copy()
    rect.inflate_ip(-offset, -offset)
    
    rules = pygame.image.load(IMAGES['rules']).convert()
    rules = pygame.transform.smoothscale(rules, rect.size)
    rules.set_alpha(240)

    return rules, rect

def _build_title_text(scrRect, bgColor):
    """
    Returns 2-tuple containing title text surface
    and its Rect, already positioned to be drawn.
    Arguments are a pygame.Rect object the size of the screen,
    and the background color of the text.
    """
    size = int(150 * (scrRect.h / 768.0))
    font = pygame.font.Font(FONTS['title'], size)
    
    #Note: bgColor required so set_alpha can be called on text.
    text = font.render("JeoparPy!", 1, (230, 230, 230), bgColor)

    rect = text.get_rect()
    rect.center = scrRect.center

    return (text, rect)

def _fade_in_title(screen, background, text, textRect, bannerColor, clock):
    fps_goal = int(255 / 7.8) #frames to draw / time to spend in secs

    pygame.time.delay(2000)
    for alpha in xrange(256):
        background.fill(bannerColor, textRect)
        text.set_alpha(alpha)
        background.blit(text, textRect)
        screen.blit(background, textRect, textRect)

        pygame.display.update(textRect)
        clock.tick_busy_loop(fps_goal)
        

###############################################################################
if __name__ == '__main__':
    #Test run
    pygame.init()
    screen = pygame.display.set_mode((800, 450))
    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))
    do_intro(screen, clock)
