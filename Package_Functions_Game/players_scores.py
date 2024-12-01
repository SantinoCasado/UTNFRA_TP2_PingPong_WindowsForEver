import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
font_score = pygame.font.Font(None, 64)
font_players = pygame.font.Font(None, 32)

def players_score (player_1_score, player_2_score):
    #Muestro por pantalla los puntajes
    score_text_p1 = font_score.render(f"{player_1_score}", True, (255, 255, 255))
    score_text_p2 = font_score.render(f"{player_2_score}", True, (255, 255, 255))

    #Muestro por pantalla a que jugador pertenece el puntaje
    player_1_text = font_players.render("Player 1", True, (255, 0, 0))
    player_2_text = font_players.render("Player 2", True, (255, 0, 0))

    #Nombres
    screen.blit(player_1_text, (300, 10))
    screen.blit(player_2_text, (420, 10))

    #Puntajes
    screen.blit(score_text_p1, (325, 40))  
    screen.blit(score_text_p2, (450, 40))