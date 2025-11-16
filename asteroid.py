import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r_angle = random.uniform(20.0, 50.0)
            asteroid_1 = Asteroid(
                self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = self.velocity
            asteroid_1.velocity = asteroid_1.velocity.rotate(
                r_angle)

            asteroid_2 = Asteroid(
                self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = self.velocity * 1.2
            asteroid_2.velocity = asteroid_2.velocity.rotate(
                -r_angle)
