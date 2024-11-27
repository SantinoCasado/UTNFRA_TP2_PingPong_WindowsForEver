import pygame

# Sonido cuando consigue un punto
point_sound = pygame.mixer.Sound("Sounds/punto.mp3")
point_sound.set_volume(1)

def point_player_1(ball_x):
    if ball_x >= 780:
        pygame.mixer.Sound.play(point_sound)
        return True

def point_player_2(ball_x):
    if ball_x <= 0:
        pygame.mixer.Sound.play(point_sound)
        return True