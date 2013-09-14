"""
config.py
Author: Adam Beagle

DESCRIPTION:
  Defines constants used by multiple ui modules.
  Anything UI-related that is designed to be user-customizable
  is placed here.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from pygame.locals import USEREVENT


ANIMATIONEND = USEREVENT + 1
JEOP_BLUE = (16, 26, 124) #RGB color


# --Everything below is customizable--
CATEGORY_HOLD_TIME = 2500 #In miliseconds
