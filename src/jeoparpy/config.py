"""
config.py
Author: Adam Beagle

DESCRIPTION:
  Defines top-level constants designed to be user-customizable.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

###############################################################################
# DISPLAY SETTINGS
#=================
#
# SET DISPLAY RESOLUTION BELOW. Resolution must have a widescreen
# (16:9 or 16:10) aspect ratio.
#
# Common 16:9 resolutions:
# (1024, 576), (1280, 720), (1366, 768), (1600, 900), (1920, 1080)
#
# Common 16:10 resolutions:
# (1280, 800), (1440, 900), (1680, 1050), (1920, 1200)
#
# It is not recommended to use a resolution higher than (1920, 1200).
SCREEN_W, SCREEN_H = SCREEN_SIZE = (1280, 720)

# It is recommended to run the game with FULLSCREEN = 1
# FULLSCREEN is 0 by default in case the default resolution is not supported.
FULLSCREEN = 0

# It is not recommended to change this field unless there are
# problems running the game at this speed.
FPS_LIMIT = 100

###############################################################################
# GAME SETTINGS
#==============

# This is the time in miliseconds that players have to answer a clue
# after buzzing in. This field must be an integer.
ANSWER_TIME_MS = 5000

# If this is set to True, money is taken away when a player answers
# incorrectly. If set to False, money remains the same on a wrong answer.
SUBTRACT_ON_INCORRECT = True
