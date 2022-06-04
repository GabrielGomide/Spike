import pygame
import sys

sys.path.append('../Spike')

import spike # Import the GUI library

# Create a 500x500px 
width, height = 500, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkboxes')

# Create a text "Choose map size"
text = spike.Text('Choose map size', 20, 20, text_size=60)

# Create three checkboxes
checkbox01 = spike.CheckBox(pygame.Rect(20, 80, 20, 20), text='Small map', border_color=spike.BLUE)
checkbox02 = spike.CheckBox(pygame.Rect(20, 110, 20, 20), text='Medium map', border_color=spike.BLUE)
checkbox03 = spike.CheckBox(pygame.Rect(20, 140, 20, 20), text='Large map', border_color=spike.BLUE)

# Create a button
button = spike.Button(pygame.Rect(20, 200, 100, 60), spike.BLUE, text='Submit', border=2)

run = True

# Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the main loop when the player presses the 'X'
            # at the top of the screen
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Player pressed mouse
            mouse_pos = pygame.mouse.get_pos() # Get mouse position

            # Handle checkboxes
            # Warning: A checkbox group means that only one checkbox
            # of the group can be marked at once
            spike.handle_checkbox_group(mouse_pos, checkbox01, checkbox02, checkbox03)
           
            if button.in_button(mouse_pos): # Player pressed button
                run = False # Exit the main loop


    surface.fill(spike.WHITE) # Make the background color white
    text.render(surface) # Render the text

    # Render the three checkboxes
    checkbox01.render(surface)
    checkbox02.render(surface)
    checkbox03.render(surface)

    button.render(surface) # Render the button
    pygame.display.update() # Update the screen

# Outside of the main loop ...

# Print the player selection
if checkbox01.marked:
    print('Map size: Small map')
elif checkbox02.marked:
    print('Map size: Medium map')
elif checkbox03.marked:
    print('Map size: Large map')
else:
    print('Map size not specified')
 

