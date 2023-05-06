import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = posicion)

        #Movimiento del jugador
        self.direccion = pygame.math.Vector2(0, 0)
        self.velocidad = 7
        self.gravedad = 0.8
        self.velocidad_salto = -16

    def obtener_teclas(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direccion.x = 1
        elif teclas[pygame.K_LEFT]:
            self.direccion.x = -1
        else:
            self.direccion.x = 0

        if teclas[pygame.K_SPACE]:
            self.saltar()

    def aplicar_gravedad(self):
        self.direccion.y += self.gravedad
        self.rect.y += self.direccion.y

    def saltar(self):
        self.direccion.y = self.velocidad_salto

    def update(self):
        self.obtener_teclas()
        self.rect.x += self.direccion.x * self.velocidad
        self.aplicar_gravedad()