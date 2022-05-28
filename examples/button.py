# This is a program that uses the button class and the color module 
# on spike to create a small clicker game

import pygame
import random
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Creates a 600x600px screen with the title 'Buttons'
width, height = 600, 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Buttons')

run = True

# Creates a button in the center of the screen
button = spike.Button(pygame.Rect(200, 270, 200, 80), spike.BLUE, text='Change the color', border=5)

current_color = spike.WHITE # Current background color

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the main loop when the player presses the 'X'
            # at the top of the screen
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: # Player pressed the mouse
            if button.in_button(pygame.mouse.get_pos()): # If player pressed the button
                # Then change the current background color to a random color
                current_color = spike.random_color()
                # And move the button to a random position
                button.rect.x = random.randint(button.border, width - (button.rect.width + button.border))
                button.rect.y = random.randint(button.border, height - (button.rect.height + button.border))

    surface.fill(current_color) # Make the background color the current_color
    button.render(surface) # Render the button
    pygame.display.update() # Update the screen


