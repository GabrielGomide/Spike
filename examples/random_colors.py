import pygame
import sys

sys.path.append('../Spike')

import spike

surface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Random colors')

run = True

fps = 60
clock = pygame.time.Clock()
iteration = 0

while run:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	if iteration % fps == 0:
		surface.fill(spike.random_color())
		pygame.display.update()
	iteration += 1

