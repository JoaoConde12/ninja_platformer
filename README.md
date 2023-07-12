# Ninja Platformer

De forma general, lo que se ha hecho a lo largo de este semestre, ha sido primer indagar sobre los lenguajes de programación existentes con sus respectivas librerías y cual se adaptaría mejor para llevar acabo el desarrollo de un videojuego. Después de haber seleccionado un lenguaje, se empezó con la planificación del juego, se decidió que sería del estilo de plataformas y que tuviera entre 2 a 3 niveles, luego se pensó en tratar de implementar alguna que otra mecánica para que el juego no sea tan monótono y finalmente se dio paso al desarrollo del videojuego

## Lenguaje seleccionado y librerías

![imagen_2023-05-07_184657907](https://user-images.githubusercontent.com/132232545/236708520-f052e6a4-2f3d-40b1-8f70-2023bc6c384c.png)


El lenguaje de programación que fue elegido es Python, esto debido a que tiene un sintaxis sencilla y que a su vez permite la programación orientada a objetos, por ende iba a ser mucho más fácil la creación del juego. Adicionalmente, si bien Python no es especialmente conocido por ser un lenguaje adecuado para desarrollar videojuegos, se pensó que Python es una excelente puerta para alguien que deseé adentrarse a este mundo. Ya que a diferencia de utilizar motores gráficos conocidos como Unity o Unreal Engine, en Python no tendremos la ayuda de ese tipo de motores y por ende vamos a tener que implementar las funcionalidades que deseemos solo con código, lo que permitirá comprender de mejor manera como funcionan dichos motores y tener una mejor base de lógica de programación cuando se desee hacer juegos con algún motor gráfico.

Las principales librerías que se han usdado en este videojuego han sido 2, la primera fue Pygame; esta se encontró en esta página: https://pypi.org/project/pygame/ y para su instalación simplemente se ejecutó el comando pip install pygame en la terminal. La segunda librería fue Os-sys ya que con esta librería se pueden manipular funcionalidades dependientes del sistema operativo, como por ejemplo acceder a directorios o archivos; esta se encontró en esta página: https://pypi.org/project/os-sys/ y para su instalación fue similar a la de pygame, simplemente se escribió el comando pip install os-sys en la terminal. La primera nos permite desarrollar videojuegos en el lenguaje de Python y la segunda nos permite acceder a archivos o carpetas de manera mucho más sencilla.

## Desarrollo del videojuego

Lo primero que se hizo es establecer las medidas de la ventana, luego seleccionar un fondo de color negro y después crear una mini version de mapa (provisional) para entender el como funcionan los bloques del videojuego. Una vez hecho esto se creo una beta del jugador, el cuál era un rectángulo rojo al cual primero se le dio movimiento tanto en el eje x positivo y negativo. Después se dio paso a la creación de una cámara que pueda seguir al jugador a donde se moviera y se le dio la función de saltar.

Una vez comprobado que no hubieran problemas se le agrego las respectivas colisiones al jugador para que pueda interactuar mejor con el mapa provisional, luego se añadió las animaciones del jugador para cada uno de sus estados:
  
  1. Inactivo
  2. Correr
  3. Saltar
  4. Caer

Luego se decidió cambiar el color del fondo del mapa para darle un poco más de vida, se decidió que el color fuera un gris claro. Posterior a esto se corrigieron algunos bugs y finalmente se subió todo el primer avance del juego a Github.

Después de entender como funciona la creación del nivel de un juego, entender como funcionan las colisiones del personaje con el terreno del mismo y comprender nuevos conceptos como los sprites, se decidió ahora sí hacer un nivel mucho mejor pensado y que tenga gráficos. Para ello se usó Tiled, el cual es un editor de niveles que facilita mucho más este proceso. Aún así, al ser la primera vez usándolo, se decidió experimentar previamente con el nivel para entender como funciona, visualizar una duración ideal para los niveles y también para calcular mejor los saltos del personaje. Lo que se hizo fue crear una carpeta aparte donde se importaron los archivos csv, las texturas del nivel (con pequeñas decoraciones al ser un nivel piloto) y los enemigos pero sin colisiones con el personaje. Si bien, este paso puede parecer algo innecesario, el haberlo hecho realmente hizo que se tenga una mejor compresión de como crear un nivel.

Después de esto se procedió con el desarrollo de los niveles con la experiencia previamente adquirida, el nivel 1 es un nivel corto y sencillo, esto con el objetivo de que el jugador se acostumbre un poco a las mecánicas del juego, al movimiento de la cámara y a las colisiones; luego el nivel 2 y 3 son un poco más extensos y tienen un poco más de complejidad. A medida que se iban desarrollando los niveles, para que el juego no sea tan monótono se pensó en tratar de añadirle una nueva mecánica. Finalmente se decidió que esta nueva mecánica sea la de poder hacer un salto doble. Un poco inspirado en Mario Bross, el cual se hace grande al comer un champiñón, se decidió que el personaje al comer un champiñón pueda realizar este doble salto. Aunque esta mecánica tardó un poco en desarrollarse ya que al no tener experiencia previa en el desarrollo de videojuegos, este se desarrolló poniendo las mecánicas en las clases que se creaban y no en eventos dentro del archivo main.py.

Luego se desarrolló un menú para que el jugador avance de nivel en nivel hasta el final (el nivel 3). Obviamente para poder jugar el resto de niveles, primero debía completar el nivel previo correspondiente. Primero se desarrolló un mini-boceto de como debería lucir y funcionar el menú y luego ya se le agregó el fondo final y las texturas del menú. Lo único que quedó pendiente es añadirle una especie de temporazidor para que una vez que el personaje avance al siguiente nivel, en el menú el jugador no pueda mover su personaje a otro nivel por unos segundos. Esto con el objetivo de mejorar de forma estética al juego. Posterior al menú, se añadió una interfaz al juego donde se mostraba la barra de vida, el contador de monedas y el contador de champiñones. Con esta actualización también se añadió la colisión con enemigos y que estos puedan hacer daño al personaje si chocan con él; y también que el personaje pueda recolectar las monedas.

Por último se arregló la mecánica del doble salto que se mencionó anteriormente, ya que hasta este punto del juego el jugador tenía dobles saltos de forma ilimitada. Lo único que quedó pendiente con esta mecánica es que el contador solo se resta una vez si el número de champiñones es mayor o igual a 2, es decir si el jugador tiene 2 doble saltos disponibles los podrá realizar sin problema pero en el contador solo se verá que solo se realizó 1. Para solucionar esto es simplemente no añadir más de 2 champiñones por nivel o en caso de hacerlo, antes de que el jugador pueda recolectar el segundo forzarlo a hacer un doble salto para que el contador no se trabe. Finalmente se le agregó la música al juego (tanto la música de fondo y los efectos) y la mecánica al champiñón naranja o amarillo que aumente la vida del jugador en caso de que este no la tenga completa. 

## Visualización del videojuego

Imágenes del primer avance del videojuego (07/05/2023):

![Juego1](https://user-images.githubusercontent.com/132232545/236709151-904a0f03-b74e-4b0c-8675-c8ec7d3ba3c0.png)

![imagen_2023-05-07_190235777](https://user-images.githubusercontent.com/132232545/236709154-dc4a5428-8982-4823-8c03-c3798702cdd4.png)

Imágenes con el nivel piloto usando Tiled (26/05/2023):

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/b5cdd10b-0897-4169-847c-7d5d9105598d)

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/a7c75002-08a9-407a-ba84-0f3ab23d12d3)

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/72eafcf4-2a0e-4d0a-ac72-dffbba1db051)

