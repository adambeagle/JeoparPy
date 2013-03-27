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
from Config import IMGS


########################################################################
class RightPanel:
    """
    Represents entire panel to the right of the game board in Jeopardy.
    Includes a background image and 3 team podia.
    Handles drawing team names and scores.
    """

    #======================================================================#
    #----------------------------- CONSTRUCTOR ----------------------------#
    #======================================================================#
    def __init__(self, size):
        """Constructor"""
        self._bg = pygame.Surface(size)
        

        self._bgImg = pygame.image.load(IMGS['rPanelBG']).convert()
        self._bgImg = pygame.transform.scale(self._bgImg, size)
        
        self._podImg = pygame.image.load(IMGS['podium']).convert_alpha()
        self._highlightImg = pygame.image.load(IMGS['highlight']).convert_alpha()
        
        if size[1] < 768:
        	ratio = size[1] / 768.0
        	oldImgSize = self._podImg.get_size()
        	w, h = int(round(oldImgSize[0] * ratio)), int(round(oldImgSize[1] * ratio))
        	self._podImg = pygame.transform.scale(self._podImg, (w, h)).convert_alpha()
        	self._highlightImg = pygame.transform.scale(self._highlightImg, (w, h)).convert_alpha()

        self._scores = [0, 0, 0]

        self.DrawAll()


    #==================================================================#
    #---------------------------- METHODS -----------------------------#
    #==================================================================#
    def AddScore(self, player, score):
        """Adds passed score to player's existing score"""
        self._scores[player] += score

    #------------------------------------------------------------------------
    def DrawAll(self):
        """
        Draw all right panel items to this object's background.
        Entire panel can then be drawn to screen elsewhere using Surface property.
        """
        self._DrawBackground()
        self._DrawPodia()
        self._DrawScores()
        self._DrawTeams()
        

    #------------------------------------------------------------------------
    def SetHighlight(self, player, on = 0):
        """
        Draws ring-in highlight to player's podium if 'on',
        or restores panel to normal state
        """
        if on:
            self._DrawHighlight(player)
        else:
            self.DrawAll()


    #===================================================================#
    #------------------------ "PRIVATE" METHODS ------------------------#
    #===================================================================#
    def _DrawBackground(self):
        self._bg.blit(self._bgImg, (0, 0))

        
    #------------------------------------------------------------------------
    def _DrawHighlight(self, player):
        x = self._bg.get_rect().centerx - (self._highlightImg.get_width() / 2)
        h = self._highlightImg.get_height()
        
        offset1 = int(self._highlightImg.get_height() * (12.0 / 234.0))
        offset2 = int(self._highlightImg.get_height() * (16.0 / 234.0))
        
        y = offset1 + h*player + player*offset2

        self._bg.blit(self._highlightImg, (x, y))

        
    #------------------------------------------------------------------------
    def _DrawPodia(self):
        x = self._bg.get_rect().centerx - (self._podImg.get_width() / 2)
        h = self._podImg.get_height()
        
        offset1 = int(h * (12.0 / 234.0))
        offset2 = int(h * (16.0 / 234.0))
        
        for i in range(3):
            y = offset1 + h*i + i*offset2
            self._bg.blit(self._podImg, (x, y))

            
    #------------------------------------------------------------------------
    def _DrawScores(self):
        offset1 = int(self._bg.get_height() * (66.0 / 768))
        offset2 = int(self._bg.get_height() * (16.0 / 768))

        for i in range(3):
            score = "$" + str(self._scores[i])
            text, textPos, font = CreateText(score, 'score', 32)
            
            textPos = CenterSurface(text, self._bg, x=1, y=0)
            textPos.centery = offset1 + (i*self._podImg.get_height()) + i*offset2
            
            shadow, shadPos = ShadowText(score, textPos, font, 2)
            self._bg.blit(shadow, shadPos)
            self._bg.blit(text, textPos)


    #------------------------------------------------------------------------
    def _DrawTeams(self):
        """Draws team names on podia"""
        fonts = [('team1', 45), ('team2', 28), ('team3', 40)]
        offset1 = int(round(self._bg.get_height() * (160.0 / 768)))
        offset2 = int(round(self._bg.get_height() * (16.0 / 768)))

        for i in range(3):
            team = "Team " + str(i + 1)
            text, textPos, font = CreateText(team, fonts[i][0], fonts[i][1], bold=bool(i == 1))
            textPos = CenterSurface(text, self._bg, x=1, y=0)
            textPos.centery = offset1 + (i*self._podImg.get_height()) + i*offset2
            self._bg.blit(text, textPos)
            
      
    #=====================================================================#
    #---------------------------- PROPERTIES -----------------------------#
    #=====================================================================#
    @property
    def Scores(self):
    	return self._scores
    	
    @property
    def Surface(self):
        return self._bg
