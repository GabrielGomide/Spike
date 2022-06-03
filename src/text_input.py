import pygame
from . import colors
from . import text

pygame.font.init()

possible_keys = 'abcdefghijklmnopqrstuvwxy0123456789'

uppercase = False

class TextInput:
    def __init__(self, rect, background_color=colors.WHITE, placeholder='', border=0, border_color=colors.BLACK):
            self.rect = rect
            self.background_color = background_color
            self.placeholder = placeholder
            self._text = text.Text(placeholder, self.rect.x + (self.rect.width // 2), self.rect.y + (self.rect.height // 2), center=True)
            self.text_size = 30
            self.border = border
            self.border_color = border_color
            self.selected = False
            self.text_content = ''

    def render(self, surface, fps):
        if self.border > 0:
            border_x = self.rect.x - self.border
            border_y = self.rect.y - self.border
            border_width = self.rect.width + (self.border * 2)
            border_height = self.rect.height + (self.border * 2)
            border_rect = pygame.Rect(border_x, border_y, border_width, border_height)
            pygame.draw.rect(surface, self.border_color, border_rect)
        
        pygame.draw.rect(surface, self.background_color, self.rect)
        max_characters_in_input = int(self.rect.width // self.text_size * 2.7)

        if self.text_content:
            if len(self.text_content) > max_characters_in_input:
                formated_text = self.text_content[len(self.text_content) - max_characters_in_input:]
            else:
                formated_text = self.text_content

            if not self.selected:
                self._text.text = formated_text
            else:
                self._text.text = formated_text + '|'
        elif self.selected:
            if pygame.time.get_ticks() // 500 % 2 == 0:
                self._text.text = ''
            else:
                self._text.text = '|'    
            
        elif self.placeholder:
            self._text.text = self.placeholder

        self._text.render(surface)

    def received_input(self, event):
        global uppercase

        if self.selected:
            if event.key == pygame.K_BACKSPACE:
                self.text_content = self.text_content[:-1]
            elif event.key == pygame.K_SPACE:
                self.text_content += ' '
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                uppercase = True
            elif event.key == pygame.K_RETURN:
                self.selected = False
            elif pygame.key.name(event.key) in possible_keys:
                if pygame.key.name(event.key) in 'abcdefghijklmnopqrstuvwxyz':
                    if uppercase:
                        self.text_content += pygame.key.name(event.key).upper()
                        return
                self.text_content += pygame.key.name(event.key)
    
    def ended_input(self, event):
        global uppercase

        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
            uppercase = False

    def in_input(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]
        if self.rect.x <= x <= self.rect.x + self.rect.width:
            if self.rect.y <= y <= self.rect.y + self.rect.height:
                return True
        return False

