#!/usr/bin/python
"""
main.pyw
Author: Adam Beagle

DESCRIPTION:
  Entry point for the JeoparPy application.
  Initialization, primary game loop, and event handlers are here.
  Serves as interface between 'game' and 'ui' packages.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

import pygame
from pygame.locals import *

from config import SCREEN_SIZE, FULLSCREEN
from game import GameData, GameState
from ui import doIntro, doScroll

###############################################################################
def main():
    """Entry point."""

    #Initialization
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE,
                                     pygame.FULLSCREEN if FULLSCREEN else 0)
    pygame.display.set_caption('JeoparPy!')

    #Declarations
    gameData = GameData()
    gs = GameState()
    clock = pygame.time.Clock()

    #Intro sequence (control passed completely to functions)
    doIntro(screen, clock)
    doScroll(screen, clock, gameData.Categories)

    #Prep for primary loop
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([MOUSEBUTTONDOWN, QUIT, KEYDOWN])

    #Primary loop
    while not gs.State == gs.GAME_END:
        #Events
        handle_events(gs)
        if gs.State == gs.QUIT:
            return

        #Update
        

        #Draw

        #Cleanup
        pygame.event.pump()
        clock.tick_busy_loop(100)

    return
    
###############################################################################
def handle_events(gameState):
    gs = gameState
    for event in pygame.event.get():
        if event.type == QUIT:
            gs.State = gs.QUIT

        elif event.type == KEYDOWN:
            handle_key_event(gs, event)
        
def handle_key_event(gameState, event):
    gs = gameState
    
    if event.key == K_q:
        if pygame.key.get_mods() & KMOD_SHIFT:
            gs.State = gs.QUIT
        else:
            gs.State = gs.GAME_END
    
###############################################################################
if __name__ == '__main__':
    main()
