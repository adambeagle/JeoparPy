"""
resmaps.py
Author: Adam Beagle

DESCRIPTION:
  Provides maps that link descriptive names
  to absolute paths to resource files.

  If changes are made to resource file or folder names,
  this is the only file that needs to be updated.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

from os import path, pardir

from ..util import get_first_textline

_rootPath = path.abspath(path.join(path.dirname(__file__), pardir, pardir, pardir))

_fontPath = path.join(_rootPath, 'res', 'fonts', '')
_imgPath = path.join(_rootPath, 'res', 'images', '')
_sndPath = path.join(_rootPath, 'res', 'sounds', '')
_subPath = path.join(_rootPath, 'res', 'text', 'subtitle.txt')
_vidPath = path.join(_rootPath, 'res', 'video', '')



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

#Note 9/11 Though SUBTITLE is not a map to a path like everything else
# defined here I'm placing it here for the following reasons:
#   * Paths need only be dealt with in this file
#   * SUBTITLE only reads from file, not customized within the .py like
#     the things defined in config.py
#   * Though SUBTITLE itself is not a map to a resource,
#     a resource is read to retrieve it, so it arguably fits here.
SUBTITLE = get_first_textline(_subPath)

VIDEOS = {}
