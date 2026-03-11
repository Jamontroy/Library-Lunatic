import pygame
from .palette import COLORS


class Player:
    SPEED = 360.0

    def __init__(self, SCREEN_W: int, SCREEN_H: int) -> None:
        self.w = SCREEN_W
        self.h = SCREEN_H
        self.rect = pygame.Rect(self.w // 2 - 16, self.h // 2 - 16, 32, 32)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt: float) -> None:
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

        self.velocity.x = input_x * self.SPEED
        self.velocity.y = input_y * self.SPEED

        self.rect.x += int(self.velocity.x * dt)
        self.rect.y += int(self.velocity.y * dt)
        self.rect.clamp_ip(pygame.Rect(0, 0, self.w, self.h))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, COLORS.player, self.rect, border_radius=8)