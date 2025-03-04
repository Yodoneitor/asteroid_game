import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import*

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")

    #Creacion de grupos
    my_group_updatable= pygame.sprite.Group() 
    my_group_drawable= pygame.sprite.Group()
    my_group_asteroids= pygame.sprite.Group()
    my_group_shots= pygame.sprite.Group()

   #Instanciar al jugador  y añadir a los grupos
    player= Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)  
    my_group_updatable.add(player)
    my_group_drawable.add(player)

    Asteroid.containers = (my_group_asteroids, my_group_updatable, my_group_drawable)

    AsteroidField.containers = (my_group_updatable,)

    Shot.containers = (my_group_updatable, my_group_drawable, my_group_shots)

    #Instanciar el campo
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60)/1000 # Actualiza el delta time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Actualizar jugador con dt
        my_group_updatable.update(dt)

        for asteroid in my_group_asteroids:
            for bullet in my_group_shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split() 

            if player.collision(asteroid):
                print("Game Over")
                sys.exit()

        #Dibujar en pantalla 
        screen.fill((0,0,0))
        for i in my_group_drawable:
            i.draw(screen)
        
        pygame.display.flip()
        
    
    
          

if __name__ == "__main__":
    main()

