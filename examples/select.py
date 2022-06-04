import pygame
import sys

sys.path.append('../Spike')

import spike

width, height = 500, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Select input')

run = True

select = spike.Select(pygame.Rect(20, 20, 170, 50), 'Country', text_size=40)

select.add_option('Brazil')
select.add_option('USA')
select.add_option('England')
select.add_option('France')
select.add_option('Italy')
select.add_option('Germany')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            select.in_option(mouse_pos)

            if select.in_select(mouse_pos):
                select.selected = not select.selected
            else:
                select.selected = False
    
    surface.fill(spike.WHITE)
    select.render(surface)
    pygame.display.update()




