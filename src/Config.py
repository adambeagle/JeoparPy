"""
Config.py

This file includes configuration options for the game.
Users can edit the portion surrounded by asterisks below.
Instuctions for each editable element are included.


Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import sys
import os

################################################################################
# INITIALIZATION: DO NOT ALTER OR MOVE THIS SECTION

#init paths
_rootPath = os.path.dirname(os.path.abspath(__file__))

#  remove /src/ from path
_rootPath = _rootPath[:-1]
while not _rootPath[-1] == os.sep:
	_rootPath = _rootPath[:-1]

_sndPath = os.path.join(_rootPath, 'res', 'sounds', '')
_imgPath = os.path.join(_rootPath, 'res', 'images', '')
_vidPath = os.path.join(_rootPath, 'res', 'video', '')
################################################################################

#*******************************************************************************
# EVERYTHING IN THIS BLOCK CAN BE CUSTOMIZED

#Subtitle goes here, between the quotes.
#  This will appear during the intro sequence, underneath the Jeoparpy! name.
SUBTITLE = 'Sample Edition'

#Put category names here
#  Make sure all but the last row ends in a comma.
#  Short category names are recommended.
#  Please note the game is only guaranteed to look ideal with 5 category columns.
CATEGORIES = ["SAMPLE CATEGORY",
              "EXAMPLE CATEGORY",
              "MODEL CATEGORY",
              "CATEGORY SAMPLE",
              "CATEGORY EXAMPLE"
              ]

#These are the amounts that each row of questions are worth (in order)
#  Please note the game is only guaranteed to look ideal with 5 rows.
AMTS = [200, 400, 600, 800, 1000]

#To add a new image:
#  1) Make sure the image file is in res/images/
#  2) Choose any name for it in the first column.
#  3) In the last column, write the filename (including extension) of the image
#  4) Be careful about putting a comma after all rows but the last
#  5) Look below for instructions on adding image to MEDIA to place it in the right clue.
IMGS = {'introBG'     : _imgPath + 'blue_big.png',
        'rPanelBG'    : _imgPath + 'blue.png',
        'podium'      : _imgPath + 'podium.png',
        'highlight'   : _imgPath + 'highlight.png',
        'rules'       : _imgPath + 'rules.png',
        'lamonster'   : _imgPath + 'livvy.png',
        'example_img' : _imgPath + 'wivtest.png'        #example; can be removed (must remove corresponding MEDIA entries)
        }

#To add a new video:
#  WARNING: For me, adding video in Ubuntu 10 crashed the app and the OS, so I warn against adding video if you're running the game in Linux.
#  WARNING #2: Pygame documentation says video does not work in Windows, though I had issue.
#
#  1) Please note that Pygame can unfortunately only handle "basic encoded MPEG1 video files" (from the documentation).
#  2) Place video in /res/video/
#  3) Choose any name for it in the first column.
#  4) Put the filename (including extension) in the last column
#  5) Be careful about putting a comma after all rows but the last
#  6) Look below for instructions on adding video to MEDIA to place it in the right clue.
VIDEOS = {
        'example_vid' : _vidPath + 'mom_mpeg1.mpg'      #example; can be removed (must remove corresponding MEDIA entry)
        }   

#Alter this at your own risk.
#The game has only been verified to work at resolutions of 1280x720 and 1366x768
#Any non 16:9 resolution will not work; Any but the two mentioned above probably won't work.
SCREEN_W, SCREEN_H = SCREEN_SIZE = (1280, 720)

#If there is a problem with displaying fullscreen, you can change this to False.
#Otherwise, it is recommended to leave this on, as trying to move
#the game window during certain portions of the game can lead to problems.
FULLSCREEN = True


#################################################################
# DO NOT ALTER OR MOVE THIS SECTION
#init media (must be None object if no media used)
_med = []
for i in range(len(CATEGORIES) * len(AMTS)):
    _med.append(None)

MEDIA = _med
#################################################################


#MEDIA: This is used to assign an image or video to a particular clue.
#Instructions:
#  1) Make sure the media you wish to use has been declared in the IMAGES and VIDEOS sections above.
#  2) Decide what clue box number you wish your media to appear in:
#     2a. The upper left clue is 0, increasing going across.
#     2b. Sample numbering (5x5 board):
#        CATEGORY | CATEGORY | CATEGORY | CATEGORY | CATEGORY
#            0    |     1    |     2    |     3    |    4
#            5    |     6    |     7    |     8    |    9
#            10   |     11   |     12   |     13   |    14
#            15   |     16   |     17   |     18   |    19
#            20   |     21   |     22   |     23   |    24
#
#  3) Using the name you chose for the media in the first column of IMAGES or VIDEOS, add a line below using the following format:
#       MEDIA[clue #] = 'name'
MEDIA[9] = 'example_img'
MEDIA[10] = 'example_img'
MEDIA[11] = 'example_img'
MEDIA[12] = 'example_img'
MEDIA[13] = 'example_img'
MEDIA[15] = 'example_vid' #REMOVE FOR LINUX: See warning in Videos section above
#*******************************************************************************





################################################################################
# EVERYTHING BELOW SHOULD NOT NEED TO BE CHANGED

#choose clues file  (OS-dependent)
if sys.platform.startswith('linux'):
    _fName = 'clues_linux.txt'
elif sys.platform.startswith('win32'):
    _fName = 'clues_win32.txt'
    
CLUES_PATH = os.path.join(_rootPath, 'res', 'misc', _fName)

JEOP_BLUE = (16, 26, 124)

SOUNDS = {'intro'     : _sndPath + 'intro.ogg',
          'fill'      : _sndPath + 'fill.ogg',
          'buzz'      : _sndPath + 'buzz.wav',
          'wrong'     : _sndPath + 'wrong.wav',
          'outoftime' : _sndPath + 'outoftime.wav',
          'end'       : _sndPath + 'end.ogg',
          'applause'  : _sndPath + 'applause.wav'
          }

#init non-OS-dependent fonts
FONTS = {'title'    : 'gyparody',
         'category' : 'impact',
         'amount'   : 'impact',
         'team3'    : 'mistral',
         'congrats' : 'gyparody'
         }

#init OS-dependent fonts
#  if adding fonts, check name from pygame.font.get_fonts()
if sys.platform.startswith('win32'):
    FONTS['team1']    = 'freestyle script'
    FONTS['team2']    = 'bradley hand itc'
    FONTS['score']    = 'korinna-extrabold'
    FONTS['clue']     = 'korinna'
    FONTS['subtitle'] = 'lucida sans unicode'
elif sys.platform.startswith('linux'):
    FONTS['team1']     = 'freestylescript'
    FONTS['team2']     = 'bradleyhanditc'
    FONTS['score']     = 'korinnaextrabold'
    FONTS['clue']      = 'korinna'
    FONTS['subititle'] = 'lucidasansunicode'
    FONTS['credits']   = 'korinna'
    
