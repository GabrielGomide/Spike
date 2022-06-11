import pygame
import sys

sys.path.append('../Spike')

import spike # Import GUI library

# Create a 600x600px screen with the title 'Drag and drop'
width, height = 600, 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Drag and drop')

# Create three drag and drops, one red, one blue and one yellow
dragdrop01 = spike.DragAndDrop(pygame.Rect(10, 10, 100, 100), spike.RED)
dragdrop02 = spike.DragAndDrop(pygame.Rect(10, 200, 100, 100), spike.BLUE)
dragdrop03 = spike.DragAndDrop(pygame.Rect(10, 400, 100, 100), spike.YELLOW)

run = True
fps = 60
clock = pygame.time.Clock()

# Main looop
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the screen when the player presses the 'X'
            # at the top of the screen
            run = False

        pos = pygame.mouse.get_pos() # Get mouse positon
        
        if event.type == pygame.MOUSEBUTTONDOWN: # Player pressed mouse
            # Tell all drag and drops that the mouse has been pressed
            dragdrop01.mouse_down(pos)
            dragdrop02.mouse_down(pos)
            dragdrop03.mouse_down(pos)

        if event.type == pygame.MOUSEBUTTONUP: # Player pressed up
            # Tell all the drag and drops that the mouse is up
            dragdrop01.mouse_up()
            dragdrop02.mouse_up()
            dragdrop03.mouse_up()

        # The mouse has moved
        # therefore move the frames along with the mouse if they're selected
        dragdrop01.mouse_moved(pos)
        dragdrop02.mouse_moved(pos)
        dragdrop03.mouse_moved(pos)

    surface.fill(spike.WHITE) # Make the background color white
    # Draw the drag and drops
    dragdrop01.render(surface)
    dragdrop02.render(surface)
    dragdrop03.render(surface)
    pygame.display.update() # Update the display


