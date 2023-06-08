import pygame
from data_niveles import niveles


class Nodo(pygame.sprite.Sprite):
    def __init__(self, posicion, estado, velociad_icono):
        super().__init__()
        self.image = pygame.Surface((100, 80))
        if estado == "disponible":
            self.image.fill("blue")
        else:
            self.image.fill("grey")
        self.rect = self.image.get_rect(center = posicion)

        self.detectar_colision = pygame.Rect(self.rect.centerx - (velociad_icono / 2),
                                             self.rect.centery - (velociad_icono / 2),
                                             velociad_icono,
                                             velociad_icono)