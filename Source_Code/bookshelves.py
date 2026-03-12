import pygame

from .palette import COLORS

class Bookshelves:

    def __init__(self) -> None:
        self.bkshlf1 = pygame.Rect(200, 200, 80, 200)
        self.bkshlf2 = pygame.Rect(600, 200, 80, 200)

        self.bkshlf3 = pygame.Rect(200, 500, 80, 200)
        self.bkshlf4 = pygame.Rect(600, 500, 80, 200)
        
        self.bkshlf5 = pygame.Rect(200, 800, 80, 200)
        self.bkshlf6 = pygame.Rect(600, 800, 80, 200)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf1)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf2)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf3)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf4)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf5)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf6)

