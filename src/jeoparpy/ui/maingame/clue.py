import pygame

from jeopgamesfc import JeopGameSurface
from ..constants import JEOP_BLUE
from ..resmaps import FONTS, IMAGES
from ..util import (draw_centered_textblock, draw_textblock,
                    get_size_textblock, scale)

###############################################################################
class Clue(JeopGameSurface):
    """ """
    def __init__(self, size):
        super(Clue, self).__init__(size)
        self._font = pygame.font.Font(FONTS['clue'], scale(51, size[1], 720))
        self.dirty = False
            

    def draw_clue(self, clueLines, img=None):
        self.fill(JEOP_BLUE)
        if img:
            self._draw_clue_and_image(clueLines, img)
        else:
            draw_centered_textblock(self, clueLines, self._font,
                                    (255, 255, 255), 0,
                                    scale(4, self.size[1], 720))
            
    def update(self, gameState, gameData):
        gs = gameState

        if gs.state == gs.CLUE_OPEN:
            cat, clue = gs.arg
            img = self._get_media(gs.arg)
            self.draw_clue(gameData.clues[cat][clue], img)
            self.dirty = True

    def _draw_clue_and_image(self, clueLines, img):
        spacer = 10
        blockSize = get_size_textblock(clueLines, self._font, 0)
        imgRect = img.get_rect()
        imgSize = imgRect.size
        size = (blockSize[0], blockSize[1] + spacer + imgSize[1])
            
        rect = pygame.Rect((0, 0), size)
        rect.center = self.rect.center

        draw_textblock(self, clueLines, self._font, (255, 255, 255),
                       rect.topleft, True, 0, scale(4, self.size[1], 720))

        rect.h -= imgSize[1]
        imgRect.top = rect.bottom
        imgRect.centerx = rect.centerx
        self.blit(img, imgRect)
        

    def _get_media(self, coords):
        if coords in IMAGES:
            img = pygame.image.load(IMAGES[coords]).convert()
            scaledSize = (scale(x, self.size[1], 720)
                          for x in img.get_size())
            return pygame.transform.smoothscale(img, tuple(scaledSize))

        return None
        
        
        
