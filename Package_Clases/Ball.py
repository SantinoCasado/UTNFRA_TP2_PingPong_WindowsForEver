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
collision_paleta_sound = pygame.mixer.Sound("Package_Sounds/contra_paleta.mp3")

# Sonido cuando choca contra los bordes
collition_limites_sound = pygame.mixer.Sound("Package_Sounds/contra_pared.mp3")
collition_limites_sound.set_volume(60)


class Ball:  
    def __init__(self):  
        self.rect = pygame.Rect(400 - 10, 300 - 10, 20, 20)
        self.x_change = 0.1 * random.choice([-1, 1])
        self.y_change = 0.1 * random.choice([-1, 1])
        self.state = "waiting"
        
        # Pasamos a float las posiciones de x e y ya que es un Rect y esta es una forma de que se mueva a una velocidad en números con coma
        self.x_float = float(self.rect.x)        # Aseguramos que sea un flotante desde el principio
        self.y_float = float(self.rect.y)        # Aseguramos que sea un flotante desde el principio

    def draw(self):  
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self):
        # Si el jugador aprieta el espacio
        if self.state == "start":  
            self.x_float += self.x_change      # Modificamos la posición a partir de la velocidad
            self.y_float += self.y_change  

            self.rect.x = self.x_float         # Modificamos la posición actual para que realice la ejecución a una
            self.rect.y = self.y_float         # Velocidad en números con coma

        # Si rebota en los bordes superiores e inferiores
        if self.rect.y <= 0 or self.rect.y >= 580:  
            self.y_change = -self.y_change
            collition_limites_sound.play()

    # Si colisiona con una de las paletas cambia la dirección
    def check_collision(self, paddles):  
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):  
                self.x_change *= 1.1  
                self.y_change *= 1.1  
                self.x_change = -self.x_change
                collision_paleta_sound.play()
                
    # Establecemos la función de reset
    def reset(self):  
        self.rect.x = 400 - 10      # Establecemos la posición en x de reset
        self.rect.y = 300 - 10      # Establecemos la posición en y de reset

        self.x_float = self.rect.x  # Modificamos la posición actual en x a la posición de reset
        self.y_float = self.rect.y  # Modificamos la posición actual en y a la posición de reset
        
        self.x_change = 0.1 * random.choice([-1, 1])  # Volvemos a elegir un inicio aleatorio en x
        self.y_change = 0.1 * random.choice([-1, 1])  # Volvemos a elegir un inicio aleatorio en y
        
        self.state = "waiting"
