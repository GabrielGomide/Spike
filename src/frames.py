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
			border_rect = pygame.Rect(self.rect.x - self.border, self.rect.y - self.border, self.rect.width + (self.border * 2), self.rect.height + (self.border * 2))
			pygame.draw.rect(surface, self.border_color, border_rect)
		pygame.draw.rect(surface, self.background_color, self.rect)

