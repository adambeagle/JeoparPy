import pygame
from pygame.locals import *

from adam.util.types_util import to_numeric

###############################################################################
def shadow_text(msg, srcRect, font, offset, color=(0, 0, 0)):
    """
    Returns surface and rect of shadowed text.
    Shadow is positioned 'offset' pixels right and down from srcRect.
    'msg' is string to shadow.
    """
    shadText = font.render(msg, 1, color)
    rect = shadText.get_rect()

    rect.x = srcRect.x + offset
    rect.y = srcRect.y + offset
    
    return shadText, rect

def get_size_textblock(lines, font, spacing):
    """
    Returns dimensions needed to render 'lines' of text
    in passed font, with 'spacing' pixels between each line.
    """
    blockW = 0
    blockH = 0

    for line in lines:
        w, h = font.size(line)
        blockW = max(blockW, w)
        blockH += h + spacing
        

    return (blockW, blockH)

def wait_for_keypress(key=None):
    """
    By default, return control when any key is pressed.
    If one key constant or list is passed, return only when 
    one of those keys is pressed.
    """
    if not key == None and not isinstance(key, collections.Iterable):
        key = [key]

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if key and event.key in key:
                    return
                elif not key:
                    return

            if event.type == QUIT:
                sys.exit()

        pygame.event.pump()

###############################################################################
class BorderedBox(pygame.Surface):
    """
    A pygame.Surface box with a customizable border.

    ATTRIBUTES:
      * borderColor
      * borderWidths
      * fillColor
      * rect
      * size (read-only)

    METHODS:
      * draw_centered_text
      * redraw
    """
    def __init__(self, size, fillColor, borderW, borderColor):
        """
        'borderW' can be an int for equal borders,
        or a 4-tuple defining widths for (top, right, bottom, left).
        """
        super(BorderedBox, self).__init__(size)
        
        self._size = size
        self.fillColor = fillColor
        self.borderColor = borderColor
        self.borderWidths = borderW
        self.rect = self.get_rect()

        self.redraw()

    def copy(self):
        b = BorderedBox(self.size, self.fillColor,
                        self.borderWidths, self.borderColor)
        b.rect = self.rect.copy()
        
        return b

# TODO 9/12 The three text-drawing functions below should be abstracted
#   into generic utility functions. 
    def draw_centered_textblock(self, lines, font, color, 
                                spacing=0, shadowOffset=None):
        """ """
        blockRect = pygame.Rect((0, 0), get_size_textblock(lines, font, spacing))
        blockRect.center = pygame.Rect((0, 0), self.size).center
        lineH = font.get_linesize()

        for i, line in enumerate(lines):
            rect = pygame.Rect((0, 0), font.size(line))
            rect.centerx = blockRect.centerx
            rect.y = blockRect.y + lineH*i

            self.draw_textline(line, font, color, rect, shadowOffset)
            
                
    def draw_centered_text(self, text, font, color, shadowOffset=None):
        rect = pygame.Rect((0, 0), font.size(text))
        rect.center = self.get_rect().center
        self.draw_textline(text, font, color, rect, shadowOffset)

    def draw_textline(self, text, font, color, rect, shadowOffset=None):
        s = text
        doShadow = shadowOffset is not None
        text = font.render(s, 1, color)

        if doShadow:
            shadow, shadRect = shadow_text(s, rect, font, shadowOffset)
            self.blit(shadow, shadRect)

        self.blit(text, rect)

    def redraw(self):
        """
        Redraws box. Must be called after altering any attributes
        for changes to be reflected on surface.
        If there was any text on the box, it will be erased;
        call draw_centered_text again to redraw it.
        """
        tb, rb, bb, lb = self.borderWidths
        w, h = self.size
        
        self.fill(self.borderColor)
        inner = pygame.Surface((w - rb - lb,
                                h - tb - bb))
        inner.fill(self.fillColor)
        self.blit(inner, (lb, tb))

    @property
    def borderWidths(self):
        return self._borderWs

    @borderWidths.setter
    def borderWidths(self, val):
        ws = []
        
        if not hasattr(val, '__iter__'):
            val = 4*[val]

        try:
            for i in xrange(4):
                ws.append(to_numeric(val[i]))
        except IndexError:
            raise BorderError("'borderW' contains ")
        except (TypeError, ValueError):
            raise BorderError()

        self._borderWs = tuple(ws)

    @property
    def size(self):
        return self._size
    
###############################################################################
class BorderError(Exception):
    pass

