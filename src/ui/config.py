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

from os import pardir, path, sep

###############################################################################
def _readSubtitleFromFile(path):
    """
    Returns first line with any non-whitespace text from file in passed path,
    or an empty string if no line found.
    """
    subtitle = ''

    with open(path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if len(stripped) > 0:
                subtitle = stripped
                break

    return subtitle

###############################################################################
#Initialization - DO NOT MOVE OR ALTER
_rootPath = path.abspath(path.join(path.dirname(__file__), pardir, pardir))

_fontPath = path.join(_rootPath, 'res', 'fonts', '')
_imgPath = path.join(_rootPath, 'res', 'images', '')
_sndPath = path.join(_rootPath, 'res', 'sounds', '')
_subPath = path.join(_rootPath, 'res', 'text', 'subtitle.txt')
_vidPath = path.join(_rootPath, 'res', 'video', '')
###############################################################################

#--Everything below is customizable--

SUBTITLE = _readSubtitleFromFile(_subPath)

FONTS = {'title'    : _fontPath + 'gyparody.ttf',
         'category' : _fontPath + 'impact.ttf',
         'amount'   : _fontPath + 'impact.ttf',
         'congrats' : _fontPath + 'gyparody.ttf',
         'team1'    : _fontPath + 'team1.ttf',
         'team2'    : _fontPath + 'team2.ttf',
         'team3'    : _fontPath + 'team3.ttf',
         'score'    : _fontPath + 'korinna-extrabold.ttf',
         'clue'     : _fontPath + 'korinab.ttf',
         'subtitle' : _fontPath + 'impact.ttf',
         'credits'  : _fontPath + 'korinab.ttf'
        }

IMAGES = {'introBG'     : _imgPath + 'blue_big.png',
          'rPanelBG'    : _imgPath + 'blue.png',
          'podium'      : _imgPath + 'podium.png',
          'highlight'   : _imgPath + 'highlight.png',
          'rules'       : _imgPath + 'rules.png',
          'lamonster'   : _imgPath + 'livvy.png',
          'uggie'       : _imgPath + 'uggie.jpg',
          'presley'     : _imgPath + 'presley.jpg',
        }

SOUNDS = {'intro'     : _sndPath + 'intro.ogg',
          'fill'      : _sndPath + 'fill.ogg',
          'buzz'      : _sndPath + 'buzz.wav',
          'wrong'     : _sndPath + 'wrong.wav',
          'outoftime' : _sndPath + 'outoftime.wav',
          'end'       : _sndPath + 'end.ogg',
          'applause'  : _sndPath + 'applause.wav'
          }

CATEGORY_HOLD_TIME = 2500 #In miliseconds
JEOP_BLUE = (16, 26, 124) #RGB color
