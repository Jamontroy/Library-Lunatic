import pygame

from .palette import COLORS
# from .player import Player

class Bookshelves:


    """
    this class defines the parts of the bookshelves. Computationally, there are two parts: the clamping box and the
    hit box. The clamping box stops the player from moving when it hits it visually. However the hit box (denoted as
    '..._hb' detects when a player is just near a box, and initiates the 'book drop off' method
    """

    def __init__(self) -> None:
        self.bkshlf1 = pygame.Rect(77, 100, 50, 160)  # Okay, I know the x values for these looks like I randomly chose them, but they are mathmatically equidistant from each other
        self.bkshlf1_hb = self.bkshlf1.inflate(10,10) # Each shelf is 60px wide there are 4 shelves to fit evenly in 600px | 600px - 240px = 360px
        self.bkshlf2 = pygame.Rect(209, 100, 50, 160) # Since there are 5 hall gaps, we divide 360/5 = 72
        self.bkshlf2_hb = self.bkshlf2.inflate(10,10)

        self.bkshlf3 = pygame.Rect(341, 100, 50, 160) # For each x value it after the first (72) it is previous value + 60px + 72px = 204px
        self.bkshlf3_hb = self.bkshlf3.inflate(10,10) # It looks off but its just math ;)
        self.bkshlf4 = pygame.Rect(473, 100, 50, 160)
        self.bkshlf4_hb = self.bkshlf4.inflate(10,10)

        self.bkshlf5 = pygame.Rect(78, 332, 50, 160)
        self.bkshlf5_hb = self.bkshlf5.inflate(10,10) # Added in an "hb" (hitbox) rect for all the shelves for the player to collide with
        self.bkshlf6 = pygame.Rect(209, 332, 50, 160)
        self.bkshlf6_hb = self.bkshlf6.inflate(10,10)
        self.bkshlf7 = pygame.Rect(341, 332, 50, 160)
        self.bkshlf7_hb = self.bkshlf7.inflate(10,10)
        self.bkshlf8 = pygame.Rect(473, 332, 50, 160)
        self.bkshlf8_hb = self.bkshlf8.inflate(10,10)

        self.bkshlf9 = pygame.Rect(77, 564, 50, 160)
        self.bkshlf9_hb = self.bkshlf9.inflate(10,10)
        self.bkshlf10 = pygame.Rect(209, 564, 50, 160)
        self.bkshlf10_hb = self.bkshlf10.inflate(10,10)
        self.bkshlf11 = pygame.Rect(341, 564, 50, 160)
        self.bkshlf11_hb = self.bkshlf11.inflate(10,10)
        self.bkshlf12 = pygame.Rect(473, 564, 50, 160)
        self.bkshlf12_hb = self.bkshlf12.inflate(10,10)

        self.color_tag= { # assigns shelf hitboxes to colors
            "red": self.bkshlf2_hb,
            "blue": self.bkshlf4_hb,
            "yellow": self.bkshlf5_hb,
            "green": self.bkshlf7_hb,
            "purple": self.bkshlf10_hb,
            "orange": self.bkshlf12_hb,
        }


    #def update(self, dt: float) -> None:
        #This is where the collision code will likely go
        #In addition to probably having to update the player collision as well

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf1)
        pygame.draw.rect(surface, COLORS.shelf_red, self.bkshlf2)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf3)
        pygame.draw.rect(surface, COLORS.shelf_blue, self.bkshlf4)
        pygame.draw.rect(surface, COLORS.shelf_yellow, self.bkshlf5)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf6)
        pygame.draw.rect(surface, COLORS.shelf_green, self.bkshlf7)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf8)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf9)
        pygame.draw.rect(surface, COLORS.shelf_purple, self.bkshlf10)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf11)
        pygame.draw.rect(surface, COLORS.shelf_orange, self.bkshlf12)
        

