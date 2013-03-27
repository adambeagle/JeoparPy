#!/usr/bin/python
"""
Main.py

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from pygame.locals import *
from MainGame import MainGame
from Intro import DoIntro
from CategoryScroll import DoScroll
from Credits import DoCredits
from Congrats import DoCongrats
from ShowVideo import PlayVideo
from Utility import BlitToScreen
from Constants import SCREEN_SIZE, JEOP_BLUE, SOUNDS

########################################################################
def BlitSfcToScreen(screen, background, sfc, pos=(0, 0)):
    """Blit a surface to the screen."""
    background.blit(sfc, pos)
    BlitToScreen(screen, background)
    

########################################################################
def HandleKey(event, gameScn, background, screen, openClue=False):
    """Handles KEYDOWN event."""

    #If clue open, allow buzz in or end
    if openClue:
        player = -1
        
        if event.key == K_1:
            player = 0
        elif event.key == K_2:
            player = 1
        elif event.key == K_3:
            player = 2
        elif event.key == K_END:
            snd = pygame.mixer.Sound(SOUNDS['outoftime'])
            snd.play()
            pygame.time.wait(800)
            return False

        if player >= 0:
            return gameScn.BuzzIn(player, background, screen)

    return True


########################################################################
def Main():
    """Entry point"""
    
    #Initialization
    pygame.init()
    
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
    pygame.display.set_caption('JeoparPy!')
    background = pygame.Surface(SCREEN_SIZE)
    pygame.event.set_allowed([MOUSEBUTTONDOWN, QUIT, KEYDOWN])
    pygame.mouse.set_visible(0)

    #Intro 
    DoIntro(screen, background)

    #Category scroll
    DoScroll(screen, background)

    #Init Main Game
    gameScn = MainGame()
    
    #Blit everything to the screen
    BlitSfcToScreen(screen, background, gameScn.Surface)

    #Animate Board Fill
    pygame.time.wait(1000)
    gameScn.AnimateBoardFill(background, screen)
    pygame.event.clear()
    pygame.mouse.set_visible(1)

    #init clock (used for fps limiting)
    clock = pygame.time.Clock()
    
    gameDone = False
    modMask = KMOD_SHIFT
    
    #Main game loop
    while not gameDone:
    
        background.fill(JEOP_BLUE)

        #Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
                
            if event.type == KEYDOWN and event.key == K_q:
            	if pygame.key.get_mods() & KMOD_SHIFT:
            		return
                
            if event.type == KEYDOWN and event.key == K_q:
            	gameDone = True

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                gameScn.HandleMouseClick(event.pos)

        #Draw main game screen
        openClue = gameScn.DrawAll()
        BlitSfcToScreen(screen, background, gameScn.Surface)

        #Play video clue if necessary
        if openClue and gameScn.Video:
            pygame.event.set_allowed([QUIT])
            PlayVideo(screen, gameScn.Video, gameScn.BoardWidth, SCREEN_SIZE[1])
            BlitSfcToScreen(screen, background, gameScn.Surface)
            pygame.event.set_allowed([MOUSEBUTTONDOWN, QUIT, KEYDOWN])

        #Open clue loop (wait for buzz-in or end)
        while openClue:
            evt = pygame.event.wait()
            if evt.type == KEYDOWN:
                openClue = HandleKey(evt, gameScn, background, screen, True)

            #If all players guessed incorrectly, exit loop
            if len(gameScn.BuzzedIn) == 3:
                openClue = False
                
            #make mouse visible again if going back to game board
            if not openClue:
                pygame.mouse.set_visible(1)

        #Clean up before loop restart
        gameScn.ClearBuzzedIn()
        pygame.event.pump()
        clock.tick_busy_loop(50)
    
    pygame.mouse.set_visible(0)
    music = pygame.mixer.Sound(SOUNDS['end'])
    applause = pygame.mixer.Sound(SOUNDS['applause'])
    alpha = 0
    fade = pygame.Surface(SCREEN_SIZE)
    fade.fill(JEOP_BLUE)
    while alpha < 255:
    	fade.set_alpha(alpha)
    	gameScn.DrawAll()
    	screen.blit(gameScn.Surface, (0, 0))
    	screen.blit(fade, (0, 0))
    	pygame.display.flip()
    	alpha += 2
    	
    winner = gameScn.Winner
    applause.play()
    DoCongrats(winner, screen, background)
    music.play()
    DoCredits(screen, background)
    music.stop()
    

    
    
########################################################################
if __name__ == '__main__':
    Main()
