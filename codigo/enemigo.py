import pygame
from bloques import Animacion


class Enemigo(Animacion):
    def __init__(self, tamaño, x, y):
        super().__init__(tamaño, x, y, "../graficos/enemigos/enemigo1/sprites")
        self.rect.y += tamaño - self.image.get_size()[1]
        self.velocidad = 3

    def mover(self):
        self.rect.x += self.velocidad

    def reversa_img(self):
        if self.velocidad > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reversa(self):
        self.velocidad *= -1

    def update(self, cambio):
        self.rect.x += cambio
        self.animar()
        self.mover()
        self.reversa_img()