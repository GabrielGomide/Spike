import pygame
import sys

sys.path.append('../Spike')

import spike

width, height = 600, 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Drag and drop')

dragdrop01 = spike.DragAndDrop(pygame.Rect(10, 10, 100, 100), spike.RED)
dragdrop02 = spike.DragAndDrop(pygame.Rect(10, 200, 100, 100), spike.BLUE)
dragdrop03 = spike.DragAndDrop(pygame.Rect(10, 400, 100, 100), spike.YELLOW)

run = True
fps = 60
clock = pygame.time.Clock()

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            dragdrop01.mouse_down(pos)
            dragdrop02.mouse_down(pos)
            dragdrop03.mouse_down(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            dragdrop01.mouse_up()
            dragdrop02.mouse_up()
            dragdrop03.mouse_up()

        dragdrop01.mouse_moved(pos)
        dragdrop02.mouse_moved(pos)
        dragdrop03.mouse_moved(pos)

    surface.fill(spike.WHITE)
    dragdrop01.render(surface)
    dragdrop02.render(surface)
    dragdrop03.render(surface)
    pygame.display.update()


