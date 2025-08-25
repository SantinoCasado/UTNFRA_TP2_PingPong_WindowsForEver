<h1>🎮 Introducción</h1>
<p>
El objetivo de este ejercicio es desarrollar un juego de tenis clásico (Pong) utilizando Pygame. Los jugadores controlarán dos paletas que deben evitar que la pelota pase detrás de ellas. Se otorgará un punto al jugador contrario si la pelota cruza el límite de la pantalla detrás de la paleta del oponente.
</p>

<h2>🧾 Requisitos</h2>

<h3>🖥️ Ventana del juego:</h3>
<ul>
  <li>📐 Dimensiones: 800x600 píxeles</li>
  <li>🎨 Fondo negro</li>
</ul>

<h3>🎯 Elementos del juego</h3>
<ul>
  <li>⚽ Pelota:
    <ul>
      <li>Tamaño: cuadrado de 20x20 píxeles</li>
      <li>Movimiento: la pelota debe moverse diagonalmente al iniciar</li>
    </ul>
  </li>
  <li>🧱 Paletas:
    <ul>
      <li>Tamaño: rectángulos de 20 píxeles de ancho y 100 píxeles de alto</li>
      <li>Control:
        <ul>
          <li>🅰️ Paleta izquierda: teclas W (arriba) y S (abajo)</li>
          <li>🅱️ Paleta derecha: flechas ↑ (arriba) y ↓ (abajo)</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h3>⚙️ Mecánicas del juego</h3>
<ul>
  <li>La pelota debe rebotar en las paredes superiores e inferiores</li>
  <li>Si la pelota toca una paleta, debe rebotar cambiando de dirección</li>
  <li>Si cruza el límite izquierdo o derecho, se suma un punto al oponente y la pelota vuelve al centro con dirección aleatoria</li>
</ul>

<h3>🏆 Sistema de puntuación</h3>
<ul>
  <li>📊 Mostrar el puntaje de ambos jugadores en la parte superior</li>
  <li>🔢 Cada jugador comienza con 0 puntos</li>
  <li>🥇 El primer jugador que alcance 10 puntos gana</li>
</ul>

<h3>🖼️ Interfaz del juego</h3>
<ul>
  <li>Mensaje "Jugador 1 Gana" o "Jugador 2 Gana" al llegar a 10 puntos</li>
  <li>Permitir reiniciar el juego con la tecla R</li>
</ul>

<h3>✨ Extras</h3>
<ul>
  <li>🚀 Aumentar gradualmente la velocidad de la pelota con cada rebote</li>
  <li>🔊 Sonidos para:
    <ul>
      <li>Rebote en paletas o paredes</li>
      <li>Anotación de puntos</li>
    </ul>
  </li>
</ul>

<h2>📦 Entregables</h2>
<ul>
  <li>Código fuente del juego en Python</li>
  <li>Archivos necesarios para el funcionamiento (sonidos, fuentes, etc.)</li>
  <li>Instrucciones breves sobre cómo ejecutar el juego</li>
</ul>

<h2>🧪 Evaluación</h2>
<ul>
  <li>✅ Correcto funcionamiento de las mecánicas</li>
  <li>🧹 Claridad y limpieza del código (funciones, comentarios, buenas prácticas)</li>
  <li>💡 Implementación de los extras (si aplica)</li>
</ul>
