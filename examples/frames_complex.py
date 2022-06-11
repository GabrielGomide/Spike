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

# Create text object
title = spike.Text('Configurations', 300, 100, center=True, font_type='ubuntumono', text_size=50)

# Add text object to frame01 as entities
frame01.add_entity(title)


# Creates another frame
#   X: 50, Y: 200
#   Width: 500, Height: 350
#   Background color: yellow
#   Border size: 5px
#   Border color: default (black)
frame02 = spike.Frame(pygame.Rect(50, 200, 500, 350), spike.YELLOW, border=5)

# Create objects
name_text = spike.Text('What\'s your name?', 55, 205)
name_input = spike.TextInput(pygame.Rect(250, 205, 130, 20), border=2, border_color=spike.BLACK)
map_text = spike.Text('Map size:', 55, 240)
small_map = spike.CheckBox(pygame.Rect(100, 275, 20, 20), text='Small map') 
medium_map = spike.CheckBox(pygame.Rect(100, 300, 20, 20), text='Medium map')
large_map = spike.CheckBox(pygame.Rect(100, 325, 20, 20), text='Large map')
submit_button = spike.Button(pygame.Rect(55, 400, 100, 50), spike.GREEN, text='Submit', border=2, border_color=spike.BLACK)

# Add objects to frame02 as entities
frame02.add_entity(name_text)
frame02.add_entity(name_input)
frame02.add_entity(map_text)
frame02.add_entity(small_map)
frame02.add_entity(medium_map)
frame02.add_entity(large_map)
frame02.add_entity(submit_button)

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

        if event.type == pygame.MOUSEBUTTONDOWN: # Player pressed mouse
            mouse_pos = pygame.mouse.get_pos() # Get mouse position

            spike.handle_checkbox_group(mouse_pos, small_map, medium_map, large_map) # Handle checkboxes
            
            if name_input.in_input(mouse_pos): # Player pressed text input
                # Make the text input border color blue
                name_input.border_color = spike.BLUE
                # Tell the text input its been selected
                name_input.selected = True
            else: # Player pressed anywhere outside the text input
                # Make the text input border color black again
                name_input.border_color = spike.BLACK
                # Tell the text input its been unselected
                name_input.selected = False

            if submit_button.in_button(mouse_pos): # Player pressed submit button
                run = False # Exit screen

        if event.type == pygame.KEYDOWN: # Player pressed key on keyboard
            name_input.received_input(event) # Add key to text
        elif event.type == pygame.KEYUP: # Player stoped pressing key on keyboard
            name_input.ended_input(event) # Tell the text input
    
    if not name_input.selected and name_input.border_color == spike.BLUE:
        name_input.border_color = spike.BLACK

    surface.fill(spike.RED) # Make the background color red
    frame01.render(surface, fps) # Render the first frame AND ALL ITS ENTITIES
    frame02.render(surface, fps) # Render the second frame AND ALL ITS ENTITIES
    pygame.display.update() # Update the screen
	
# Print result of name_input
if name_input.text_content:
    print(f'Player name: {name_input.text_content}')
else:
    print('Player didn\'t tell his name')

# Print the result of the checkboxes
if small_map.marked:
    print('Player chose small map')
elif medium_map.marked:
    print('Player chose medium map')
elif large_map.marked:
    print('Player chose large map')
else:
    print('Player didn\'t choose any map size')



