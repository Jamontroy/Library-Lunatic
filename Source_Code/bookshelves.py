import pygame

from .palette import COLORS
# from .player import Player

class Bookshelves:

    def __init__(self) -> None:
        self.bkshlf1 = pygame.Rect(80, 100, 50, 160)  #Okay, I know the x values for these looks like I randomly chose them, but they are mathmatically equidistant from each other
        self.bkshlf2 = pygame.Rect(178, 100, 50, 160) # Each shelf is 50px wide there are 4 shelves to fit evenly in 600px | 600px - 200px = 400px
                                                        # Since there are 5 hall gaps, we divide 400/5 = 80
        self.bkshlf3 = pygame.Rect(276, 100, 50, 160) # For each x value it after the first (80) it is previous value + 50px + 48px = 210px
        self.bkshlf4 = pygame.Rect(374, 100, 50, 160) # It looks off but its just math ;)
        self.bkshlf5 = pygame.Rect(472, 100, 50, 160)  

        self.bkshlf6 = pygame.Rect(80, 308, 50, 160)                                                         
        self.bkshlf7 = pygame.Rect(178, 308, 50, 160) 
        self.bkshlf8 = pygame.Rect(276, 308, 50, 160)
        self.bkshlf9 = pygame.Rect(374, 308, 50, 160)  
        self.bkshlf10 = pygame.Rect(472, 308, 50, 160)  

        self.bkshlf11 = pygame.Rect(80, 516, 50, 160) 
        self.bkshlf12 = pygame.Rect(178, 516, 50, 160)
        self.bkshlf13 = pygame.Rect(276, 516, 50, 160)
        self.bkshlf14 = pygame.Rect(374, 516, 50, 160)  
        self.bkshlf15 = pygame.Rect(472, 516, 50, 160) 


    #def update(self, dt: float) -> None:
        #This is where the collision code will likely go
        #In addition to probably having to update the player collision as well

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf1)
        pygame.draw.rect(surface, COLORS.shelf_red, self.bkshlf2)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf3)
        pygame.draw.rect(surface, COLORS.shelf_blue, self.bkshlf4)
        pygame.draw.rect(surface, COLORS.shelf_yellow, self.bkshlf5)
        pygame.draw.rect(surface, COLORS.shelf_green, self.bkshlf6)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf7)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf8)
        pygame.draw.rect(surface, COLORS.shelf_orange, self.bkshlf9)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf10)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf11)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf12)
        pygame.draw.rect(surface, COLORS.shelf_purple, self.bkshlf13)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf14)
        pygame.draw.rect(surface, COLORS.shelf_brown, self.bkshlf15)
        

