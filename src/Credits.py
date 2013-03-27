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
from Utility import BlitToScreen, CenterSurface, CreateText
from ShadowText import ShadowText
from CreditLine import CreditLine
from Config import JEOP_BLUE, IMGS

###################################################################


def DoCredits(screen, background):
        #declarations
	positions = """Programmer/Designer
Research
Research Assistant
Writer
Writing Consultant
Legal Counsel
Play Testers
~ 
Executive in 
~Charge of Play Testing
Executive in Charge of
~Chocolate Dipped Peanuts
Video/Photo Test Model
Assistant to Ms. Madill
Assistant to Mr. Madill
"""

	names = """Adam Beagle
Claire Madill
Starla 'Kitty Kitty' Warla
Adam Beagle
Claire Madill
Claire Madill
Lori Madill
~Gary Madill
Toulouse 'Woosy' Madill
~ 
Adam Beagle
~ 
Livvy Lamont
Giselle 'Zelly Poo Poo' Madill
Presley 'Chadwick' Madill
"""
	clock = pygame.time.Clock()
	w, h = background.get_size()
	posX = int(w * .19)
	nameX = int(w * .6)
	centerX = background.get_rect().centerx
	names = names.splitlines()
	positions = positions.splitlines()
	move = 3
	
	s = "CREDITS"
	topLine = CreditLine(s, 40)
	topLine.SetY(h)
	topLine.SetCenterX(centerX)

	#init lines
	nameLines, posLines = _CreateNameAndPosLines(names, positions, nameX, posX, h, 140)
	lineH = nameLines[0].Surface.get_height()
	stop = -1*lineH
	
	#scroll credits
	while nameLines[-1].Y > stop:
		background.fill((JEOP_BLUE))
		
		#draw top line
		if topLine.Y > stop:
			topLine.SetY(topLine.Y - move)
			background.blit(topLine.Surface, topLine.SfcRect)
			
		for i in range(len(nameLines)):
			if nameLines[i].Y > stop:
				nameLines[i].SetY(nameLines[i].Y - move)
				posLines[i].SetY(posLines[i].Y - move)
				background.blit(nameLines[i].Surface, nameLines[i].SfcRect)
				background.blit(posLines[i].Surface, posLines[i].SfcRect)
			
		BlitToScreen(screen, background)
		clock.tick_busy_loop(45)
		
		
	#init final lines
	text="""Catering by
~Mancinos of Alpena, MI
Brought to you by
~Lamonster Synergy e-Solutions, Inc."""
	finalLines = _CreateFinalLines(text.splitlines(), centerX, h, 180)
	img = pygame.image.load(IMGS['lamonster']).convert()
	iW, iH = img.get_size()
	img = pygame.transform.scale(img, (int(.5*iW), int(.5*iH)))
	imgRect = img.get_rect()
	imgRect.centerx = centerX
	imgRect.top = finalLines[-1].SfcRect.bottom + 20
	
	#scroll final lines
	while imgRect.bottom > 0:
		background.fill(JEOP_BLUE)
		
		for l in finalLines:
			if l.SfcRect.bottom > 0:
				l.SetY(l.Y - move)
				background.blit(l.Surface, l.SfcRect)
				
		imgRect.top -= move
		background.blit(img, imgRect)
	
		BlitToScreen(screen, background)
		clock.tick_busy_loop(45)
		
	text, textPos, font = CreateText('Thanks for playing!', 'credits', 40)
	textPos = CenterSurface(text, background)
	shad, shadPos = ShadowText('Thanks for playing!', textPos, font, 3)
	
	background.blit(shad, shadPos)
	background.blit(text, textPos)
	BlitToScreen(screen, background)
	pygame.time.delay(4000)

        alpha = 0
        fade = pygame.Surface(background.get_size())
        fade.fill((0, 0, 0))
	while alpha < 255:
    	    fade.set_alpha(alpha)
    	    screen.blit(background, (0, 0))
    	    screen.blit(fade, (0, 0))
    	    pygame.display.flip()
    	    alpha += 4

	
		
	
			
	
#-----------------------------------------------------------------
def _CreateFinalLines(text, centerx, h, offset):
	lines = []
	for i in range(len(text)):
		continued = False
		s = text[i]
		
		if s[0] == '~':
			continued = True
			s = s[1:]
		
		lines.append(CreditLine(s))
		lines[-1].SetCenterX(centerx)
		
		#if normal line
		if not continued:
			lines[-1].SetY(h + offset*(i))
		else:
			lineH = lines[-1].Surface.get_height()
			lines[-1].SetY(h + offset*(i-1) + lineH + 5)
			
	return lines
			
			
			
	
		
#-----------------------------------------------------------------	
def _CreateNameAndPosLines(names, positions, nameX, posX, h, offset):
	nameLines = []
	posLines = []

	for i in range(len(names)):
		continued = False
		name = names[i]
		pos = positions[i]
		
		if name[0] == '~':
			continued = True
			name = name[1:]
			pos = pos[1:]
			
		nameLines.append(CreditLine(name))
		posLines.append(CreditLine(pos))
		
		#if normal line
		if not continued:
			nameLines[-1].SetPos(nameX, h + offset*(i + 1))
			posLines[-1].SetPos(posX, h + offset*(i + 1))
			
		#if continued line
		else:
			lineH = nameLines[-1].Surface.get_height()
			nameLines[-1].SetPos(nameX, h + offset*i + lineH + 5)
			posLines[-1].SetPos(posX, h + offset*i + lineH + 5)
		
		
		
	return nameLines, posLines
			
		
	
	
###################################################################
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((1280, 720))
	background = pygame.Surface((1280, 720))
	DoCredits(screen, background)
    







