import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y

        # in the Player class
        def triangle(self) -> list[pygame.Vector2]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            a = self.position + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            return [a, b, c]

        #test_tri = triangle

    rotation = 0

    pygame.draw.polygon(screen, "white", a, b, c, LINE_WIDTH)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

player_ch = player(x, y)
