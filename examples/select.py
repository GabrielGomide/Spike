import pygame
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Create a 500x500px screen
width, height = 500, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Select input')

# Create a select input with the placeholder 'Country'
select = spike.Select(pygame.Rect(20, 20, 170, 50), 'Country', text_size=40)

# Add options to the select input
select.add_option('Brazil')
select.add_option('USA')
select.add_option('England')
select.add_option('France')
select.add_option('Italy')
select.add_option('Germany')

run = True

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the main loop when the player presses the 'X'
            # at the top of the screen
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Player pressed mouse
            mouse_pos = pygame.mouse.get_pos()
            
            select.in_option(mouse_pos) # See if player selected any option

            if select.in_select(mouse_pos): # See if player clicked on the select input
                select.selected = not select.selected 
            else:
                select.selected = False
    
    surface.fill(spike.WHITE) # Make the background color white
    select.render(surface) # Render the select input
    pygame.display.update() # Update the display

# Outside of the main loop...

# Print the option the player selected
if select.option_selected != None:
    print(f'The player lives in {select.options[select.option_selected]}')

