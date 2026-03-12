import pygame
from .palette import COLORS
 
 
class HUD:
    def __init__(self, screen, screen_w):
        # Sets up the font and saves screen width for text
        self.screen = screen
        self.screen_w = screen_w
        self.font = pygame.font.SysFont(None, 22)
        self.rect = pygame.Rect(0, 0, screen_w, 56)
 
    def _draw_text(self, text, pos, color):
        s = self.font.render(text, True, color)
        self.screen.blit(s, pos)
 
    def draw(self, timer, score, carrying):
        # Draw the HUD panel at the top
        pygame.draw.rect(self.screen, COLORS.panel, pygame.Rect(0, 0, self.screen_w, 56))
 
        # Timer turns red when low
        if timer > 10:
            timer_color = COLORS.hud_timer_ok
        else:
            timer_color = COLORS.hud_timer_low
 
        # Score top left
        self._draw_text(f"Score: {score}", (12, 10), COLORS.text)
 
        # Timer top center
        s = self.font.render(f"Time: {int(timer)}", True, timer_color)
        self.screen.blit(s, (self.screen_w // 2 - s.get_width() // 2, 10))
 
        # Carrying top right
        self._draw_text(f"Carrying: {carrying}/3", (self.screen_w - 120, 10), COLORS.text)
 