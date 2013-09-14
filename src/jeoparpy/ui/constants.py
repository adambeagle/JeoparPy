"""
constants.py
Author: Adam Beagle

DESCRIPTION:
  Defines constants required by multiple ui modules and subpackages.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""
from os import path

from pygame.locals import USEREVENT

from ..constants import ROOT_PATH
from ..util import get_first_textline

_subPath = path.join(ROOT_PATH, 'res', 'text', 'subtitle.txt')

ANIMATIONEND = USEREVENT
JEOP_BLUE = (16, 26, 124) #RGB color
SUBTITLE = get_first_textline(_subPath)
