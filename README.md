# New_Idiri

Primer avance del videojuego New Idiri (Nuevo Líder)

De forma general, lo que se ha hecho a lo largo de este primer progreso, ha sido primer indagar sobre los lenguajes de programación existentes con sus respectivas librerías y cual se adaptaría mejor para llevar acabo el desarrollo de un videojuego. Después de haber seleccionado un lenguaje, se empezó con la planificación del juego, se decidió que sería del estilo de plataformas y que tuviera entre 2 a 3 niveles, luego se decidió implementar un poco de historia para que el juego tenga un poco de profundidad y el jugador pueda tener un poco de contexto sobre en que ambiente está pensado este juego. Finalmente se dio paso al desarrollo del videojuego.

## Lenguaje seleccionado y librerías

![imagen_2023-05-07_184657907](https://user-images.githubusercontent.com/132232545/236708520-f052e6a4-2f3d-40b1-8f70-2023bc6c384c.png)


El lenguaje de programación que fue elegido es Python, esto debido a que tiene un sintaxis sencilla y que a su vez permite la programación orientada a objetos, por ende iba a ser mucho más fácil la creación del juego. Adicionalmente, si bien Python no es especialmente conocido por ser un lenguaje adecuado para desarrollar videojuegos, se pensó que Python es una excelente puerta para alguien que deseé adentrarse a este mundo. Ya que a diferencia de utilizar motores gráficos conocidos como Unity o Unreal Engine, en Python no tendremos la ayuda de ese tipo de motores y por ende vamos a tener que implementar las funcionalidades que deseemos solo con código, lo que permitirá comprender de mejor manera como funcionan dichos motores y tener una mejor base de lógica de programación cuando se desee hacer juegos con algún motor gráfico.

Hasta el momento se han usado 2 librerías, la primera fue Pygame; esta se encontró en esta página: https://pypi.org/project/pygame/ y para su instalación simplemente se ejecutó el comando pip install pygame en la terminal. La segunda librería fue Os-sys ya que con esta librería se pueden manipular funcionalidades dependientes del sistema operativo, como por ejemplo acceder a directorios o archivos; esta se encontró en esta página: https://pypi.org/project/os-sys/ y para su instalación fue similar a la de pygame, simplemente se escribió el comando pip install os-sys en la terminal.

## Desarrollo del videojuego

Lo primero que se hizo es establecer las medidas de la ventana, luego seleccionar un fondo de color negro y después crear una mini version de mapa (provisional) para entender el como funcionan los bloques del videojuego. Una vez hecho esto se creo una beta del jugador, el cuál era un rectángulo rojo al cual primero se le dio movimiento tanto en el eje x positivo y negativo. Después se dio paso a la creación de una cámara que pueda seguir al jugador a donde se moviera y se le dio la función de saltar.

Una vez comprobado que no hubieran problemas se le agrego las respectivas colisiones al jugador para que pueda interactuar mejor con el mapa provisional, luego se añadió las animaciones del jugador para cada uno de sus estados:
  
  1. Inactivo
  2. Correr
  3. Saltar
  4. Caer

Luego se decidió cambiar el color del fondo del mapa para darle un poco más de vida, se decidió que el color fuera un gris claro. Posterior a esto se corrigieron algunos bugs y finalmente se subió todo el avance a Github

## Visualización del videojuego

A continuación algunas imágenes de como se visualiza el videojuego:

![Juego1](https://user-images.githubusercontent.com/132232545/236709151-904a0f03-b74e-4b0c-8675-c8ec7d3ba3c0.png)

![imagen_2023-05-07_190235777](https://user-images.githubusercontent.com/132232545/236709154-dc4a5428-8982-4823-8c03-c3798702cdd4.png)

## Controles

Al ser un juego que recién está en su primer avance, tan solo tiene las mecánicas de saltar y correr, pero a medida que el desarrollo siga avanzando se irán incrementado las mecánicas del juego y por ende los controles para ejecutarlas. Por el momento estos son sus controles:
  
  - Flecha izquierda = Moverse a la izquierda
  - Flecha derecha = Moverse a la derecha
  - Espacio = Salto del personaje
  
