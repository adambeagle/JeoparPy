"""
resmaps.py
Author: Adam Beagle

DESCRIPTION:
  Provides maps that link descriptive names
  to absolute paths to resource files.

  If changes are made to resource file or folder names,
  this is the only file that needs to be updated,
  assuming the names by which the files are referred are not
  altered in this file.

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

###############################################################################
# INSTRUCTIONS TO ADD YOUR OWN IMAGES:
# To use your own image file in a clue, it must be added to IMAGES below.
#
# 1) Do NOT delete any of the existing IMAGES lines.
#    The game will not be able to run.
#
# 2) Place your image file in the <jeoparpy root>/res/images folder.
#
# 3) Take note of your image's name and file extension.
#
# 4) Add a line inside the brackets of IMAGES (located immediately below these
#    instructions) for your image. It should look very similar to the
#    existing lines, and use this format:
#        'descriptive_name' : _imgPath + 'filename.ext',
#
#    4a) Replace 'descriptive_name' with an alphanumeric name of your choosing.
#        Make sure it is surrounded by single quotes like in the other lines.
#
#    4b) Replace 'filename.ext' with exact filename and extension of the image.
#        This must also be surrounded by single (or double) quotes.
#        Only write the filename and extension; include no path information.
#
# 5) Go to config.py, in the same folder as this file, and follow the
#    instructions to add your image to a specific clue. Take note of the
#    descriptive name(s) you used for your file(s) as it/they will be required
#    in config.py to link your file to a clue.

IMAGES = {'introBG'     : _imgPath + 'introbg.png',
          'rPanelBG'    : _imgPath + 'podiabg.png',
          'podium'      : _imgPath + 'podium.png',
          'highlight'   : _imgPath + 'highlight.png',
          'lamonster'   : _imgPath + 'livvy.png',
          'test_img'    : _imgPath + 'wivtest.png',
        }

###############################################################################
# WARNING: Alter anything below at your own risk.
FONTS = {'title'    : _fontPath + 'gyparody.ttf',
         'rules'    : _fontPath + 'korinab.ttf',
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

SOUNDS = {'intro'     : _sndPath + 'intro.ogg',
          'fill'      : _sndPath + 'fill.ogg',
          'buzz'      : _sndPath + 'buzz.wav',
          'wrong'     : _sndPath + 'wrong.wav',
          'outoftime' : _sndPath + 'outoftime.wav',
          'end'       : _sndPath + 'end.ogg',
          'applause'  : _sndPath + 'applause.wav'
          }

VIDEOS = {}
