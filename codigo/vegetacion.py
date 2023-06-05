import pygame
from bloques import Bloque_estatico

#En vegetación se importará los árboles, troncos y arbustos

class Arbol1(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arboles/arbol1/0.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Arbol2(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arboles/arbol2/2.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))

        
class Tronco(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arboles/tronco/1.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))
