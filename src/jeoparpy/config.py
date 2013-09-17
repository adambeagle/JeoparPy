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

# SET DISPLAY RESOLUTION BELOW. Resolution must be 16:9 aspect ratio.
# Reccomended common 16:9 resolutions:
# (640, 360), (854, 480), (960, 540), (1024, 576),
# (1280, 720), (1366, 768), (1600, 900), (1920, 1080)
#
# It is not recommended to use a resolution higher than (1920, 1080).
SCREEN_W, SCREEN_H = SCREEN_SIZE = (1280, 720)

# It is recommended to run the game with FULLSCREEN = 1
# FULLSCREEN is 0 by default in case the default resolution is not supported.
FULLSCREEN = 0


# It is not recommended to change this field unless there are
# problems running the game at this speed.
FPS_LIMIT = 100
