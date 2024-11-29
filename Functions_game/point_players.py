import pygame

# Inicializar pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

#Incializo el cartel de Match Point
match_point_txt = "¡MATCH POINT!"
font_match_point = pygame.font.Font(None, 32)

# Sonido cuando consigue un punto
point_sound = pygame.mixer.Sound("Sounds/punto.mp3")
point_sound.set_volume(1)   # Seteo el volumen del audio (Estaba re fuerte al principio xD)

def point_player_1(ball_x):
    if ball_x >= 780:    # Cuando la pelota llega al borde de la pantalla izquierda es punto del jugador 1
        pygame.mixer.Sound.play(point_sound)
        return True

def point_player_2(ball_x):
    if ball_x <= 0:     # Cuando la pelota llega al borde de la pantalla izquierda es punto del jugador 2
        pygame.mixer.Sound.play(point_sound)
        return True

# En el caso de que uno de los jugadores consiga 9 puntos se mostrara el texto: "¡MATCH POINT! y se generara un audio"
def match_point(player_1_score, player_2_score):
    if (player_1_score == 9 or player_2_score == 9):
        text_match_point = font_match_point.render(f"{match_point_txt}", True, (255, 0, 0))
        screen.blit(text_match_point, (314, 65))
        return True