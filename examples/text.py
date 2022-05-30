import pygame
import sys

sys.path.append('../Spike/')

import spike

width, height = 600, 120
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Texts')

run = True

text01 = spike.Text('Some text in Comic Sans MS', 300, 15)
text02 = spike.Text('Some more text in ubuntumono', 300, 50, font_type='ubuntumono', color=spike.RED)
text03 = spike.Text('Some text in 50px', 300, 90, text_size=50, color=spike.BLUE)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    surface.fill(spike.WHITE)
    text01.render(surface)
    text02.render(surface)
    text03.render(surface)
    pygame.display.update()




