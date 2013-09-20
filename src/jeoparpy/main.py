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

from config import FPS_LIMIT, FULLSCREEN, SUBTRACT_ON_INCORRECT, SCREEN_SIZE
from game import GameData, JeopGameState
from ui import (ANIMATIONEND, Controller, do_congrats,
                do_credits, do_intro, do_scroll)

EVENTS_ALLOWED = (ANIMATIONEND, KEYDOWN, MOUSEBUTTONDOWN, QUIT)

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
    gs = JeopGameState()
    uicontroller = Controller(screen, gameData, FPS_LIMIT)
    clock = pygame.time.Clock()

    #Intro sequence (control passed completely to functions)
    pygame.mouse.set_visible(False)
    do_intro(screen, clock, uicontroller.audioplayer)
    do_scroll(screen, clock, gameData.categories)
    pygame.mouse.set_visible(True)

    #Prep for primary loop
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(EVENTS_ALLOWED)
    uicontroller.draw(screen)
    gs.state = gs.BOARD_FILL

    #Primary loop
    while not gs.state == gs.GAME_END:
        #Events
        handle_events(gs, gameData, uicontroller)
        if gs.state == gs.QUIT:
            return

        #Update
        uicontroller.update(gs, gameData)
        transition_state(gs, gameData, uicontroller)

        #Draw
        uicontroller.draw(screen)

        #Cleanup
        pygame.event.pump()
        clock.tick_busy_loop(FPS_LIMIT)

    #Post game: Congratulations screen and credits
    pygame.mouse.set_visible(0)
    do_congrats(screen, clock, gameData.winners, uicontroller.audioplayer)
    do_credits(screen, clock, uicontroller.audioplayer, FPS_LIMIT)
    
###############################################################################
def handle_events(gameState, gameData, uicontroller):
    gs = gameState
    for event in pygame.event.get():
        if event.type == QUIT:
            gs.state = gs.QUIT

        elif event.type == KEYDOWN:
            handle_event_key(event, gameState, gameData)

        elif event.type == MOUSEBUTTONDOWN:
            handle_event_mousebuttondown(event, gameState, uicontroller)

        elif event.type == ANIMATIONEND:
            handle_event_animationend(event, gameState)

def handle_event_animationend(event, gameState):
    gs = gameState

    if gs.state == gs.WAIT_BOARD_FILL:
        gs.state = gs.WAIT_CHOOSE_CLUE

    elif gs.state == gs.WAIT_CLUE_OPEN:
        gs.state = (gs.CLUE_OPEN, gs.arg)
        
def handle_event_key(event, gameState, gameData):
    gs = gameState
    
    if event.key == K_q:
        if pygame.key.get_mods() & KMOD_SHIFT:
            gs.state = gs.QUIT
        else:
            gs.state = gs.GAME_END

    elif gs.state == gs.WAIT_TRIGGER_AUDIO and event.key == K_m:
        pygame.event.set_allowed(EVENTS_ALLOWED)
        gs.state = (gs.PLAY_CLUE_AUDIO, gs.arg)

    elif gs.state == gs.WAIT_BUZZ_IN and event.key in (K_1, K_2, K_3):
        p = event.key - K_1
        if not gameData.players[p].hasAnswered:
            gs.state = (gs.BUZZ_IN, (p, gs.arg))
            
    elif gs.state == gs.WAIT_BUZZ_IN and event.key == K_END:
        gs.state = gs.ANSWER_TIMEOUT

    elif gs.state == gs.WAIT_ANSWER:
        if event.key == K_SPACE:
            gs.state = (gs.ANSWER_CORRECT, gs.arg)
            gameData.players[gs.arg[0]].score += gs.arg[1]
        elif event.key == K_BACKSPACE:
            gs.state = (gs.ANSWER_INCORRECT, gs.arg)
            if SUBTRACT_ON_INCORRECT:
                gameData.players[gs.arg[0]].score -= gs.arg[1]

def handle_event_mousebuttondown(event, gameState, uicontroller):
    gs = gameState

    if gs.state == gs.WAIT_CHOOSE_CLUE and event.button == 1:
        clueCoords = uicontroller.get_clicked_clue(event.pos)

        if clueCoords:
            pygame.mouse.set_visible(0)
            gs.state = (gs.CLICK_CLUE, clueCoords)

def transition_state(gameState, gameData, uicontroller):
    gs = gameState

    if gs.state == gs.BOARD_FILL:
        gs.state = gs.WAIT_BOARD_FILL

    elif gs.state == gs.CLICK_CLUE:
        gs.state = (gs.WAIT_CLUE_OPEN, gs.arg)
        
    elif gs.state == gs.CLUE_OPEN:
        if uicontroller.clue_has_audio_reading(gs.arg):
            gs.state = (gs.WAIT_CLUE_READ, gs.arg)
            pygame.event.set_allowed(None)
        elif uicontroller.clue_is_audioclue(gs.arg):
            gs.state = (gs.WAIT_TRIGGER_AUDIO, gs.arg)
        else:
            gs.state = (gs.WAIT_BUZZ_IN, gameData.amounts[gs.arg[1]])

    elif gs.state == gs.WAIT_CLUE_READ:
        if not pygame.mixer.get_busy():
            pygame.event.set_allowed(EVENTS_ALLOWED)
            if uicontroller.clue_is_audioclue(gs.arg):
                gs.state = (gs.PLAY_CLUE_AUDIO, gs.arg)
            else:
                gs.state = (gs.WAIT_BUZZ_IN, gameData.amounts[gs.arg[1]])

    elif gs.state == gs.PLAY_CLUE_AUDIO:
        gs.state = (gs.WAIT_BUZZ_IN, gameData.amounts[gs.arg[1]])
        
    elif gs.state == gs.BUZZ_IN:
        gs.state = (gs.WAIT_ANSWER, gs.arg)

    elif gs.state in (gs.ANSWER_CORRECT, gs.ANSWER_TIMEOUT, gs.ANSWER_NONE):
        gameData.clear_players_answered()
        
        if gs.state == gs.ANSWER_CORRECT:
            gs.state = gs.DELAY
        else:
            pygame.mouse.set_visible(1)
            gs.state = gs.WAIT_CHOOSE_CLUE

    elif gs.state == gs.ANSWER_INCORRECT:
        gameData.players[gs.arg[0]].hasAnswered = True

        if gameData.allPlayersAnswered:
            gs.state = gs.ANSWER_NONE
        else:
            gs.state = (gs.WAIT_BUZZ_IN, gs.arg[1])

    elif gs.state == gs.DELAY:
        pygame.mouse.set_visible(1)
        gs.state = gs.WAIT_CHOOSE_CLUE
