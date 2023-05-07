from os import walk

def importar_carpeta(directorio):

    for informacion in walk(directorio):
        print(informacion)
