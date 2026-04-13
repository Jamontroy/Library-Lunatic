import pygame
from .palette import COLORS

#I made this player movement based on the example code frow week 2, the structure and format of how it works is very similar

NUM_FRAMES = 4  # change this to however many frames each direction has

class Player:
    SPEED = 300.0 #These 4 attributes at the top make it super easy to change the feel of the game when we get deeper into testing
    BOOSTED_SPEED = 500.0
    ACCEL = 4800.0 # This is what I think felt best for right now but obviously we will tweak it the more we test.
    FRICTION = 100.0
    STOP_THRESHOLD = 20.0
    BOOST_DURATION = 5.0  # seconds the boost lasts

    def __init__(self, SCREEN_W: int, SCREEN_H: int) -> None:
        self.w = SCREEN_W
        self.h = SCREEN_H
        self.rect = pygame.Rect(self.w // 2 - 16, self.h // 2 - 16, 32, 32)
        self.pos = pygame.Vector2(self.rect.center)
        self.velocity = pygame.Vector2(0, 0)
        self.score = 0  # tracks player score
        self.bookscarried = []
        self.boost_timer = 0.0  # tracks how long boost has left

        self.playeranimations = {
            "up":    [pygame.image.load(f"Assets/PlayerAnim/PlayerUp{i}.png").convert_alpha()    for i in range(1, 4)],
            "down":  [pygame.image.load(f"Assets/PlayerAnim/PlayerDown{i}.png").convert_alpha()  for i in range(1, 4)],
            "left":  [pygame.image.load(f"Assets/PlayerAnim/PlayerLeft{i}.png").convert_alpha()  for i in range(1, 3)],
            "right": [pygame.image.load(f"Assets/PlayerAnim/PlayerRight{i}.png").convert_alpha() for i in range(1, 3)],
        }

        for key in self.playeranimations:
            self.playeranimations[key] = [pygame.transform.scale2x(frame) for frame in self.playeranimations[key]]

        self.direction = "down"  # default facing direction
        self.frame = 0           # current frame index
        self.anim_timer = 0      # tracks time between frames
        self.ANIM_SPEED = 0.1    # seconds per frame, adjust to taste

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

        new_direction = self.direction
        if direction.y < 0:
            new_direction = "up"
        elif direction.y > 0:
            new_direction = "down"
        elif direction.x < 0:
            new_direction = "left"
        elif direction.x > 0:
            new_direction = "right"

        if new_direction != self.direction:
            self.direction = new_direction
            self.frame = 0  # reset frame when direction changes

        # Advance animation frame if moving
        if direction.length_squared() > 0:
            self.anim_timer += dt
            if self.anim_timer >= self.ANIM_SPEED:
                self.anim_timer = 0
                self.frame = (self.frame + 1) % len(self.playeranimations[self.direction])
        else:
            self.frame = 0  # snap back to idle frame when still

        # This accelerates towards the direction
        self.velocity += direction * self.ACCEL * dt

        # This applies the friction when there is no key pressed
        if direction.length_squared() == 0:
            self.velocity -= self.velocity * min(1.0, self.FRICTION * dt)

        # To prevent a feeling of endlessly sliding whenever the velovity is < 20 it snaps to 0
        if self.velocity.length() < self.STOP_THRESHOLD:
            self.velocity.update(0, 0)

        # Makes sure that the velocity does go beyond the capped op speed
        if self.boost_timer > 0:
            self.boost_timer -= dt
            top_speed = self.BOOSTED_SPEED
        else:
            top_speed = self.SPEED

        if self.velocity.length() > top_speed:
            self.velocity.scale_to_length(top_speed)
        # Move Code
        self.pos += self.velocity * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))
        self.rect.clamp_ip(pygame.Rect(0, 0, self.w, self.h))
        self.pos.update(self.rect.center)

    def draw(self, surface: pygame.Surface) -> None:
        current_frame = self.playeranimations[self.direction][self.frame]
        surface.blit(current_frame, self.rect)