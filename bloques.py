import pygame
from pygame.sprite import AbstractGroup

class Bloque(pygame.sprite.Sprite):
    def __init__(self, posicion, tamaño):
        super().__init__()
        self.image = pygame.Surface((tamaño, tamaño))
        self.image.fill((128 , 128, 128))
        self.rect = self.image.get_rect(topleft = posicion)