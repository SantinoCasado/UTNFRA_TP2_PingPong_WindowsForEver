import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))

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