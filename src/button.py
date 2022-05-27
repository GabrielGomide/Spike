import pygame
from . import colors

pygame.font.init()

class Button:
	def __init__(self, rect, background_color, text='Button', font_type='Comis Sans MS', text_size=30, border=0, border_color=colors.BLACK):
		self.rect = rect
		self.background_color = background_color
		self.text_content = text
		self.font_type = font_type
		self.text_size = text_size
		self.font = pygame.font.SysFont(self.font_type, self.text_size)
		self.font
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
			text = self.font.render(self.text_content, False, colors.BLACK)
			text_x = self.rect.x + (self.rect.width / 2)
			text_y = self.rect.y + (self.rect.height / 2)
			text_rect = text.get_rect(center=(text_x, text_y))
			surface.blit(text, text_rect)

	def in_button(self, mouse_pos):
		x = mouse_pos[0]
		y = mouse_pos[1]
		if self.rect.x <= x <= self.rect.x + self.rect.width:
			if self.rect.y <= y <= self.rect.y + self.rect.height:
				return True
		return False



