# This program takes input in a pygame window
# and then displays the result of the input in
# the terminal once you close the window

import pygame
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Creates a 600x600px window with the title 'Text inputs'
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Text inputs')

# Creates a text input
text_input = spike.TextInput(pygame.Rect(150, 275, 300, 50), placeholder='Text Input', border=5)

run = True

fps = 60
clock = pygame.time.Clock()

# Main loop
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            # Stops the main loop once the player pressed the 'X'
            # sign at the top of the screen
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: # Player pressed the mouse
            if text_input.in_input(pygame.mouse.get_pos()): # If player pressed the input
                # Then make the border color to blue
                text_input.border_color = spike.BLUE
                # And also start taking input
                text_input.selected = True
            else: # If the player pressed the mouse somewhere outside the input
                # Then make the border color black again
                text_input.border_color = spike.BLACK
                # And also stop taking input
                text_input.selected = False

        if event.type == pygame.KEYDOWN: # Player pressed some key on the keyboard
            text_input.received_input(event) # Send it to the text input
        elif event.type == pygame.KEYUP: # Input stopped
            text_input.ended_input(event) # Send it to the text input

    # Player ended input by pressing enter instead
    # of clicking somewhere outside the text input
    if not text_input.selected and text_input.border_color == spike.BLUE:
        text_input.border_color = spike.BLACK

    surface.fill(spike.WHITE) # Make the surface background white
    text_input.render(surface, fps) # Render the text input
    pygame.display.update() # Update the screen

# After the player exited the screen display
# the result of the text input on the terminal
print(f'Input: {text_input.text_content}')


