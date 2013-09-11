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
from ui import Controller, do_intro, do_scroll

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
    controller = Controller(screen, gameData)
    clock = pygame.time.Clock()

    #Intro sequence (control passed completely to functions)
    pygame.mouse.set_visible(False)
    do_intro(screen, clock)
    do_scroll(screen, clock, gameData.categories)
    pygame.mouse.set_visible(True)

    #Prep for primary loop
    gs.state = gs.WAIT_CHOOSE_CLUE
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([MOUSEBUTTONDOWN, QUIT, KEYDOWN])
    controller.draw_all(screen)

    #Primary loop
    while not gs.state == gs.GAME_END:
        #Events
        handle_events(gs)
        if gs.state == gs.QUIT:
            return

        #Update
        controller.update(gs, gameData)
        transition_state(gs)

        #Draw
        controller.draw(screen)

        #Cleanup
        pygame.event.pump()
        clock.tick_busy_loop(100)

    return
    
###############################################################################
def handle_events(gameState):
    gs = gameState
    for event in pygame.event.get():
        if event.type == QUIT:
            gs.state = gs.QUIT

        elif event.type == KEYDOWN:
            handle_key_event(gs, event)
        
def handle_key_event(gameState, event):
    gs = gameState
    
    if event.key == K_q:
        if pygame.key.get_mods() & KMOD_SHIFT:
            gs.state = gs.QUIT
        else:
            gs.state = gs.GAME_END

    if gs.state == gs.WAIT_BUZZ_IN and event.key in (K_1, K_2, K_3):
        p = event.key - K_1
        gs.state = (gs.BUZZ_IN, p)

    if event.key == K_SPACE:
        gs.state = (gs.ANSWER_CORRECT, gs.arg)
    if event.key == K_BACKSPACE:
        gs.state = (gs.ANSWER_INCORRECT, gs.arg)
    if event.key == K_END:
        gs.state = (gs.ANSWER_TIMEOUT, gs.arg)

def transition_state(gameState):
    gs = gameState
    if gs.state == gs.BUZZ_IN:
        gs.state = (gs.WAIT_ANSWER, gs.arg)

    if gs.state in gs.ANSWER:
        gs.state = gs.WAIT_PICK_CLUE
    
###############################################################################
if __name__ == '__main__':
    main()
