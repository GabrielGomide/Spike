import pygame
from . import colors
import sys

class Frame:
	def __init__(self, rect, background_color, border=0, border_color=colors.BLACK):
		self.rect = rect
		self.background_color = background_color
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



