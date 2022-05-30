import pygame
from . import colors
from . import text

pygame.font.init()

class Button:
    def __init__(self, rect, background_color, text='Button', font_type='Comic Sans MS', text_size=30, text_color=colors.BLACK, border=0, border_color=colors.BLACK):
        self.rect = rect
        self.background_color = background_color
        self.text_content = text
        self.font_type = font_type
        self.text_size = text_size
        self.text_color = text_color
        self.border = border
        self.border_color = border_color

    def render(self, surface):
        if self.border > 0:
            border_x = self.rect.x - self.border
            border_y = self.rect.y - self.border
            border_width = self.rect.width + (self.border * 2)
            border_height = self.rect.height + (self.border * 2)
            border_rect = pygame.Rect(border_x, border_y, border_width, border_height)
            pygame.draw.rect(surface, self.border_color, border_rect)
        pygame.draw.rect(surface, self.background_color, self.rect)
        if self.text_content:
            text01 = text.Text(self.text_content, self.rect.x + (self.rect.width // 2), self.rect.y + (self.rect.height // 2), self.text_color, font_type=self.font_type, text_size=self.text_size)
            text01.render(surface)


    def in_button(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width:
            if self.rect.y <= y <= self.rect.y + self.rect.height:
                return True
        return False



