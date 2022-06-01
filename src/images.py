import pygame

class Image:
    def __init__(self, rect, image):
        self.rect = rect
        self.image = image

    def render(self, surface):
        surface.blit(pygame.transform.scale(self.image, (self.rect.width, self.rect.height)), (self.rect.x, self.rect.y))


