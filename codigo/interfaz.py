import pygame

class Interfaz:
    def __init__(self, surface):
        #Configuración
        self.ventana_surface = surface

        #Barra de vida
        self.barra_vida = pygame.image.load("../graficos/interfaz/barra_vida.png").convert_alpha()
        self.barra_vida_topleft = (54, 39)
        self.barra_maxima_ancho = 152
        self.barra_altura = 4

        #Contador de monedas
        self.contador_monedas = pygame.image.load("../graficos/interfaz/monedas.png").convert_alpha()
        self.contador_monedas_rect = self.contador_monedas.get_rect(topleft = (20, 71))
        self.font = pygame.font.Font("../graficos/interfaz/tipografia.TTF", 30)

        #
        self.mushroom = pygame.image.load("../graficos/interfaz/mushroom.png").convert_alpha()
        self.mushroom_rect = self.mushroom.get_rect(topleft = (1190, 39))
        self.font = pygame.font.Font("../graficos/interfaz/tipografia.TTF", 30)


    def mostrar_vida(self, vida_actual, vida_maxima):
        self.ventana_surface.blit(self.barra_vida, (20, 10))
        vida_actual_ratio = vida_actual / vida_maxima
        vida_actual_ancho = self.barra_maxima_ancho * vida_actual_ratio
        barra_vida_rect = pygame.Rect(self.barra_vida_topleft, (vida_actual_ancho, self.barra_altura))
        pygame.draw.rect(self.ventana_surface, "#dc4949", barra_vida_rect)


    def mostrar_monedas(self, cantidad):
        self.ventana_surface.blit(self.contador_monedas, self.contador_monedas_rect)
        aumentar_monedas_surf = self.font.render(str(cantidad), False, "#33323d")
        aumentar_monedas_rect = aumentar_monedas_surf.get_rect(midleft = (self.contador_monedas_rect.right + 4,
                                                                          self.contador_monedas_rect.centery))
        self.ventana_surface.blit(aumentar_monedas_surf, aumentar_monedas_rect)


    def mostrar_mushroom(self, cantidad):
        self.ventana_surface.blit(self.mushroom, self.mushroom_rect)
        mushroom_surf = self.font.render(str(cantidad), False, "#33323d")
        mushroom_rect = mushroom_surf.get_rect(midleft = (self.mushroom_rect.right + 4,
                                                                        self.mushroom_rect.centery))
        self.ventana_surface.blit(mushroom_surf, mushroom_rect)

