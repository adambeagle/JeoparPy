"""
Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from Config import VIDEOS

def PlayVideo(screen, vidStr, maxW, maxH):
    """
    Plays a video in its original size in the center
    of region defined by top left corner and (maxW, maxH).
    Note video will be scaled if larger than (maxW, maxH)
    """
    pygame.time.wait(1000)                          #added for Jeopardy video clue

    #must quit mixer PRIOR to creating Movie object for video sound
    pygame.mixer.quit()                             
    vid = pygame.movie.Movie(VIDEOS[vidStr])
    
    #center video in specific region of screen
    #   in case of Jeopardy, keep it within the clue size
    bounding = pygame.Rect(0, 0, maxW, maxH)
    w, h = vid.get_size()
    w = min((w, maxW))
    h = min((h, maxH))
        
    rect = pygame.Rect(0, 0, w, h)
    rect.center = bounding.center

    #play video, wait until finished
    #note video automatically scales to rect size
    vid.set_display(screen, rect)
    vid.play()
    pygame.time.wait(int(vid.get_length() * 1000))
    vid.stop()

    #clean up
    vid = None
    pygame.mixer.init()
    
