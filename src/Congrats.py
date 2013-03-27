"""
Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from ShadowText import ShadowText
from Utility import BlitToScreen, CreateText, CenterSurface
from Config import JEOP_BLUE

###########################################################
def DoCongrats(winner, screen, background):
	background.fill(JEOP_BLUE)
	_AnimateCongrats(screen, background)
	count = 0
	offset = 30
	
	for p in winner:
		text, rect, font = CreateText('Team ' + str(p + 1), 'team' + str(p + 1), 90)
		rect = CenterSurface(text, background)
		rect.top += 30
		
		if count > 0:
			rect.top = lastY + offset
			
		background.blit(text, rect)
		BlitToScreen(screen, background)
		lastY = rect.bottom
		count += 1
		
	pygame.time.wait(3500)
		
def _AnimateCongrats(screen, background):
	word = 'CONGRATULATIONS!'
	size = 100
	
	#get width of full word
	text, rect, font = CreateText(word, 'congrats', size)
	rect = CenterSurface(text, background)
	x = rect.left
	y = 0.3*background.get_height()
	
	for c in word:
		text, textPos, font = CreateText(c, 'congrats', size)
		textPos.topleft = (x, y)
		x += text.get_width() + 2
		
		shad, shadPos = ShadowText(c, textPos, font, 4)
		
		background.blit(shad, shadPos)
		background.blit(text, textPos)
		BlitToScreen(screen, background)
		pygame.time.wait(100)
		
		
		
###################################################################
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((1280, 720))
	background = pygame.Surface((1280, 720))
	DoCongrats([0], screen, background)
		
	
	
	
	
