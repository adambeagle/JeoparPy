"""
Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""

def ShadowText(msg, textPos, font, offset):
    """"""
    shadText = font.render(msg, 1, (0, 0, 0))
    pos = shadText.get_rect()
    posX = textPos[1] + offset
    posY = textPos[0] + offset
    pos.top = posX
    pos.left = posY
    return shadText, pos
