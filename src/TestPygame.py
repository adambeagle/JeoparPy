"""
Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from Config import SOUNDS

def DoSoundTest():
	pygame.init()
	snd = pygame.mixer.Sound(SOUNDS['buzz'])
	snd.play()
	pygame.time.wait(int(snd.get_length())*1000 + 1000)
	print 'sound test over'
	pygame.quit()
	return
	
	
def DoDisplayTest():
	pygame.init()
	size = (1280, 720)
	pygame.display.set_mode(size, pygame.FULLSCREEN)
	print 'display works'
	pygame.quit()
	return






###################################################################
if __name__ == '__main__':
	DoSoundTest()
	DoDisplayTest()
	raw_input('Test over. Press enter...')
	
