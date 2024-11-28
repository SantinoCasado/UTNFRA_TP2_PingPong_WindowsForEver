import pygame

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