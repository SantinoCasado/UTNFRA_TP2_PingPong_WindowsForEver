import pygame
import random
import math
import pygame.mixer as mixer

#Inicializar pygame
pygame.init()

#Inicializamps sonido de fondo y la perzonalizamos
mixer.init()
backround_sound = mixer.Sound("musica_fondo.mp3") # Establecemos que musica queremos
backround_sound.set_volume(0.1) # Establecemos el volumen
#Ejecutamos el sonido mientras el juego este activo
backround_sound.play()



#Sonido bullet
bullet_sound = pygame.mixer.Sound("bullet.mp3")
bullet_sound.set_volume(0.1)
collision_sound = pygame.mixer.Sound("hit_enemy.mp3")
collision_sound.set_volume(0.2)


#Configuramos la pantalla
screen = pygame.display.set_mode((800, 600))    #tupla que define el tamaño de la ventana, con 800 píxeles de ancho y 600 píxeles de alto.
pygame.display.set_caption("Space Invaders")    #Título de la ventana del juego.

#Establezco la clase jugador
class Player:
    def __init__(self):
        self.image = pygame.image.load("nave.png")
        self.x = 370    #Posicion inicial sobre x
        self.y = 480    ##Posicion inicial sobre x
        self.x_change = 0   #Cambio de posicion sobre x (movimiento)
    
    def draw(self):
        #Dibujar la nave en pantalla
        screen.blit(self.image, (self.x, self.y))
    
    def move(self):
        # Definir movimiento acutalizando la posicion en x
        self.x += self.x_change

        #Limito el movimiento dentro de los limites de la pantalla
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:  #Ancho de pantalla: 800 - Ancho de figura: 64 
            self.x = 736

#Establezco la clase para los enemigos
class Enemy:
    def __init__(self, speed):
        self.image = pygame.image.load("ovni.png")
        self.x = random.randint(0, 736) #Comienza en cualquier parte de la x
        self.y = random.randint(50, 150) #Comienzan en cualquier parte designada sobre y
        self.x_change = speed # Velociada de movimiento horizontal
        self.y_change = 40 # Distancia de bajada
    
    def draw (self):
        screen.blit(self.image, (self.x, self.y))
    
    def move(self):
        self.x += self.x_change
        # Cambiar de direccion al alcanzar los bordes
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1 #Invierto la direccion
            self.y += self.y_change # Al sumar baja la posicion del enemigo
    
    def reset_position(self, speed):
        #Reinicio la posicion del enemigo una vez destruido
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = speed 

#Creamos la clase disparo
class Bullet:
    def __init__(self):
        self.x = 0
        self.y = 480
        self.y_change = 4
        self.state = "ready" #Bandera para que solo pueda disparar una bala a la vez en pantalla

    def fire(self, x):
        # Disparar el proyectil desde la posicion del jugador
        self.state = "fire"
        self.x = x
        pygame.mixer.Sound.play(bullet_sound) #Reproduzco un sonido cada vez que dispara
    
    def move (self):
        if self.state == "fire":
            # Mover el proyectil si no hay ninguna bala en la pantalla
            self.y -= self.y_change
            #             superficie   color         x       y  ancho largo
            pygame.draw.rect(screen,(255, 0, 0), (self.x, self.y, 5, 20))
            # Restablecer el disparo si se sale de la pantalla
            if self.y <= 0:
                self.state = "ready"
                self.y = 480

#Funcion de deteccion de colisiones
def es_colision(enemy_x, enemy_y, bullet_x, bullet_y):
    distancia = math.sqrt((math.pow((enemy_x - bullet_x), 2) + math.pow((enemy_y - bullet_y), 2)))
    return distancia < 64 #Ajustable respecto al valor del tamaño de las imagenes

#Establecemos funcion para mostrar GAME OVER
def game_over_text():
    over_font = pygame.font.Font(None, 64)
    over_text = over_font.render(f"GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (250, 250))


#Definimos el score y la fuente de escritura
score = 0
font = pygame.font.Font(None, 36)

level = 1
font_level = pygame.font.Font(None, 36)

# Establecemos las vidas
lives = 5

#Creo una instancia o objeto del jugador
player = Player()

#Creo el proyectil
bullet = Bullet()

#Creo varios enemigos
num_of_enemies = 10
#Creo una lista donde alojar los enemigos en pantalla
enemies = []
initial_enemy_speed = 0.7
for i in range(num_of_enemies):
    enemies.append(Enemy(initial_enemy_speed))

#Bandera
running = True

game_over = False

while running:

    #Establezco fondo de pantalla negro (0, 0, 0) o (Red, Green, Blue)
    screen.fill((0, 0, 0))

    #Deteccion de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Si el tipo de evento que selecciona el usuario es el de salir rompe el ciclo
            running = False

        #Detecto si se presiona una tecla
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                player.x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                player.x_change = 0.5
        #Detectamos si toca la tecla de disparo
            elif event.key == pygame.K_SPACE:
                if bullet.state == "ready":
                    bullet.fire(player.x + 32) #Establezo el centrado del disparo en la nave

        #Detectar si se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0

    if not game_over:
        #Muevo y Dibujo al jugador
        player.move()
        player.draw()

        #Muevo y dibujo los enemigos
        for enemy in enemies:
            enemy.move()
            enemy.draw()

            #Verifico si hubo colision entre el enemigo y el disparo por cada enemigo en la lista
            if es_colision(enemy.x, enemy.y, bullet.x, bullet.y):
                bullet.y = 480
                bullet.state = "ready"
                score += 25
                pygame.mixer.Sound.play(collision_sound)

            # Aumentar la dificulta incrementando la velocidad de los enemigos
                if score % 500 == 0:    #Cada 5 enemigos
                    level += 1
                    initial_enemy_speed += 0.3
                    for e in enemies:
                        e.reset_position(initial_enemy_speed)
            #Si todavia no llego a la puntuacio se resetea el enemigo 
                else:
                    enemy.reset_position(initial_enemy_speed)

            #Verifico si el enmigo llego a la altura del jugador
            if enemy.y > 426:
                lives -= 1
                enemy.reset_position(initial_enemy_speed) # Una vez llegado se reinicia la posicion del enemigo
                #Una vez perdido
                if lives <= 0:
                    for e in enemies:
                        e.y = 2000 #Saco los enemigos de la pantalla
                    game_over = True

        #Mover y dibujar el disparo solo si esta "fire"
        bullet.move()


        #Mostrar la puntuacion en pantalla
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        lives_text = font.render(f"Lifes: {lives}", True, (255, 255, 255)) # Muestro las vidas restantes
        screen.blit(lives_text, (10, 40))


        #Muestro el nivel en el que se encuentra
        level_text = font.render(f"Level {level}", True, (255, 255, 255))
        screen.blit(level_text, (700, 10))

    # Si perdio
    else:
        game_over_text()
        pygame.display.flip()
        pygame.time.delay(3500)
        running = False

    #Actualizo la pantalla
    pygame.display.flip()

pygame.quit() #Se rompe el ciclo y se realiza el quit del juego