import pygame
from . import colors

pygame.font.init()

class Text:
        def __init__(self, text, x, y, color=colors.BLACK, font_type='Comic Sans MS', text_size=30):
            self.text = text
            self.x = x
            self.y = y
            self.color = color
            self.font = pygame.font.SysFont(font_type, text_size)

        def render(self, surface):
            text = self.font.render(self.text, False, self.color)
            text_rect = text.get_rect(center=(self.x, self.y))
            surface.blit(text, text_rect)

