import pygame
from .palette import COLORS

#I made this player movement based on the example code frow week 2, the structure and format of how it works is very similar

class Player:
    SPEED = 360.0 #These 4 attributes at the top make it super easy to change the feel of the game when we get deeper into testing
    ACCEL = 4800.0 # This is what I think felt best for right now but obviously we will tweak it the more we test.
    FRICTION = 25.0
    STOP_THRESHOLD = 20.0

    def __init__(self, SCREEN_W: int, SCREEN_H: int) -> None:
        self.w = SCREEN_W
        self.h = SCREEN_H
        self.rect = pygame.Rect(self.w // 2 - 16, self.h // 2 - 16, 32, 32)
        self.pos = pygame.Vector2(self.rect.center)
        self.velocity = pygame.Vector2(0, 0)

    def read_direction(self) -> pygame.Vector2:
        keys = pygame.key.get_pressed()
        input_x = 0.0
        input_y = 0.0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            input_x -= 1.0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            input_x += 1.0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            input_y -= 1.0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            input_y += 1.0

        direction = pygame.Vector2(input_x, input_y)
        if direction.length_squared() > 0:
            direction = direction.normalize()
        return direction

    def update(self, dt: float) -> None:
        direction = self.read_direction()

        # This accelerates towards the direction
        self.velocity += direction * self.ACCEL * dt

        # This applies the friction when there is no key pressed
        if direction.length_squared() == 0:
            self.velocity -= self.velocity * min(1.0, self.FRICTION * dt)

        # To prevent a feeling of endlessly sliding whenever the velovity is < 20 it snaps to 0
        if self.velocity.length() < self.STOP_THRESHOLD:
            self.velocity.update(0, 0)

        # Makes sure that the velocity does go beyond the capped op speed
        if self.velocity.length() > self.SPEED:
            self.velocity.scale_to_length(self.SPEED)

        # Move Code
        self.pos += self.velocity * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))
        self.rect.clamp_ip(pygame.Rect(0, 0, self.w, self.h))
        self.pos.update(self.rect.center)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, COLORS.player, self.rect, border_radius=8)