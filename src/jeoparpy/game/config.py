"""
config.py
Author: Adam Beagle

DESCRIPTION:
  Defines constants used by multiple game modules.
  Anything designed to be customizable by the user is defined here.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from os import pardir, path, sep

#Initialization; do not move or alter
_rootPath = path.abspath(path.join(path.dirname(__file__), pardir, pardir, pardir))
_textPath = path.join(_rootPath, 'res', 'text', '')

#Everything below is customizable
CLUES_PATH = _textPath + 'clues.txt'
CATEGORIES_PATH = _textPath + 'categories.txt'

AMOUNTS = (200, 400, 600, 800, 1000)
PLAYER_NAMES = ('Team 1', 'Team 2', 'Team 3')
