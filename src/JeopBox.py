#!/usr/bin/python
"""
Copyright (C) 2013 Adam Beagle - All Rights Reserved
You may use, distribute, and modify this code under
the terms of the GNU General Public License,
viewable at http://opensource.org/licenses/GPL-3.0

This copyright notice must be retained with any use
of source code from this file.
"""
import pygame
from pygame.locals import *
from ShadowText import ShadowText
from Utility import CreateText, CenterSurface
from Config import JEOP_BLUE

############################################################################
class JeopBox:
    """
    Represents one box on a Jeopardy board.
    Can either include a category or a dollar amount as text.
    """
    
    #======================================================================#
    #----------------------------- CONSTRUCTOR ----------------------------#
    #======================================================================#
    def __init__(self, size, isCategory=False, rightEdge=False):
        """Constructor"""
        self._w, self._h = size
        self._isCategory = isCategory
        self._bg = pygame.Surface(size)
        self._rect = self._bg.get_rect()
        self._bg.fill(JEOP_BLUE)
        self._rightEdge = rightEdge
        
        self._InitBorders()


    #==================================================================#
    #---------------------------- METHODS -----------------------------#
    #==================================================================#
    def RemoveAmount(self):
        """
        Redraws box surface with text no longer there.
        """
        self._bg.fill(JEOP_BLUE)
        self._InitBorders()

    #--------------------------------------------------------------------
    def WriteAmount(self, msg):
        """
        Write dollar amount in box.
        """
        text, textPos, font = CreateText(msg, 'amount', 48, (217, 164, 31))
        textPos = CenterSurface(text, self._bg)
        shadow, shadPos = ShadowText(msg, textPos, font, 6)
        self._bg.blit(shadow, shadPos)
        self._bg.blit(text, textPos)


    #--------------------------------------------------------------------
    def WriteCategory(self, msg):
        """
        Write category in box.
        Currently only supports two-word categories.
        """
        words = msg.split()

        for i in range(len(words)):
            word = words[i]
            text, textPos, font = CreateText(word, 'category', 36)
            textPos = CenterSurface(text, self._bg, x=1, y=0)
            
            if i == 0:
                textPos.centery = self._bg.get_rect().centery - (25 * bool(len(words) > 1))
            else:
                textPos.centery = self._bg.get_rect().centery + 15
            shadow, shadPos = ShadowText(word, textPos, font, 3)
            self._bg.blit(shadow, shadPos)
            self._bg.blit(text, textPos)


    

    #===================================================================#
    #------------------------ "PRIVATE" METHODS ------------------------#
    #===================================================================#
    def _InitBorders(self):
        borderSize = 2
        catOffset = 4
        width = self._w
        height = self._h
        category = self._isCategory
        rightEdge = self._rightEdge
        
        #draw left border
        left = pygame.Surface((borderSize, height))
        left.fill((0, 0, 0))
        self._bg.blit(left, (0, 0))

        #draw right border
        right = pygame.Surface((borderSize*(rightEdge + 1), height))
        right.fill((0, 0, 0))
        self._bg.blit(right, (self._rect.right - borderSize*(rightEdge + 1), 0))

        #draw top border
        if not category:
            top = pygame.Surface((width, borderSize))
            top.fill((0, 0, 0))
            self._bg.blit(top, (0, 0))

        #draw bottom border
        if category:
            bottom = pygame.Surface((width, borderSize + catOffset))
        else:
            bottom = pygame.Surface((width, borderSize))
        bottom.fill((0, 0, 0))
        self._bg.blit(bottom, (0, self._rect.bottom - (borderSize + category*catOffset)))
        


    #===================================================================#
    #---------------------------- PROPERTIES ---------------------------#
    #===================================================================#      
    @property
    def Surface(self):
        return self._bg

    @property
    def Width(self):
        return self._w

    @property
    def Height(self):
        return self._h

    
