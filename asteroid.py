import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    containers= ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width= 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            # Creamos los vectores rotados sin modificar el actual
            vector1 = self.velocity.rotate(random_angle)  # Rota en una dirección
            vector2 = self.velocity.rotate(-random_angle)  # Rota en la dirección opuesta
            
            # Calcular una sola vez el nuevo radio
            radio = self.radius - ASTEROID_MIN_RADIUS

            asteroid1= Asteroid(self.position.x, self.position.y, radio)
            asteroid2= Asteroid(self.position.x, self.position.y, radio)
            
            asteroid1.velocity= vector1 * 1.2
            asteroid2.velocity= vector2 * 1.2

