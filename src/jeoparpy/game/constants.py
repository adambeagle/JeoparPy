"""
constants.py
Author: Adam Beagle

DESCRIPTION:
  Defines constants required by multiple game modules.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from os import path

from ..constants import ROOT_PATH

_textPath = path.join(ROOT_PATH, 'res', 'text', '')

CLUES_PATH = _textPath + 'clues.txt'
CATEGORIES_PATH = _textPath + 'categories.txt'
