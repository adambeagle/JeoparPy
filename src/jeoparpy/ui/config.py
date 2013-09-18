"""
config.py
Author: Adam Beagle

DESCRIPTION:
  Defines constants used by multiple ui modules and subpackages
  that are designed to be user-customizable.

Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.

"""

###############################################################################
#INITIALIZATION: Do not alter or move 
#====================================
MEDIA = {}
###############################################################################


# This is the time, in miliseconds, that the game holds on each
# category name during the category scroll at the start of the game.
CATEGORY_HOLD_TIME = 2500 #In miliseconds

# MEDIA INSTRUCTIONS:
# ===================
# Altering MEDIA allows the user to add an image that will display
# underneath the text of a clue.
#
#
# 1) Go to resmaps.py, located in the same folder as this file, and
#    follow the instructions to add your image file to the game's resources.
#
# 2) Add your image to MEDIA below, following this format:
#        MEDIA[(column, row)] = 'image_name'
#
#    2a) (Column, row) is the location on the game board of the desired clue.
#         Note that both are 0-based, so coordinates of the upper-left clue
#         are (0, 0). See the chart below for a visual example.
#
#    2b) 'image_name' comes from /src/jeoparpy/ui/resmaps.py.
#        It is the name the user chose in that file to refer to the image.
#        See instructions in that file on how to add your own image files.
#
#
# 3) Make sure to delete the sample MEDIA lines below
#    (those that assign 'test_img'). 
#
# For a 5x5 board, these are the (column, row) values:
#        CATEGORY | CATEGORY | CATEGORY | CATEGORY | CATEGORY
#       ----------|----------|----------|----------|----------
#         (0, 0)  |  (1, 0)  |  (2, 0)  |  (3, 0)  |  (4, 0)
#         (0, 1)  |  (1, 1)  |  (2, 1)  |  (3, 1)  |  (4, 1)
#         (0, 2)  |  (1, 2)  |  (2, 2)  |  (3, 2)  |  (4, 2)
#         (0, 3)  |  (1, 3)  |  (2, 3)  |  (3, 3)  |  (4, 3)
#         (0, 4)  |  (1, 4)  |  (2, 4)  |  (3, 4)  |  (4, 4)
#

# ALL LINES BELOW ARE SAMPLE DATA. DELETE IF CREATING YOUR OWN GAME.
MEDIA[(0, 3)] = 'test_img'
MEDIA[(1, 3)] = 'test_img'
MEDIA[(2, 3)] = 'test_img'
MEDIA[(3, 3)] = 'test_img'
MEDIA[(4, 3)] = 'test_img'
