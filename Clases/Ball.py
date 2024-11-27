import pygame
import random
import math
import pygame.mixer as mixer

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializamos el mixer
mixer.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))    # Tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto.    

# Sonido colisión entre la pelota y la paleta
collision_paleta_sound = pygame.mixer.Sound("Sounds/contra_paleta.mp3")

# Sonido cuando choca contra los bordes
collition_limites_sound = pygame.mixer.Sound("Sounds/contra_pared.mp3")
collition_limites_sound.set_volume(60)

class Ball: 
    def __init__(self):
        self.rect = pygame.Rect(400 - 10, 300 - 10, 20, 20)
        self.x_change = 0.1 * random.choice([-1, 1])
        self.y_change = 0.1 * random.choice([-1, 1])
        self.state = "waiting"
        # Pasamos a float las posiciones de x e y ya que es un Rect y esta es una forma de que se mueva a una velocidad en números con coma
        self.x_float = float(self.rect.x) 
        self.y_float = float(self.rect.y) 
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self, paleta_izquierda, paleta_derecha):
        # Si el jugador aprieta el espacio
        if self.state == "start":
            self.x_float += self.x_change  # Modificamos la posición a partir de la velocidad
            self.y_float += self.y_change

            self.rect.x = self.x_float  # Modificamos la posición actual para que realice la ejecución a una
            self.rect.y = self.y_float  # Velocidad en números con coma
        
        # Si rebota en los bordes superiores e inferiores
        if self.rect.y <= 0 or self.rect.y >= 580:
            pygame.mixer.Sound.play(collition_limites_sound)
            self.y_change = -self.y_change 
        
        # Si colisiona con una de las paletas cambia la dirección
        if self.rect.colliderect(paleta_izquierda.rect) or self.rect.colliderect(paleta_derecha.rect):
            pygame.mixer.Sound.play(collision_paleta_sound)
            self.x_change *= 1.1    # Aumenta la velocidad un 10% cada vez que la pelota hace un rebote.
            self.y_change *= 1.1    # Aumenta la velocidad un 10% en el eje Y también.
            self.x_change = -self.x_change  #Cambia de lado
    
    # Establecemos la función de reset
    def reset(self):
        self.rect.x = 400 - 10  # Establecemos la posición en x de reset
        self.rect.y = 300 - 10  # Establecemos la posición en y de reset

        self.x_float = self.rect.x  # Modificamos la posición actual en x a la posición de reset
        self.y_float = self.rect.y  # Modificamos la posición actual en y a la posición de reset

        self.x_change = 0.1 * random.choice([-1, 1])  # Volvemos a elegir un inicio aleatorio en x
        self.y_change = 0.1 * random.choice([-1, 1])  # Volvemos a elegir un inicio aleatorio en y

        self.state = "waiting"