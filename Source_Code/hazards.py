import pygame

class WetFloor(pygame.sprite.Sprite):

  # class is meant to spawn wet static wet floors that the player slips on, stoppiung them for two seconds.

    WIDTH = 30
    HEIGHT = 30
    LIFESPAN = 4.0

    def __init__(self, center):
        super().__init__()
        self.rect = pygame.Rect(0,0, self.WIDTH, self.HEIGHT)
        self.rect.center = center
        self.age = 0

    def update(self, dt):
        self.age += dt
        if self.age >= self.LIFESPAN:
            self.kill()

    def draw(self, screen):
        # Placeholder visual: a semi-transparent blue rectangle
        surf = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        surf.fill((100, 149, 237, 120))  # cornflower blue, semi-transparent
        screen.blit(surf, self.rect)
        pygame.draw.rect(screen, pygame.Color("#5588cc"), self.rect, 2)

class Kid(pygame.sprite.Sprite):

    # Spawns randomly on a timer, sits still, and despawns after a while.
    # If the player collides with them while carrying books, one book is stolen.
    # Will update later such that the kids move around


    SIZE = 28
    LIFESPAN = 6.0  # seconds before the Kid despawns on their own

    def __init__(self, center):
        super().__init__()
        self.rect = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.rect.center = center
        self.age = 0.0  # tracks how long this Kid has been alive

    def update(self, dt):
        self.age += dt
        if self.age >= self.LIFESPAN:
            self.kill()

    def draw(self, screen):
        # Placeholder visual: orange square with a black border
        center = self.rect.center
        radius = self.SIZE // 2
        pygame.draw.circle(screen, pygame.Color("#FF2020"), center, radius)
        pygame.draw.circle(screen, pygame.Color("#FF8C42"), center, radius, 2)
