import pygame
from bloques import Bloque_estatico


class Mushroom_salto(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/mushroom_salto/mushroom_salto.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Mushroom_decoracion(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/decoraciones/mushroom_dec/mushroom_dec.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))