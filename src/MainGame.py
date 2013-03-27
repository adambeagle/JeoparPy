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
from random import randint
from JeopBox import JeopBox
from RightPanel import RightPanel
from ClueBox import ClueBox
from Utility import BlitToScreen
from Config import *


########################################################################
class MainGame:
    """Represents primary Jeopardy game screen, with clue board and podia"""
    
    #======================================================================#
    #----------------------------- CONSTRUCTOR ----------------------------#
    #======================================================================#
    def __init__(self):
	ratio = 1050.0 / 1366.0
        self._board_w = int(SCREEN_W * ratio)
        self._divsX = len(CATEGORIES)
        self._divsY = len(AMTS) + 1
        self._box_w = self._board_w / self._divsX
        self._box_h = SCREEN_H / self._divsY
        self._bg = pygame.Surface(SCREEN_SIZE).convert()
        self._rPanel = RightPanel((SCREEN_W - self._board_w, SCREEN_H))
        self._boxCoords = []
        self._boxes = []
        self._openClueBox = None
        self._animateClue = False
        self._clues = []
        self._prevAmt = 0
        self._buzzedIn = []
        self._currentMedia = None
        self._sounds = self._CreateSounds()

        self._CreateBoxes()
        self._ParseClues()
        self.DrawAll()
        


    #==================================================================#
    #---------------------------- METHODS -----------------------------#
    #==================================================================#
    def AddScore(self, player, score):
        """
        Add amount in 'score' to the score of 'player.'
        Player represented as index
        """
        self._rPanel.AddScore(player, score)
        self._prevAmt = 0


    #-----------------------------------------------------------------
    def AnimateBoardFill(self, background, screen):
        left = range(self._divsX*(self._divsY - 1))
        fill = self._sounds['fill']
        fill.play()

        #compensate for sound delay
        pygame.time.wait(50)

		#choose random box to fill, draw amount, repeat until board full
        while len(left) > 0:
            i = -1
            while i not in left:
                i = randint(0, max(left))
            left.remove(i)
            i += self._divsY - 1
            self._boxes[i].WriteAmount('$' + str(AMTS[(i / 5) - 1]))
            self._DrawBoxes()
            background.blit(self._bg, (0, 0))
            BlitToScreen(screen, background)
            pygame.time.wait(135)


    #-----------------------------------------------------------------
    def BuzzIn(self, player, background, screen):
        """
        Buzzes player in, draws highlight on podium, waits for 
        key input specifying result of answer.
        Returns bool telling Main whether or not to wait for another buzz-in.
        """
        if not player in self._buzzedIn:
            self._sounds['buzz'].play()
            
            self._buzzedIn.append(player)
            wait = True
            self._rPanel.SetHighlight(player, True)
            self._DrawRightPanel()
            background.blit(self.Surface, (0, 0))
            BlitToScreen(screen, background)

            while wait:
                evt = pygame.event.wait()
                if evt.type == KEYDOWN:

                    #correct answer
                    if evt.key == K_SPACE:
                        self.AddScore(player, self.PrevAmt)
                        self._rPanel.SetHighlight(player, False)
                        self._DrawRightPanel()
                        background.blit(self.Surface, (0, 0))
                        BlitToScreen(screen, background)
                        pygame.time.wait(500)
                        return False

                    #incorrect answer
                    if evt.key == K_BACKSPACE:
                        self._sounds['wrong'].play()
                        self._rPanel.SetHighlight(player, False)
                        self._DrawRightPanel()
                        background.blit(self.Surface, (0, 0))
                        BlitToScreen(screen, background)
                        pygame.time.wait(500)
                        return True

                    #leave clue
                    if evt.key == K_END:
                        self._rPanel.SetHighlight(player, False)
                        return False
                        

        return True


    #-----------------------------------------------------------------
    def ClearBuzzedIn(self):
        self._buzzedIn = []

        
    #-----------------------------------------------------------------
    def DrawAll(self):
        wait = False
        skip = self._openClueBox and not self._animateClue
        
        if not skip:
            self._DrawBackground()
            self._DrawBoxes()
            
        if not self._openClueBox == None:
            wait = self._DrawClue()            

        self._DrawRightPanel()

        return wait


    #-----------------------------------------------------------------
    def HandleMouseClick(self, pos):
        top = self._boxCoords[self._divsX][1]
        
        #if click anywhere but on a clickable box, or clue box already open, return
        if pos[0] > self._board_w or pos[1] < top or not self._openClueBox == None:
            return

        self._frames = 0
        pygame.mouse.set_visible(0)

		#find which box clicked, and set all class variables accordingly
        boxI = self._FindClickedBox(pos)
        self._currentMedia = MEDIA[boxI - 5]
        self._openClueBox = ClueBox(self._boxCoords[boxI],
                                 (self._box_w, self._box_h),
                                    self._clues[boxI - self._divsX],
                                    boardW = self._board_w)
        self._animateClue = True
        self._boxes[boxI].RemoveAmount()
        
        amtsI = (boxI - 5) / 5
        self._prevAmt = AMTS[amtsI]

        
        
    #===================================================================#
    #------------------------ "PRIVATE" METHODS ------------------------#
    #===================================================================#
    def _CreateBoxes(self):
        """Init Jeopbox objects array and boxCoords"""
        #w = self._board_w / self._divsX
        #h = SCREEN_H / self._divsY
        size = (self._box_w, self._box_h)
                                 
        for r in range(self._divsY):
            for c in range(self._divsX):
                self._boxes.append(JeopBox(size, bool(r == 0), bool(c == self._divsX - 1)))
                if r == 0:
                    self._boxes[-1].WriteCategory(CATEGORIES[c])
                else:
                	#uncomment this if not calling AnimateBoardFill
                    #self._boxes[-1].WriteAmount('$' + str(AMTS[r - 1]))
                    pass

                self._boxCoords.append((self._box_w * c, self._box_h * r))


    #-----------------------------------------------------------------
    def _ParseClues(self):
        f = open(CLUES_PATH, 'r')
        clues = ['']

        for line in f:
            if not line == "\n":
                clues[-1] += line
            else:
                if not clues[-1] == '':
                    clues.append('')

        for i in range(len(clues)):
            self._clues.append('')

        for i in range(len(clues)):
            newI = (i / self._divsX) + (self._divsX * (i % self._divsX))
            self._clues[newI] = clues[i]


    #-----------------------------------------------------------------
    def _CreateSounds(self):
        snds = {}
        snds['fill'] = pygame.mixer.Sound(SOUNDS['fill'])
        snds['buzz'] = pygame.mixer.Sound(SOUNDS['buzz'])
        snds['wrong'] = pygame.mixer.Sound(SOUNDS['wrong'])
        snds['outoftime'] = pygame.mixer.Sound(SOUNDS['outoftime'])

        snds['buzz'].set_volume(0.7)

        return snds
            
                    
    #-----------------------------------------------------------------
    def _DrawBackground(self):
        self._bg.fill(JEOP_BLUE)
        

    #-----------------------------------------------------------------
    def _DrawBoxes(self):
        i = 0
        
        for r in range(self._divsY):
            for c in range(self._divsX):
                self._bg.blit(self._boxes[i].Surface, self._boxCoords[i])
                i += 1


    #-----------------------------------------------------------------
    def _DrawClue(self):
    	
        if self._animateClue:
            clueSfc = self._openClueBox.StepAnimation()
            
            #if animation finished, open new box that covers entire board, ready for clue to be written
            if self._openClueBox.Width >= self._board_w - 2:
                self._animateClue = False
                c = self._openClueBox.Clue
                self._openClueBox = ClueBox((0, 0), (self._board_w, SCREEN_H), c, imgPath=self.ClueImage)
                self._DrawBackground()
                return
            
            self._bg.blit(clueSfc, self._openClueBox.Pos)
        else:
            self._openClueBox.WriteClue()
            self._bg.blit(self._openClueBox.Surface, self._openClueBox.Pos)
            self._openClueBox = None
            return True
        
        return False


    #-----------------------------------------------------------------
    def _DrawRightPanel(self):
        self._bg.blit(self._rPanel.Surface, (self._board_w, 0))


    #-----------------------------------------------------------------
    def _FindClickedBox(self, pos):
        coords = self._boxCoords
        x = -1

        for i in range(self._divsX):
            if pos[0] < coords[i][0]:
                x = i - 1
                break

        if x < 0:
            x = self._divsX - 1

        for i in range(x, len(coords), self._divsX):
            if pos[1] < coords[i][1]:
                return i - self._divsX

        return (self._divsX * (self._divsY) - self._divsX) + x
        


    #===================================================================#
    #---------------------------- PROPERTIES ---------------------------#
    #===================================================================#
    @property
    def BoardWidth(self):
        return self._board_w

    @property
    def BuzzedIn(self):
        return self._buzzedIn

    @property
    def ClueImage(self):
        if self._currentMedia in IMGS:
            return IMGS[self._currentMedia]

        return None
      
    @property
    def PrevAmt(self):
        return self._prevAmt
    
    @property
    def Surface(self):
        return self._bg
        
    @property
    def Video(self):
        if self._currentMedia in VIDEOS:
            return self._currentMedia
        
        return None
        
    @property
    def Winner(self):
    	scores = self._rPanel.Scores
    	high = -1
    	players = []
    	
    	for i in range(len(scores)):
    		if scores[i] > high:
    			high = scores[i]
    			players = [i]
    		elif scores[i] == high:
    			players.append(i)
    																																								
    	return players

    
        
