<body>
  <h1>🎮 Desarrollo de un Juego Pong con Pygame</h1>
  <p>
    En este proyecto implementé una versión clásica del juego de tenis de mesa digital, conocido como Pong, utilizando la librería Pygame. 
    El objetivo principal fue aplicar conceptos de programación orientada a objetos, manejo de eventos y renderizado gráfico en tiempo real. 
    El juego consiste en dos paletas controladas por los jugadores, que deben evitar que la pelota pase detrás de ellas. 
    Cada vez que eso ocurre, el jugador contrario suma un punto.
  </p>

  <h2>🚀 ¿Cómo ejecutar el juego?</h2>
  <p>Para correr el juego correctamente, es necesario tener instalado Python y la librería Pygame. A continuación detallo los pasos:</p>
  <ul>
    <li>✅ Tener Python 3.8 o superior instalado</li>
    <li>📦 Instalar Pygame ejecutando: <code>pip install pygame</code></li>
    <li>📁 Clonar o descargar el repositorio del proyecto</li>
    <li>▶️ Ejecutar el archivo principal con: <code>python pong.py</code></li>
  </ul>

  <h2>🖼️ Configuración visual del juego</h2>
  <h3>🖥️ Ventana del juego:</h3>
  <ul>
    <li>📐 Dimensiones: 800x600 píxeles</li>
    <li>🎨 Fondo negro para resaltar los elementos</li>
  </ul>

  <h3>🎯 Elementos principales:</h3>
  <ul>
    <li>⚽ <strong>Pelota</strong>:
      <ul>
        <li>Cuadrada, de 20x20 píxeles</li>
        <li>Inicia con movimiento diagonal</li>
      </ul>
    </li>
    <li>🧱 <strong>Paletas</strong>:
      <ul>
        <li>Rectángulos de 20 píxeles de ancho por 100 de alto</li>
        <li>Controles:
          <ul>
            <li>🅰️ Jugador 1: teclas W (arriba) y S (abajo)</li>
            <li>🅱️ Jugador 2: flechas ↑ y ↓</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

  <h2>⚙️ Lógica y mecánicas implementadas</h2>
  <ul>
    <li>La pelota rebota contra los bordes superior e inferior</li>
    <li>Al tocar una paleta, cambia de dirección</li>
    <li>Si cruza el borde izquierdo o derecho, se suma un punto al oponente y la pelota se reinicia en el centro con dirección aleatoria</li>
  </ul>

  <h2>🏆 Sistema de puntuación</h2>
  <ul>
    <li>📊 Se muestra el puntaje de ambos jugadores en la parte superior</li>
    <li>🔢 Cada jugador comienza con 0 puntos</li>
    <li>🥇 El primero en llegar a 10 puntos gana la partida</li>
  </ul>

  <h2>🖼️ Interfaz y experiencia de usuario</h2>
  <ul>
    <li>Mensaje de victoria: "Jugador 1 Gana" o "Jugador 2 Gana"</li>
    <li>Posibilidad de reiniciar el juego presionando la tecla R</li>
  </ul>

  <h2>✨ Funcionalidades extra</h2>
  <ul>
    <li>🚀 La velocidad de la pelota aumenta progresivamente con cada rebote</li>
    <li>🔊 Sonidos incorporados para:
      <ul>
        <li>Rebotes</li>
        <li>Anotaciones</li>
      </ul>
    </li>
  </ul>

  <h2>📦 Entregables del proyecto</h2>
  <ul>
    <li>🧠 Código fuente en Python</li>
    <li>🔊 Archivos de sonido y fuentes necesarias</li>
    <li>📄 Instrucciones para ejecutar el juego</li>
  </ul>

  <h2>🧪 Criterios de evaluación</h2>
  <ul>
    <li>✅ Funcionamiento correcto de las mecánicas</li>
    <li>🧹 Código limpio y bien estructurado</li>
    <li>💡 Implementación de funcionalidades extra</li>
  </ul>
</body>
</html>
