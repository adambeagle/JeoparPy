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
from Utility import CenterSurface, CreateText
from ShadowText import ShadowText
from Config import JEOP_BLUE

###################################################################
class CreditLine():	
	#/=========================================\
	#|-------------- CONSTRUCTOR --------------|
	#\=========================================/
	def __init__(self, text, size=34):
		textSfc, textPos, font = CreateText(text, 'credits', size)
		shad, shadPos = ShadowText(text, textPos, font, 4)
		
		w, h = textSfc.get_size()
		self._sfc = pygame.Surface((w + 5, h + 5))
		self._sfc.fill(JEOP_BLUE)
		self._sfcRect = pygame.Rect(0, 0, w, h)
		
		self._sfc.blit(shad, shadPos)
		self._sfc.blit(textSfc, textPos)
		
	#/=========================================\
	#|---------------- METHODS ----------------|
	#\=========================================/
	def SetCenterX(self, centerx):
		self._sfcRect.centerx = centerx
		
	def SetPos(self, x, y):
		self.SetX(x)
		self.SetY(y)
		
	def SetX(self, value):
		self._sfcRect.left = value
		
	def SetY(self, value):
		self._sfcRect.top = value
	
		
	#/=========================================\
	#|-------------- PROPERTIES ---------------|
	#\=========================================/
	@property
	def Pos(self):
		x = self._sfcRect[0]
		y = self._sfcRect[1]
		return (x, y)
	
	@property
	def SfcRect(self):
		return self._sfcRect
	
	@property
	def Surface(self):
		return self._sfc
		
	@property
	def X(self):
		return self._sfcRect.left
		
	@property
	def Y(self):
		return self._sfcRect.top
		
	#@Y.setter
	#def Y(self, value):
	#	self._sfcRect.top = value
		
		
	
