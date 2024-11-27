import pygame
import random
import math
import pygame.mixer as mixer


#Inicializamos el pygame
pygame.init()

#Configuracion de la pantalla
screen = pygame.display.set_mode((800, 600))    #tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto.
pygame.display.set_caption("Ping Pong")         #Título de la ventana del juego.

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Esablecemos clase Pelota
class Ball: 
    def __init__(self): 
        self.rect = pygame.Rect(800 // 2, 600 // 2, 20, 20)
        self.x_change = 0.1 * random.choice([-1, 1]) 
        self.y_change = 0.1 * random.choice([-1, 1]) 
        self.state = "waiting"
        #Pasamos a float las posciones de  x e y ya que es un Rect y esta es una forma de que se mueva a una velocidad en numeros con coma
        self.x_float = self.rect.x 
        self.y_float = self.rect.y 
        
    def draw(self): 
        pygame.draw.rect(screen, WHITE, self.rect)

    def move(self, paleta_izquierda, paleta_derecha):
        #Si el jugador apreta el spacio
        if self.state == "start":

            self.x_float += self.x_change #Modificamos la posicion a partir de la velocidad
            self.y_float += self.y_change 

            self.rect.x = self.x_float  #Mofificamos la posicion actual para que realize la ejecucion a una
            self.rect.y = self.y_float  #velocidad en numeros con coma
        
        # Si rebota en los bordes superiores e inferiores  
        if self.rect.y <= 0 or self.rect.y >= 580: 
            self.y_change = -self.y_change 
        
        # Si se consigue un punto vuelve a la poscion incial
        if self.rect.x <= 0: 
            self.reset() 
        elif self.rect.x >= 780:
            self.reset()
        
        #Si coliciona con una de las paletas cambia la direccion
        #El .colliderect devuelve un booleano si colicionaron o no dos .Rect
        if self.rect.colliderect(paleta_izquierda.rect) or self.rect.colliderect(paleta_derecha.rect): 
            self.x_change = -self.x_change 
    
    #Establecemos la funcion de reset
    def reset(self): 
        self.rect.x = 800 // 2  #Esatblecemos la posicion en x de reset
        self.rect.y = 600 // 2  #Establecemos la posicion en y de reset

        self.x_float = self.rect.x  #Modificamos la posicion actual en x a la posicion de reset
        self.y_float = self.rect.y  #Modificamos la posicion actual en y a la poscion de reset

        self.x_change = 0.1 * random.choice([-1, 1]) #Volvemos a elegir un inicio aleatorio en x
        self.y_change = 0.1 * random.choice([-1, 1]) #Volvemos a elegir un inicio aleatorio en y

        self.state = "waiting"

#Establecemos la clase jugador
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


player_1 = Player(780, 300)
player_2 = Player(0, 300)

ball = Ball()
#Bandera
running = True

while running:

    #Establezco fondo de pantalla negro (0, 0, 0) o (Red, Green, Blue)
    screen.fill(BLACK)

    #Deteccion de eventos
    for event in pygame.event.get():
        #Si quitea
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #Player 1
            if event.key == pygame.K_DOWN: 
                player_1.y_change = 0.3 
            elif event.key == pygame.K_UP: 
                player_1.y_change = -0.3
            
            #Player 2
            elif event.key == pygame.K_w: 
                player_2.y_change = -0.3 
            elif event.key == pygame.K_s: 
                player_2.y_change = 0.3

            #Si apreta el espacio inicia el partido
            elif event.key == pygame.K_SPACE: 
                if ball.state == "waiting": 
                    ball.state = "start"

            #Si apreta la "r" vuelve al inicio
            elif event.key == pygame.K_r:
                ball.reset()


        #Detectar si se suelta la tecla
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_1.y_change= 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                player_2.y_change = 0

    #Muevo y Dibujo a los jugadores
    player_1.move()
    player_1.draw()

    player_2.move()
    player_2.draw()
    
    #Dibujo la pelota en la posicion inicial
    ball.move(player_2, player_1)
    ball.draw()

    #Actualizo la pantalla
    pygame.display.flip()

pygame.quit() #Se rompe el ciclo y se realiza el quit del juego