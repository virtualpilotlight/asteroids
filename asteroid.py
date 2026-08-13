import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        return super().draw(screen)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        return super().update(dt)

    def split(self):
        self.kill()
        if self <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            self.velocity.rotate(angle)
            self.velocity.rotate(-abs(angle))
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            Asteroid.draw(self, self.x, self.y, new_radius)
            Asteroid.draw(self, self.x, self.y, new_radius)
