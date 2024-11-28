import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))

# Establecemos la clase jugador
class Player: 
    def __init__(self, x, y): 
        self.rect = pygame.Rect(x, y, 20, 100)
        self.y_change = 0 
        self.y_float = float(self.rect.y)  # Aseguramos que sea un flotante desde el principio

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
    
    def move(self):
        # Al igual que en la restriccion .Rect no toma muy bien los numeros flotantes sin antes ser asignados por eso utilizamos el self.y_float
        self.y_float += self.y_change 
        self.rect.y = self.y_float

        # Limitar el movimiento dentro de los límites de la pantalla
        # La restriccion la hacemos en float para evitar que las paletas sigan su curso por fuera de la pantalla a pesar que la imagen si se limita
        if self.y_float <= 0: 
            self.y_float = 0
        elif self.y_float >= 500: 
            self.y_float = 500
    