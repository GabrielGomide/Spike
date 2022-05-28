import pygame
from . import colors

pygame.font.init()

possible_keys = 'abcdefghijklmnopqrstuvwxy0123456789'

uppercase = False

class TextInput:
    def __init__(self, rect, background_color=colors.WHITE, placeholder='', font_type='Comic Sans MS', text_size=30, border=0, border_color=colors.BLACK):
            self.rect = rect
            self.background_color = background_color
            self.placeholder = placeholder
            self.font_type = font_type
            self.text_size = text_size
            self.font = pygame.font.SysFont(self.font_type, self.text_size)
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
        text_x = self.rect.x + (self.rect.width / 2)
        text_y = self.rect.y + (self.rect.height / 2)

        max_characters_in_input = int(self.rect.width // self.text_size * 2.7)

        if self.text_content:
            if len(self.text_content) > max_characters_in_input:
                formated_text = self.text_content[len(self.text_content) - max_characters_in_input:]
            else:
                formated_text = self.text_content

            if not self.selected:
                text = self.font.render(formated_text, False, colors.BLACK)
            else:
                text = self.font.render(formated_text + '|', False, colors.BLACK) 
            text_rect = text.get_rect(center=(text_x, text_y))
            surface.blit(text, text_rect)
        elif self.selected:
            if pygame.time.get_ticks() // 500 % 2 == 0:
                text = self.font.render('|', False, colors.BLACK)
            else:
                text = self.font.render(' ', False, colors.BLACK)
            text_rect = text.get_rect(center=(text_x, text_y))
            surface.blit(text, text_rect)
        elif self.placeholder:
            text = self.font.render(self.placeholder, False, colors.BLACK)
            text_rect = text.get_rect(center=(text_x, text_y))
            surface.blit(text, text_rect)

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

