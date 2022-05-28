import pygame
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Create a 300x300px screen with the title 'Colors'
surface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Colors')

run = True

# Main loop
while run:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
            # Exit the main loop when the player presses the 'X'
            # at the top of the screen
	    run = False

    surface.fill(spike.RED) # Sets the background color to red using spike's colors
    pygame.display.update() # Updated the screen
	

