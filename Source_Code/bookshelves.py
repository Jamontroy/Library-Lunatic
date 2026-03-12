import pygame

from .palette import COLORS
# from .player import Player

class Bookshelves:

    def __init__(self) -> None:
        self.bkshlf1 = pygame.Rect(77, 100, 50, 160)  #Okay, I know the x values for these looks like I randomly chose them, but they are mathmatically equidistant from each other
        self.bkshlf2 = pygame.Rect(209, 100, 50, 160) # Each shelf is 60px wide there are 4 shelves to fit evenly in 600px | 600px - 240px = 360px
                                                        # Since there are 5 hall gaps, we divide 360/5 = 72
        self.bkshlf3 = pygame.Rect(341, 100, 50, 160) # For each x value it after the first (72) it is previous value + 60px + 72px = 204px
        self.bkshlf4 = pygame.Rect(473, 100, 50, 160) # It looks off but its just math ;)
        
        self.bkshlf5 = pygame.Rect(78, 332, 50, 160)  
        self.bkshlf6 = pygame.Rect(209, 332, 50, 160)                                                         
        self.bkshlf7 = pygame.Rect(341, 332, 50, 160) 
        self.bkshlf8 = pygame.Rect(473, 332, 50, 160)

        self.bkshlf9 = pygame.Rect(77, 564, 50, 160)  
        self.bkshlf10 = pygame.Rect(209, 564, 50, 160)                                                         
        self.bkshlf11 = pygame.Rect(341, 564, 50, 160) 
        self.bkshlf12 = pygame.Rect(473, 564, 50, 160)


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
        

