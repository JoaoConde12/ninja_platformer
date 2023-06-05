import pygame
from importador import importar_carpeta
from configuraciones import ventana_ancho


class Bloque(pygame.sprite.Sprite):
    def __init__(self, tamaño, x, y):
        super().__init__()
        self.image = pygame.Surface((tamaño, tamaño))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, cambio):
	    self.rect.x += cambio
            

class Bloque_estatico(Bloque):
     def __init__(self, tamaño, x, y, superficie):
        super().__init__(tamaño, x, y)
        self.image = superficie


class Animacion(Bloque):
    def __init__(self, tamaño, x, y, direccion):
        super().__init__(tamaño, x, y)
        self.frames = importar_carpeta(direccion)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animar(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, cambio):
        self.animar()
        self.rect.x += cambio


class Animacion_olas(Bloque):
    def __init__(self, tamaño, x, y, direccion):
        super().__init__(tamaño, x, y)
        self.frames = importar_carpeta(direccion)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animar(self):
        self.frame_index += 0.11
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, cambio):
        self.animar()
        self.rect.x += cambio