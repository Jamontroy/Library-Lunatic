import pygame

from .palette import COLORS
# from .player import Player

SCREEN_W = 600
SCREEN_H = 800

# Shelf dimensions as fractions of screen size
SHELF_W = SCREEN_W * (40 / 600)   # ~8.3% of screen width
SHELF_H = SCREEN_H * (140 / 800)  # 20% of screen height

SW, SH = int(SHELF_W), int(SHELF_H)  # shelf width/height as ints for pygame.Rect

COL_GAP = 70  # adjust to taste
TOTAL_SHELF_W = 4 * SW + 3 * COL_GAP
COL_START = (SCREEN_W - TOTAL_SHELF_W) // 2
COL_X = [COL_START + col * (SW + COL_GAP) for col in range(4)]

ROW_START = 160  # px from top of screen
ROW_GAP = 60     # gap between rows, adjust this to taste
ROW_Y = [ROW_START + row * (SH + ROW_GAP) for row in range(3)]

class Bookshelves:


    """
    this class defines the parts of the bookshelves. Computationally, there are two parts: the clamping box and the
    hit box. The clamping box stops the player from moving when it hits it visually. However the hit box (denoted as
    '..._hb' detects when a player is just near a box, and initiates the 'book drop off' method
    """

    def __init__(self) -> None:
        self.bkshlf_sprite = pygame.transform.scale((pygame.image.load("Assets/BasicBookshelf.png").convert_alpha()), (SW, SH))
        self.bkshlf_blue_sprite = pygame.transform.scale((pygame.image.load("Assets/BlueBookshelf.png").convert_alpha()), (SW, SH))
        self.bkshlf_green_sprite = pygame.transform.scale((pygame.image.load("Assets/GreenBookshelf.png").convert_alpha()), (SW, SH))
        self.bkshlf_yellow_sprite = pygame.transform.scale((pygame.image.load("Assets/YellowBookshelf.png").convert_alpha()), (SW, SH))
        self.bkshlf_purple_sprite = pygame.transform.scale((pygame.image.load("Assets/PurpleBookshelf.png").convert_alpha()), (SW, SH))
        self.bkshlf_orange_sprite = pygame.transform.scale((pygame.image.load("Assets/OrangeBookshelf.png").convert_alpha()), (SW, SH))
        self.bkshlf_red_sprite = pygame.transform.scale((pygame.image.load("Assets/RedBookshelf.png").convert_alpha()), (SW, SH))

        self.bkshlf1 = pygame.Rect(COL_X[0], ROW_Y[0], SW, SH)
        self.bkshlf1_hb = self.bkshlf1.inflate(10, 10)
        self.bkshlf2 = pygame.Rect(COL_X[1], ROW_Y[0], SW, SH)
        self.bkshlf2_hb = self.bkshlf2.inflate(10, 10)
        self.bkshlf3 = pygame.Rect(COL_X[2], ROW_Y[0], SW, SH)
        self.bkshlf3_hb = self.bkshlf3.inflate(10, 10)
        self.bkshlf4 = pygame.Rect(COL_X[3], ROW_Y[0], SW, SH)
        self.bkshlf4_hb = self.bkshlf4.inflate(10, 10)

        self.bkshlf5 = pygame.Rect(COL_X[0], ROW_Y[1], SW, SH)
        self.bkshlf5_hb = self.bkshlf5.inflate(10, 10)
        self.bkshlf6 = pygame.Rect(COL_X[1], ROW_Y[1], SW, SH)
        self.bkshlf6_hb = self.bkshlf6.inflate(10, 10)
        self.bkshlf7 = pygame.Rect(COL_X[2], ROW_Y[1], SW, SH)
        self.bkshlf7_hb = self.bkshlf7.inflate(10, 10)
        self.bkshlf8 = pygame.Rect(COL_X[3], ROW_Y[1], SW, SH)
        self.bkshlf8_hb = self.bkshlf8.inflate(10, 10)

        self.bkshlf9 = pygame.Rect(COL_X[0], ROW_Y[2], SW, SH)
        self.bkshlf9_hb = self.bkshlf9.inflate(10, 10)
        self.bkshlf10 = pygame.Rect(COL_X[1], ROW_Y[2], SW, SH)
        self.bkshlf10_hb = self.bkshlf10.inflate(10, 10)
        self.bkshlf11 = pygame.Rect(COL_X[2], ROW_Y[2], SW, SH)
        self.bkshlf11_hb = self.bkshlf11.inflate(10, 10)
        self.bkshlf12 = pygame.Rect(COL_X[3], ROW_Y[2], SW, SH)
        self.bkshlf12_hb = self.bkshlf12.inflate(10, 10)

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
        surface.blit(self.bkshlf_sprite, self.bkshlf1)
        surface.blit(self.bkshlf_red_sprite, self.bkshlf2)
        surface.blit(self.bkshlf_sprite, self.bkshlf3)
        surface.blit(self.bkshlf_blue_sprite, self.bkshlf4)
        surface.blit(self.bkshlf_yellow_sprite, self.bkshlf5)
        surface.blit(self.bkshlf_sprite, self.bkshlf6)
        surface.blit(self.bkshlf_green_sprite, self.bkshlf7)
        surface.blit(self.bkshlf_sprite, self.bkshlf8)
        surface.blit(self.bkshlf_sprite, self.bkshlf9)
        surface.blit(self.bkshlf_purple_sprite, self.bkshlf10)
        surface.blit(self.bkshlf_sprite, self.bkshlf11)
        surface.blit(self.bkshlf_orange_sprite, self.bkshlf12)