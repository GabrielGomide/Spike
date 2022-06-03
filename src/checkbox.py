import pygame
from . import colors
from . import text as _text

class CheckBox:
    def __init__(self, rect, border=2, background_color=colors.WHITE, border_color=colors.BLACK, text=None, font_type='Comic Sans MS', text_size=30, text_color=colors.BLACK):
        self.rect = rect
        self.border = border
        self.background_color = background_color
        self.border_color = border_color
    
        text_x = self.rect.x + self.rect.width + 5
        self.text = _text.Text(text, text_x, self.rect.y, font_type=font_type, text_size=text_size, center=False, color=text_color)

        self.marked = False

    def render(self, surface):
        border_x = self.rect.x - self.border
        border_y = self.rect.y - self.border
        border_width = self.rect.width + (self.border * 2)
        border_height = self.rect.height + (self.border * 2)
        border_rect = pygame.Rect(border_x, border_y, border_width, border_height)

        pygame.draw.rect(surface, self.border_color, border_rect)
        
        if not self.marked:
            pygame.draw.rect(surface, self.background_color, self.rect)

        self.text.render(surface)

    def in_checkbox(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width:
            if self.rect.y <= y <= self.rect.y + self.rect.height:
                return True
        return False



