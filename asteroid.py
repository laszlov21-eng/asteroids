from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame
import logger
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        logger.log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        ast_1_velocity = self.velocity.rotate(random_angle)*1.2
        ast_2_velocity = self.velocity.rotate(-random_angle)*1.2
        new_radius = self.radius-ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x,self.position.y,new_radius)
        ast_2 = Asteroid(self.position.x,self.position.y,new_radius)
        ast_1.velocity = ast_1_velocity
        ast_2.velocity = ast_2_velocity