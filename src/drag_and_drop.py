import pygame
from . import frames
from . import colors
from . import text

class DragAndDrop():
    def __init__(self, rect, background_color, border=0, border_color=colors.BLACK):
        self.rect = rect
        self.background_color = background_color
        self.border = border
        self.border_color = border_color
        self.selected = False
        self.x = None
        self.y = None

    def in_frame(self, x, y):
        if self.rect.x <= x <= self.rect.x + self.rect.width:
            if self.rect.y <= y <= self.rect.y + self.rect.height:
                return True
        return False

    def mouse_down(self, pos):
        if self.in_frame(pos[0], pos[1]):
            self.selected = True
            self.x = pos[0] - self.rect.x
            self.y = pos[1] - self.rect.y

    def mouse_moved(self, pos):
        if self.selected:
            self.rect.x = pos[0] - self.x
            self.rect.y = pos[1] - self.y

    def mouse_up(self):
        self.selected = False

    def render(self, surface):
        if self.border > 0:
            border_x = self.rect.x - self.border
            border_y = self.rect.y - self.border
            border_width = self.rect.width + (self.border * 2)
            border_height = self.rect.height + (self.border * 2)
            border_rect = pygame.Rect(border_x, border_y, border_width, border_height)
            pygame.draw.rect(surface, self.border_color, border_rect)

        pygame.draw.rect(surface, self.background_color, self.rect)
