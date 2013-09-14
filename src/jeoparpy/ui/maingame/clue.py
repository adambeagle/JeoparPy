import pygame

from jeopgamesfc import JeopGameSurface
from ..constants import JEOP_BLUE
from ..resmaps import FONTS
from ..util import draw_centered_textblock, scale

###############################################################################
class Clue(JeopGameSurface):
    """ """
    def __init__(self, size):
        super(Clue, self).__init__(size)
        self._font = pygame.font.Font(FONTS['clue'], scale(51, size[1], 720))
        self.dirty = False
            

    def draw_clue(self, clueLines):
        self.fill(JEOP_BLUE)
        draw_centered_textblock(self, clueLines, self._font, (255, 255, 255),
                                0, scale(4, self.size[1], 720))

    def update(self, gameState, gameData):
        gs = gameState

        if gs.state == gs.CLUE_OPEN:
            cat, clue = gs.arg
            self.draw_clue(gameData.clues[cat][clue])
            self.dirty = True
        
        
