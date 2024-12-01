import pygame

screen = pygame.display.set_mode((800, 600))

def winner (player):
    over_font = pygame.font.Font(None, 64)  # Asigno la fuente del texto y el tamaño
    over_text = over_font.render(f"{player} WIN", True, (255, 0, 0))    # Printeo un mensaje con color rojo
    screen.blit(over_text, (250, 250))      # dibujo el texto sobre la pantalla