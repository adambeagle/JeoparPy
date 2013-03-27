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
from Utility import CenterSurface
from Config import JEOP_BLUE, SCREEN_H, FONTS

########################################################################
class ClueBox:
    """
    Represents box that appears when amount on
    board is clicked that contains an 'answer'
    """

    #======================================================================#
    #----------------------------- CONSTRUCTOR ----------------------------#
    #======================================================================#
    def __init__(self, pos, size, clue, boardW = -1, imgPath = None):
        """
        Constructor. Pos and size expect 2-tuple/list.
        Clue expects string from clues.txt
        ImgPath expects entire path to image (can get from IMGS constant)
        """
        self._w, self._h = self._size = size
        self._pos = [pos[0], pos[1]]
        self._boardW = boardW
        self._clue = clue
        self._imgPath = imgPath
        
        self._bg = pygame.Surface(size).convert()
        
        frameGoal = 30
        self._posSteps = self._GetPosSteps(frameGoal)
        self._scaleSteps = self._GetScaleSteps(frameGoal)
        
        self._centerx = self._pos[0] + (self._w / 2)
        self._centery = self._pos[1] + (self._h / 2)
        
        path = pygame.font.match_font(FONTS['clue'])
        self._font = pygame.font.Font(path, size[1] / 15)

        self._bg.fill(JEOP_BLUE)

    #==================================================================#
    #---------------------------- METHODS -----------------------------#
    #==================================================================#

    def StepAnimation(self):
        """
        Does one step in an opening box animation.
        Scales and alters position by amounts defined here and in _GetPosSteps
        Returns surface of entire ClueBox object, to be drawn to screen elsewhere.
        """        
        #scaleStepX = int(SCREEN_H * (24.0 / 768))
        #scaleStepY = int(SCREEN_H * (18.0 / 768))
        scaleStepX, scaleStepY = self._scaleSteps
        self._w = self._size[0] + scaleStepX
        self._h = self._size[1] + scaleStepY

        #scale bg surface to new size
        self._bg = pygame.transform.scale(self._bg, (self._w, self._h))
        self._size = (self._w, self._h)

        #change position
        sX, sY = self._posSteps
        
        self._pos[0] += sX
        self._pos[1] += sY
        
        return self._bg


    #-------------------------------------------------------------------
    def WriteClue(self):
        """
        Renders and writes clue onto background surface.
        Handles multiline clues.
        """
        clue = self._clue.splitlines()
        font = self._font
        w = h = 0
        img = None
        imgSpacer = int(SCREEN_H * (40.0 / 768))

        if self._imgPath:
            img = pygame.image.load(self._imgPath)

        #get dimensions to fit clue on new surface
        for l in clue:
            w = max(w, font.size(l)[0])
            h += font.get_linesize()

        #add height of image, if necessary
        if img:
            imgH = img.get_height()
            h += imgH + imgSpacer

        #create surface
        sfc = pygame.Surface((w, h))
        sfc.fill(JEOP_BLUE)

        #render and draw each line of clue
        h = 0
        centerx = sfc.get_rect().centerx
        for l in clue:
            x = centerx - (font.size(l)[0] / 2)
            text = font.render(l, 1, (255, 255, 255))
            shadow, shadPos = ShadowText(l, (x, h), font, 3)
            sfc.blit(shadow, shadPos)
            sfc.blit(text, (x, h))
            h += font.get_linesize()

        #draw image, if exists
        if img:
            h += imgSpacer
            x = centerx - (img.get_width() / 2)
            sfc.blit(img, (x, h))

        #place and draw surface
        textPos = CenterSurface(sfc, self._bg)
        self._bg.fill(JEOP_BLUE)
        self._bg.blit(sfc, textPos)
        

    #===================================================================#
    #------------------------ "PRIVATE" METHODS ------------------------#
    #===================================================================#
    
    #-------------------------------------------------------------------
    def _GetScaleSteps(self, numFrames):
        """"""
        sX = (self._boardW - self._w) / numFrames
        sY = (SCREEN_H - self._h) / numFrames

        return (sX, sY)


    def _GetOnePosStep(self, center, centerScr, numFrames):
    	if centerScr >= center:
    		step = (centerScr - center) / numFrames
    	else:
    		step = -1*((center - centerScr) / numFrames)
    		
    	return step
    		
    		
    #-------------------------------------------------------------------
    def _GetPosSteps(self, numFrames):
        """
        Returns shift to be made in x and y
        diretions upon animation step
        """
        x, y = self._pos
        
        sX = -1*(x / numFrames)
        sY = -1*(y / numFrames)

        return (sX, sY)

    

    #===================================================================#
    #---------------------------- PROPERTIES ---------------------------#
    #===================================================================#
    @property
    def Clue(self):
        return self._clue

    @property
    def Height(self):
        return self._h

    @property
    def Pos(self):
        return self._pos

    @property
    def Surface(self):
        return self._bg

    @property
    def Width(self):
        return self._w
