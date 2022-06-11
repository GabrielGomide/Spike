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
title = spike.Text('Configurations', 300, 100, center=True, font_type='ubuntumono', text_size=50)
frame01.add_entity(title)


# Creates another frame
#   X: 50, Y: 200
#   Width: 500, Height: 350
#   Background color: yellow
#   Border size: 5px
#   Border color: default (black)
frame02 = spike.Frame(pygame.Rect(50, 200, 500, 350), spike.YELLOW, border=5)
name_text = spike.Text('What\'s your name?', 55, 205)
name_input = spike.TextInput(pygame.Rect(250, 205, 130, 20), border=2, border_color=spike.BLACK)
map_text = spike.Text('Map size:', 55, 240)
small_map = spike.CheckBox(pygame.Rect(100, 275, 20, 20), text='Small map') 
medium_map = spike.CheckBox(pygame.Rect(100, 300, 20, 20), text='Medium map')
large_map = spike.CheckBox(pygame.Rect(100, 325, 20, 20), text='Large map')
submit_button = spike.Button(pygame.Rect(55, 400, 100, 50), spike.GREEN, text='Submit', border=2, border_color=spike.BLACK)

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            spike.handle_checkbox_group(mouse_pos, small_map, medium_map, large_map)
            
            if name_input.in_input(mouse_pos):
                name_input.border_color = spike.BLUE
                name_input.selected = True
            else:
                name_input.border_color = spike.BLACK
                name_input.selected = False

            if submit_button.in_button(mouse_pos):
                run = False

        if event.type == pygame.KEYDOWN:
            name_input.received_input(event)
        elif event.type == pygame.KEYUP:
            name_input.ended_input(event)

    surface.fill(spike.RED) # Make the background color red
    frame01.render(surface, fps) # Render the first frame
    frame02.render(surface, fps) # Render the second frame
    pygame.display.update() # Update the screen
	
if name_input.text_content:
    print(f'Player name: {name_input.text_content}')
else:
    print('Player didn\'t tell his name')

if small_map.marked:
    print('Player chose small map')
elif medium_map.marked:
    print('Player chose medium map')
elif large_map.marked:
    print('Player chose large map')
else:
    print('Player didn\'t choose any map size')



