import pygame
from os import walk

def importar_carpeta(directorio):

    lista = []

    for _ ,__ , archivos_img in walk(directorio):
        for imagen in archivos_img:
            directorio_lleno = directorio + "/" + imagen
            imagen_surf = pygame.image.load(directorio_lleno).convert_alpha()
            lista.append(imagen_surf)

    return lista
        
