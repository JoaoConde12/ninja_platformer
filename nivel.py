import pygame
from bloques import Bloque
from configuraciones import tamaño_bloque

class Nivel:
    def __init__(self, nivel_beta, surface):
        #super().__init__()
        self.mostrar_surface = surface
        self.cofigurar_nivel(nivel_beta)

    def cofigurar_nivel(self, layout):
        self.bloques = pygame.sprite.Group()
        for fila_indice, fila in enumerate(layout):
            for columna_indice, columna in enumerate(fila):
                if columna == 'x':
                    x = columna_indice * tamaño_bloque
                    y = fila_indice * tamaño_bloque
                    bloque = Bloque((x, y), tamaño_bloque)
                    self.bloques.add(bloque)

    def ejecutar(self):
        self.bloques.draw(self.mostrar_surface)