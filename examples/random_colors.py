# This program changes the background to a random color from spike every second

import pygame
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Create a 300x300px screen with the title 'Random colors'
surface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Random colors')

run = True

fps = 60
clock = pygame.time.Clock()
iteration = 0

# Main loop
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the main loop when the player pressed the 'X'
            # at the top of the screen
            run = False
    
    if iteration % fps == 0:
        # Changes the background color to a random color once every second
        surface.fill(spike.random_color())
        pygame.display.update()
    
    iteration += 1

