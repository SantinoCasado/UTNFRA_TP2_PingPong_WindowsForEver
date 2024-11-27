import pygame

screen = pygame.display.set_mode((800, 600))

def winner (player):
    over_font = pygame.font.Font(None, 64)
    over_text = over_font.render(f"{player} WIN", True, (255, 0, 0))
    screen.blit(over_text, (250, 250))