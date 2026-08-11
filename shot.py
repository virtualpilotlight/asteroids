from circleshape import CircleShape
from constantws import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: float, y: float, SHOT_RADIUS: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        return super().draw(screen)

    def update(self, dt: float) -> None:
        return super().update(dt)
