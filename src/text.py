import pygame
from . import colors

pygame.font.init()

class Text:
        def __init__(self, text, x, y, color=colors.BLACK, font_type='Comic Sans MS', text_size=30, center=False):
            self.text = text
            self.x = x
            self.y = y
            self.color = color
            self.font = pygame.font.SysFont(font_type, text_size)
            self.center = center

        def render(self, surface):
            text = self.font.render(self.text, False, self.color)

            if self.center:
                text_rect = text.get_rect(center=(self.x, self.y))
                surface.blit(text, text_rect)
            else:
                surface.blit(text, (self.x, self.y))