Imagenes ya con los niveles finalizados del juego (06/06/2023):

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/f441228b-16bf-4cae-9dad-f5c172204561)

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/352e28f0-d9dd-4c09-adf0-43466ccfb47e)

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/53e9e48c-a17e-42ac-b6b4-bfa952da2df1)

Imagen del menú del juego (16/06/2023):

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/59551a03-7d84-44d4-9186-d633038da155)

Desarrollo del juego finalizado (12/07/2023):

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/3a7527b8-b44f-49e6-875e-3c34706dc1b0)

## Controles

Al ser un juego que recién está en su primer avance, tan solo tiene las mecánicas de saltar y correr, pero a medida que el desarrollo siga avanzando se irán incrementado las mecánicas del juego y por ende los controles para ejecutarlas. Por el momento estos son sus controles:
  
  - Flecha izquierda = Moverse a la izquierda
  - Flecha derecha = Moverse a la derecha
  - Espacio = Salto del personaje

## Elementos funcionales del juego

Por último, hay ciertos elementos en el juego o decoraciones que tienen ciertas funcionalidades detro del mismo, ya sea para ayudar al personaje o que tengan también colisiones. El primer elemento decorativo que tuvo un tipo de funcionalidad es las cajas, en estas tanto los personajes como los enemigos pueden colisionar con ellas, lo cual permite que cambie un poco la funcionalidad del juego ya que dependiendo donde están colocadas estas cajas el personaje puede llegar con un salto a plataformas más altas de manera mucho más sencilla. El siguiente elemento son las monedas, las cuales pueden ser recolectadas y se muestran en la parte superior izquierda de la pantalla (abajo de la barra de vida), estas dependiendo del tipo de moneda pueden valer $1 o $5, las monedas de oro valen $5 y las de plata $1.

Los otros dos elementos del juego que añaden nuevas mecánicas o funcionalidades son los champiñones, en este juego hay de 2 tipos: El champiñón rosado y el champiñón naranja o amarillo. El champiñón rosado lo que permite es que el personaje tenga un doble salto cuando el jugador agarra 1. Para que al jugador se le haga más fácil el saber cuando tiene permitido o no el doble salto, en la parte superior derecha de la pantalla hay un contador, cuando el jugador agarra un champiñón rosado este incrementa en 1 y una vez que el jugador realice el doble salto este resta. Finalmente se tiene al champiñón naranja o amarillo, este originalmente estaba pensado para que sirva como elemento decorativo (sin ninguna funcionalidad), pero al final se decidió que al agarrarlo le sume 10 de vida al jugador, claro está que si el jugador está con la vida completa su vida no será aumentada. 

Jugador haciendo el doble salto:

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/0a2f7760-74fa-4704-9bb1-c7b0c6077d4c)

Jugador recuperando vida:

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/249115a3-60f6-48f5-a8a4-95908ed05656)

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/62cf16cf-bcb4-48dc-927e-009e0f8c609f)

Contador de monedas:

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/b6b2e6d8-9bd8-447b-8951-b06c0978c5d3)

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/74c5c51a-ea5e-47ce-857d-b44637a429bf)

Colision con caja:

![image](https://github.com/JoaoConde12/ninja_platformer/assets/132232545/7f9ec65f-f9dc-4edb-9a6e-406b1707bbfc)



