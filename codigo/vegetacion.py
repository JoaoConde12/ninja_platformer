import pygame
from bloques import Bloque_estatico

#En vegetación se importará los árboles, troncos y arbustos

class Arbol1(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arboles/arbol1/arbol1.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Arbol2(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arboles/arbol2/arbol2.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))

        
class Tronco(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arboles/tronco/tronco.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Arbusto1(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arbustos/arbusto1/arbusto1.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Arbusto2(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arbustos/arbusto2/arbusto2.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Arbusto3(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arbustos/arbusto3/arbusto3.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Arbusto4(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/arbustos/arbusto4/arbusto4.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))
