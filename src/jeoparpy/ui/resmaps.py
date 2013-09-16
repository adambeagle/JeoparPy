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

from os import path

from ..constants import ROOT_PATH

_fontPath = path.join(ROOT_PATH, 'res', 'fonts', '')
_imgPath = path.join(ROOT_PATH, 'res', 'images', '')
_sndPath = path.join(ROOT_PATH, 'res', 'sounds', '')
_vidPath = path.join(ROOT_PATH, 'res', 'video', '')

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
          'test'        : _imgPath + 'wivtest.png',
        }

SOUNDS = {'intro'     : _sndPath + 'intro.ogg',
          'fill'      : _sndPath + 'fill.ogg',
          'buzz'      : _sndPath + 'buzz.wav',
          'wrong'     : _sndPath + 'wrong.wav',
          'outoftime' : _sndPath + 'outoftime.wav',
          'end'       : _sndPath + 'end.ogg',
          'applause'  : _sndPath + 'applause.wav'
          }

VIDEOS = {}
