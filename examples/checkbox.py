import pygame
import sys

sys.path.append('../Spike')

import spike

width, height = 500, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkboxes')

text = spike.Text('Choose map size', 20, 20, text_size=60)
checkbox01 = spike.CheckBox(pygame.Rect(20, 80, 20, 20), text='Small map', border_color=spike.BLUE)
checkbox02 = spike.CheckBox(pygame.Rect(20, 110, 20, 20), text='Medium map', border_color=spike.BLUE)
checkbox03 = spike.CheckBox(pygame.Rect(20, 140, 20, 20), text='Large map', border_color=spike.BLUE)
button = spike.Button(pygame.Rect(20, 200, 100, 60), spike.BLUE, text='Submit', border=2)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if checkbox01.in_checkbox(mouse_pos):
                checkbox01.marked = not checkbox01.marked
                checkbox02.marked = False
                checkbox03.marked = False
            
            if checkbox02.in_checkbox(mouse_pos):
                checkbox01.marked = False
                checkbox02.marked = not checkbox02.marked
                checkbox03.marked = False

            if checkbox03.in_checkbox(mouse_pos):
                checkbox01.marked = False
                checkbox02.marked = False
                checkbox03.marked = not checkbox03.marked

            if button.in_button(mouse_pos):
                run = False


    surface.fill(spike.WHITE)
    text.render(surface)
    checkbox01.render(surface)
    checkbox02.render(surface)
    checkbox03.render(surface)
    button.render(surface)
    pygame.display.update()

if checkbox01.marked:
    print('Map size: Small map')
elif checkbox02.marked:
    print('Map size: Medium map')
elif checkbox03.marked:
    print('Map size: Large map')
else:
    print('Map size not specified')
 

