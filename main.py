import pygame
import pygame.mixer as mixer
from Clases import *
from Functions_game.point_players import point_player_1, point_player_2
from Functions_game.winner import winner


# Inicializamos el pygame
pygame.init()

# Inicializamos el mixer
mixer.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))    # Tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto.
pygame.display.set_caption("Ping Pong")         # Título de la ventana del juego.

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Inicializo los puntajes
player_1_score = 0
player_2_score = 0
font_score = pygame.font.Font(None, 64)

#Incializo el cartel de Match Point
match_point_txt = "¡MATCH POINT!"
font_match_point = pygame.font.Font(None, 32)

status = "playing"

#Inicializo los jugadores
player_1 = Player(780, 300)
player_2 = Player(0, 300)

#Inicializo la pelota
ball = Ball()
# Bandera
running = True

while running:
    # Establezco fondo de pantalla negro (0, 0, 0)
    screen.fill(BLACK)

    # Detección de eventos
    for event in pygame.event.get():
        match event.type:
            #Detecta si sale del juego
            case pygame.QUIT:
                running = False
            # Deteccion de eventos cuanto APRIETA una tecla
            case pygame.KEYDOWN:
                match event.key:
                    # Player 1
                    case pygame.K_DOWN:
                        player_1.y_change = 0.3 
                    case pygame.K_UP:
                        player_1.y_change = -0.3

                    # Player 2
                    case pygame.K_w: 
                        player_2.y_change = -0.3
                    case pygame.K_s: 
                        player_2.y_change = 0.3

                    # Si aprieta el espacio inicia el partido
                    case pygame.K_SPACE: 
                        if ball.state == "waiting": 
                            ball.state = "start"
                    
                    # Si aprieta la "r" vuelve al inicio
                    case pygame.K_r:
                        ball.reset()
                        player_1_score = 0
                        player_2_score = 0
                        status = "playing"

            # Detectar si se SUELTA la tecla
            case pygame.KEYUP:
                match event.key:
                    #Player 1
                    case pygame.K_UP:
                        player_1.y_change = 0
                    case pygame.K_DOWN:
                        player_1.y_change = 0
                    #Player 2
                    case pygame.K_w:
                        player_2.y_change = 0
                    case pygame.K_s:
                        player_2.y_change = 0

    # Mientras que la partida este en proceso
    if status == "playing":
        pygame.draw.line(screen, WHITE, (400, 0), (400, 600), 2)  # Línea vertical en  el centro de la pantalla

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

        if player_1_score == 9 or player_2_score == 9:
            text_match_point = font_match_point.render(f"{match_point_txt}", True, (255, 0, 0))
            screen.blit(text_match_point, (314 , 65))

        # Cuando uno de los jugadores logra 10 puntos se termina el juego
        if player_1_score == 10 or player_2_score == 10:
            status = "finished"
    
    # Si el juego esta terminado
    elif status == "finished":
        # Si fue el player 1 quien consiguio los 10 puntos
        if player_1_score == 10:
            winner("PLAYER 1")
            pygame.display.flip()   # Actualizo la pantalla
            pygame.time.delay(3500) # Una vez terminado el juego dejo la venta abierta unos segundos
            running = False         # Termino el juego

        # Si fue el player 2 quien consiguio los 10 puntos
        elif player_2_score == 10:
            winner("PLAYER 2")
            pygame.display.flip()   
            pygame.time.delay(3500) 
            running = False         

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()  # Se rompe el ciclo y se realiza el quit del juego
