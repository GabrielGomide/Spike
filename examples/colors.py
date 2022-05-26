import pygame
import sys

sys.path.append('../Spike')

import spike

surface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Colors')

run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	surface.fill(spike.RED)
	pygame.display.update()
	

