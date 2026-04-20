import pygame
import random

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

# AI walkable grid cell centers (5 cols x 4 rows = 20 spots)
# These are the midpoints of the corridors between/around the shelves
H_GAPS = [80, 190, 300, 410, 520]   #Fartest left x point was 80px frather right is 520px 520-80/4 = 110px between each space
V_GAPS = [136, 331, 535, 720]       #Farthest up is 136 farthest down is 720 730-136/3 = roughly 146, I honestly eyeballed and tweaked a little with this one until it looked right.

GRID_ROWS = 4
GRID_COLS = 5

AI_SPEED = 3  # pixels per frame
WAIT_DURATION = 2.0 #ms to wait

class Pedestrian(pygame.sprite.Sprite):
    def __init__(self, start_row, start_col):
        super().__init__()

        self.hit_cooldown = 0.0
        
        self.row = start_row
        self.col = start_col

        self.pixel_x = H_GAPS[self.col]
        self.pixel_y = V_GAPS[self.row]

        self.target_x = self.pixel_x
        self.target_y = self.pixel_y

        self.wait_timer = 0
        self.is_waiting = False

        # Animations - are the exact same basically as I implemented in the player class.
        self.animations = {
            "up":    [pygame.image.load(f"Assets/PedestrianAnim/PedUp{i}.png").convert_alpha()    for i in range(1, 4)],
            "down":  [pygame.image.load(f"Assets/PedestrianAnim/PedDown{i}.png").convert_alpha()  for i in range(1, 4)],
            "left":  [pygame.image.load(f"Assets/PedestrianAnim/PedLeft{i}.png").convert_alpha()  for i in range(1, 3)],
            "right": [pygame.image.load(f"Assets/PedestrianAnim/PedRight{i}.png").convert_alpha() for i in range(1, 3)],
        }

        for key in self.animations:
            self.animations[key] = [pygame.transform.scale2x(frame) for frame in self.animations[key]]

        self.direction = "down"
        self.frame = 0
        self.anim_timer = 0
        self.ANIM_SPEED = 0.15  # slightly slower than player

        self.image = self.animations[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.pixel_x, self.pixel_y)

    def get_adjacent(self):
        candidates = [
            (self.row - 1, self.col),
            (self.row + 1, self.col),
            (self.row, self.col - 1),
            (self.row, self.col + 1),
        ]
        return [(r, c) for r, c in candidates if 0 <= r < GRID_ROWS and 0 <= c < GRID_COLS]

    def pick_next_cell(self, occupied_cells):
        adjacent = self.get_adjacent()
        free = [(r, c) for r, c in adjacent if (r, c) not in occupied_cells]

        if free:
            new_row, new_col = random.choice(free)

            # Set direction based on movement
            dr = new_row - self.row
            dc = new_col - self.col
            if dr < 0:
                self.direction = "up"
            elif dr > 0:
                self.direction = "down"
            elif dc < 0:
                self.direction = "left"
            elif dc > 0:
                self.direction = "right"

            self.frame = 0  # reset frame on direction change
            self.row, self.col = new_row, new_col

        self.target_x = H_GAPS[self.col]
        self.target_y = V_GAPS[self.row]

    def update(self, dt, occupied_cells):
        if self.is_waiting:
            self.wait_timer += dt
            if self.wait_timer >= WAIT_DURATION:
                self.wait_timer = 0
                self.is_waiting = False
                self.pick_next_cell(occupied_cells)
        else:
            dx = self.target_x - self.pixel_x
            dy = self.target_y - self.pixel_y

            if abs(dx) <= AI_SPEED and abs(dy) <= AI_SPEED:
                self.pixel_x = self.target_x
                self.pixel_y = self.target_y
                self.is_waiting = True
                self.frame = 0  # snap to idle when stopped
            else:
                if abs(dx) > 0:
                    self.pixel_x += AI_SPEED * (1 if dx > 0 else -1)
                if abs(dy) > 0:
                    self.pixel_y += AI_SPEED * (1 if dy > 0 else -1)

                # Advance animation while walking
                self.anim_timer += dt
                if self.anim_timer >= self.ANIM_SPEED:
                    self.anim_timer = 0
                    self.frame = (self.frame + 1) % len(self.animations[self.direction])

            self.rect.center = (self.pixel_x, self.pixel_y)

        # Update image each frame
        self.image = self.animations[self.direction][self.frame]

    def draw(self, surface):
        surface.blit(self.image, self.rect)