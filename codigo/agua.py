import pygame
from bloques import Bloque_estatico, Animacion_olas


class Agua(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/decoraciones/agua/agua.png").convert_alpha())
        self.rect = self.image.get_rect(topleft = (x, y))


class Olas(Animacion_olas):
    def __init__(self, tamaño, x, y, direccion):
        super().__init__(tamaño, x, y, direccion)
        self.rect = self.image.get_rect(bottomleft = (x, y + tamaño))
