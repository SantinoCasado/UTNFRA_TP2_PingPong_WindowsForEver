import pygame
import random
import math
import pygame.mixer as mixer

# Inicializamos el pygame
pygame.init()

# Inicializamos el mixer
mixer.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))    # Tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto.
pygame.display.set_caption("Ping Pong")         # Título de la ventana del juego.

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sonido colisión entre la pelota y la paleta
collision_paleta_sound = pygame.mixer.Sound("contra_paleta.mp3")

# Sonido cuando choca contra los bordes
collition_limites_sound = pygame.mixer.Sound("contra_pared.mp3")
collition_limites_sound.set_volume(60)

# Sonido cuando consigue un punto
point_sound = pygame.mixer.Sound("punto.mp3")
point_sound.set_volume(1)

#Inicializo los puntajes
player_1_score = 0
player_2_score = 0
font_score = pygame.font.Font(None, 64)

# Establecemos clase Pelota
class Ball: 
    def __init__(self):
        self.rect = pygame.Rect(400 - 10, 300 - 10, 20, 20)
        self.x_change = 1 * random.choice([-1, 1])
        self.y_change = 1 * random.choice([-1, 1])
        self.state = "waiting"
        # Pasamos a float las posiciones de x e y ya que es un Rect y esta es una forma de que se mueva a una velocidad en números con coma
        self.x_float = self.rect.x 
        self.y_float = self.rect.y 
        
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

        self.x_change = 1 * random.choice([-1, 1])  # Volvemos a elegir un inicio aleatorio en x
        self.y_change = 1 * random.choice([-1, 1])  # Volvemos a elegir un inicio aleatorio en y

        self.state = "waiting"

# Establecemos la clase jugador
class Player: 
    def __init__(self, x, y): 
        self.rect = pygame.Rect(x, y, 20, 100)
        self.y_change = 0 
        self.y_float = self.rect.y 

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
    
    def move(self):
        self.y_float += self.y_change 
        self.rect.y = self.y_float

        # Limitar el movimiento dentro de los límites de la pantalla
        if self.rect.y <= 0: 
            self.rect.y = 0
        elif self.rect.y >= 500: 
            self.rect.y = 500

def point_player_1(ball_x):
    if ball_x >= 780:
        pygame.mixer.Sound.play(point_sound)
        return True

def point_player_2(ball_x):
    if ball_x <= 0:
        pygame.mixer.Sound.play(point_sound)
        return True

def winner (player):
    over_font = pygame.font.Font(None, 64)
    over_text = over_font.render(f"{player} WIN", True, (255, 0, 0))
    screen.blit(over_text, (250, 250))

status = "playing"

player_1 = Player(780, 300)
player_2 = Player(0, 300)

ball = Ball()
# Bandera
running = True

while running:
    # Establezco fondo de pantalla negro (0, 0, 0)
    screen.fill(BLACK)

    # Detección de eventos
    for event in pygame.event.get():
        # Si quitea
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Player 1
            if event.key == pygame.K_DOWN: 
                player_1.y_change = 0.3 
            elif event.key == pygame.K_UP: 
                player_1.y_change = -0.3
            
            # Player 2
            elif event.key == pygame.K_w: 
                player_2.y_change = -0.3 
            elif event.key == pygame.K_s: 
                player_2.y_change = 0.3

            # Si aprieta el espacio inicia el partido
            elif event.key == pygame.K_SPACE: 
                if ball.state == "waiting": 
                    ball.state = "start"

            # Si aprieta la "r" vuelve al inicio
            elif event.key == pygame.K_r:
                ball.reset()
                player_1_score = 0
                player_2_score = 0
                status = "playing"

        # Detectar si se suelta la tecla
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_1.y_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                player_2.y_change = 0

    if status == "playing":
        pygame.draw.line(screen, WHITE, (400, 0), (400, 600), 2)  # Línea vertical en   el centro de la pantalla

        # Si y quien consiguió un punto
        if point_player_1(ball.rect.x):
            player_1_score += 1
            ball.reset()
        elif point_player_2(ball.rect.x):
            player_2_score += 1
            ball.reset()

        # Muevo y dibujo a los jugadores
        player_1.move()
        player_1.draw()

        player_2.move()
        player_2.draw()

        # Mover y dibujar la pelota
        ball.move(player_2, player_1)
        ball.draw()

        #Muestro por pantalla los puntajes
        score_text_p1 = font_score.render(f"{player_1_score}", True, (255, 255, 255))
        score_text_p2 = font_score.render(f"{player_2_score}", True, (255, 255, 255))
        screen.blit(score_text_p1, (325, 20))  
        screen.blit(score_text_p2, (450, 20))

        if player_1_score == 10 or player_2_score == 10:
            status = "finished"
    
    elif status == "finished":
        if player_1_score == 10:
            winner("PLAYER 1")
            pygame.display.flip()
            pygame.time.delay(3500)
            running = False

        elif player_2_score == 10:
            winner("PLAYER 2")
            pygame.display.flip()
            pygame.time.delay(3500)
            running = False

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()  # Se rompe el ciclo y se realiza el quit del juego
