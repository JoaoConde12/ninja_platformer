import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = posicion)
        self.direccion = pygame.math.Vector2(0, 0)
        self.velocidad = 7

    def obtener_teclas(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direccion.x = 1
        elif teclas[pygame.K_LEFT]:
            self.direccion.x = -1
        else:
            self.direccion.x = 0

    def update(self):
        self.obtener_teclas()
        self.rect.x += self.direccion.x * self.velocidad