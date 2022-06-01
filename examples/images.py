import pygame
import os
import sys

sys.path.append('../Spike')

import spike # Import GUI library

# Create a 300x300px screen with the title 'Images'
width, height = 300, 300
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Images')

# Creates an image object
path_to_file = os.path.join(os.getcwd(), 'examples/Assets/grass.png')
image = spike.Image(pygame.Rect(100, 100, 100, 100), pygame.image.load(path_to_file))

run = True

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exits main loop when the player presses the 'X'
            # at the top of the screen
            run = False

    surface.fill(spike.WHITE) # Make the background white
    image.render(surface) # Render the image object
    pygame.display.update() # Update the screen


