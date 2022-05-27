# This program creates two frames and renders them using spike

import pygame
import sys

sys.path.append('../Spike')

import spike

surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Frames')

run = True

frame01 = spike.Frame(pygame.Rect(50, 50, 500, 100), spike.BLUE, border=5, border_color=spike.GREEN)
frame02 = spike.Frame(pygame.Rect(50, 200, 500, 350), spike.YELLOW, border=5)

fps = 60
clock = pygame.time.Clock()

while run:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	surface.fill(spike.RED)
	frame01.render(surface)
	frame02.render(surface)
	pygame.display.update()
	


