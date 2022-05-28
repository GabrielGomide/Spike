# This program creates two frames and renders them using spike

import pygame
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Create a 600x600px screen with the title 'Frames'
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Frames')

run = True

# Creates a frame
#   X: 50, Y: 50
#   Width: 500, Height: 100
#   Background color: blue
#   Border size: 5px
#   Border color: green
frame01 = spike.Frame(pygame.Rect(50, 50, 500, 100), spike.BLUE, border=5, border_color=spike.GREEN)

# Creates another frame
#   X: 50, Y: 200
#   Width: 500, Height: 350
#   Background color: yellow
#   Border size: 5px
#   Border color: default (black)
frame02 = spike.Frame(pygame.Rect(50, 200, 500, 350), spike.YELLOW, border=5)

fps = 60
clock = pygame.time.Clock()

# Main loop
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exits the main loop when the player presses the 'X'
            # at the top of the screen
            run = False
	
    surface.fill(spike.RED) # Make the background color red
    frame01.render(surface) # Render the first frame
    frame02.render(surface) # Render the second frame
    pygame.display.update() # Update the screen
	


