import pygame
import random
import pygame.mixer as mixer

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializamos Pygame y el mixer
pygame.init()
mixer.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))

# Carga de sonidos
collision_paleta_sound = pygame.mixer.Sound("Package_Sounds/contra_paleta.mp3")
collision_paleta_sound.set_volume(0.6)  # Ajustamos volumen entre 0 y 1

collition_limites_sound = pygame.mixer.Sound("Package_Sounds/contra_pared.mp3")
collition_limites_sound.set_volume(0.6)

# Establecemos la clase jugador
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)
        self.y_change = 0.0
        self.y_float = float(self.rect.y)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self):
        self.y_float += self.y_change
        self.rect.y = round(self.y_float)  # Redondeamos para evitar errores en rect
        
        # Limitar movimiento dentro de los límites de la pantalla
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y_float = 0  # Aseguramos que no siga desplazándose
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.y_float = 500

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            ball.x_change = -ball.x_change * 1.1  # Aumentamos velocidad tras impacto
            collision_paleta_sound.play()  # Sonido de colisión con la paleta
