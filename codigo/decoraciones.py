import pygame
from bloques import Bloque_estatico, Animacion


class Roca(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/decoraciones/roca/roca.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Cartel1(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/decoraciones/cartel1/cartel1.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Cartel2(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/decoraciones/cartel2/cartel2.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))

    
class Cajas(Bloque_estatico):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, pygame.image.load("../graficos/decoraciones/caja/caja.png").convert_alpha())
        desplazar_y = y + tamaño
        self.rect = self.image.get_rect(bottomleft = (x, desplazar_y))


class Monedas(Animacion):
    def __init__(self, tamaño, x, y, direccion, valor):
        super().__init__(tamaño, x, y, direccion)
        centro_x = x + int(tamaño / 2)
        centro_y = y + int(tamaño / 2)
        self.rect = self.image.get_rect(center = (centro_x, centro_y))
        self.valor = valor