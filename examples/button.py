# This is a program that uses the button class and the color module 
# on spike to create a small clicker game

import pygame
import random
import sys

sys.path.append('../Spike')

import spike

width, height = 600, 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Buttons')

run = True

button = spike.Button(pygame.Rect(200, 270, 200, 80), spike.BLUE, text='Change the color', border=5)

current_color = spike.WHITE

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if button.in_button(pygame.mouse.get_pos()):
				current_color = spike.random_color()
				button.rect.x = random.randint(0, width - (button.rect.width + button.border))
				button.rect.y = random.randint(0, height - (button.rect.height + button.border))

	surface.fill(current_color)
	button.render(surface)
	pygame.display.update()


