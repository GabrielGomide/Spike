import pygame
from . import colors
from . import text


class Select:
    def __init__(self, rect, placeholder='Select', background_color=colors.WHITE, border=2, border_color=colors.BLACK, text_color=colors.BLACK, font_type='Comic Sans MS', text_size=30, selected_color=colors.BLUE):
        self.rect = rect
        self.background_color = background_color
        self.border = border
        self.border_color = border_color
        self.placeholder = placeholder
        self.text_color = text_color
        self.font_type = font_type
        self.text_size = text_size
        self.options = []
        self.selected_color = selected_color
        self.selected = False
        self.option_selected = None

    def add_option(self, text):
        self.options.append(text)

    def in_select(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width:
            if self.rect.y <= y <= self.rect.y + self.rect.height:
                return True
        return False

    def in_option(self, mouse_pos):
        if self.selected:
            x = mouse_pos[0]
            y = mouse_pos[1]

            for i in range(len(self.options)):
                if self.rect.x <= x <= self.rect.x + self.rect.width:
                    if self.rect.y + ((i + 1) * self.rect.height) <= y <= self.rect.y + (self.rect.height * (i + 1)) + self.rect.height:
                        self.option_selected = i
                        return True
            return False

    def render(self, surface):
        border_x = self.rect.x - self.border
        border_y = self.rect.y - self.border
        border_width = self.rect.width + (self.border * 2)
        border_height = self.rect.height + (self.border * 2)
        border_rect = pygame.Rect(border_x, border_y, border_width, border_height)
        border_color = self.border_color if not self.selected else self.selected_color

        pygame.draw.rect(surface, border_color, border_rect)

        pygame.draw.rect(surface, self.background_color, self.rect)
        
        text_x = self.rect.x + (self.rect.width // 2)
        text_y = self.rect.y + (self.rect.height // 2)
        text_color = self.text_color if not self.selected else self.selected_color
        
        _text = self.placeholder if self.option_selected == None else self.options[self.option_selected]

        placeholder_text = text.Text(_text, text_x, text_y, color=text_color, font_type=self.font_type, text_size=self.text_size, center=True)
        
        placeholder_text.render(surface)

        if self.selected:
            if len(self.options):
                for i in range(len(self.options)):
                    border_x = self.rect.x - self.border
                    border_y = self.rect.y - self.border + ((i + 1) * self.rect.height)
                    border_width = self.rect.width + (self.border * 2)
                    border_height = self.rect.height + (self.border * 2)
                    border_rect = pygame.Rect(border_x, border_y, border_width,  border_height)
                    pygame.draw.rect(surface, self.border_color, border_rect)
                    
                    option_y = self.rect.y + ((i + 1) * self.rect.height)
                    option_rect = pygame.Rect(self.rect.x, option_y, self.rect.width, self.rect.height)
                    pygame.draw.rect(surface, self.background_color, option_rect)
                    text_x = self.rect.x + (self.rect.width // 2)
                    text_y = self.rect.y + ((i + 1) * self.rect.height) + (self.rect.height // 2)
                    option_text = text.Text(self.options[i], text_x, text_y, color=self.text_color, font_type=self.font_type, text_size=self.text_size, center=True)
                    option_text.render(surface)



