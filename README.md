Introducción

El objetivo de este ejercicio es desarrollar un juego de tenis clásico (Pong) utilizando
Pygame. Los jugadores controlarán dos paletas que deben evitar que la pelota pase
detrás de ellas. Se otorgará un punto al jugador contrario si la pelota cruza el límite de la pantalla detrás de la paleta del oponente.

Requisitos

1. Ventana del juego: LISTO
● Dimensiones: 800x600 píxeles.
● Fondo negro.

2. Elementos del juego:
● Pelota: LISTO
    ● Tamaño: cuadrado de 20x20 píxeles.
    ● Movimiento: la pelota debe moverse diagonalmente al iniciar.
● Paletas:
    ● Tamaño: rectángulos de 20 píxeles de ancho y 100 píxeles de alto.
    ● Control:
        ● Paleta izquierda: controlada por las teclas W (arriba) y S (abajo).
        ● Paleta derecha: controlada por las flechas de dirección ↑ (arriba) y ↓ (abajo).

3. Mecánicas del juego:
    ● La pelota debe rebotar en las paredes superiores e inferiores de la ventana.
    ● Si la pelota toca una paleta, debe rebotar cambiando de dirección.
    ● Si la pelota cruza el límite izquierdo o derecho de la pantalla, se suma un punto al oponente y la pelota vuelve al centro con una dirección aleatoria.

4. Sistema de puntuación:
    ● Mostrar el puntaje de ambos jugadores en la parte superior de la ventana.
    ● Cada jugador comienza con 0 puntos.
    ● El primer jugador que alcance 10 puntos gana el juego.

5. Interfaz del juego:
    ● Mensaje "Jugador 1 Gana" o "Jugador 2 Gana" cuando uno de los jugadores llegue a 10 puntos.
    ● Permitir reiniciar el juego presionando la tecla R.

6. Extras (Opcional):
    ● Aumentar gradualmente la velocidad de la pelota con cada rebote.
    ● Sonidos para:
        ● El rebote de la pelota en las paletas o paredes.
        ● La anotación de puntos.

Entregables
    ● Código fuente del juego en Python.
    ● Archivos necesarios para el correcto funcionamiento (si usas recursos externos como sonidos o fuentes personalizadas).
    ● Instrucciones breves sobre cómo ejecutar el juego.

Evaluación

El proyecto será evaluado según:
    ● Correcto funcionamiento de las mecánicas del juego.
    ● Claridad y limpieza del código (uso de funciones, comentarios, y buenas prácticas).
    ● Implementación de los extras (si aplica).

¡Buena suerte desarrollando tu juego de Pong!🎮
