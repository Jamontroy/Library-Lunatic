import pygame
from .palette import COLORS
 
 
class HUD:
    def __init__(self, screen, screen_w):
        # Sets up the font and saves screen width for text
        self.screen = screen
        self.screen_w = screen_w
        self.font = pygame.font.SysFont(None, 22)
        self.rect = pygame.Rect(0, 0, screen_w, 56)
        self.threebooks = []
        self.threeboxes = pygame.sprite.Group();
 
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

        # Timer bar under the timer text
        bar_width = 120
        bar_height = 8
        bar_x = self.screen_w // 2 - bar_width // 2
        bar_y = 32
        fill = int((timer / 60.0) * bar_width)

        if timer > 30:
            bar_color = pygame.Color("#a3be8c")  # green
        elif timer > 10:
            bar_color = pygame.Color("#ebcb8b")  # yellow
        else:
            bar_color = pygame.Color("#bf616a")  # red

        pygame.draw.rect(self.screen, pygame.Color("#4c566a"), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(self.screen, bar_color, (bar_x, bar_y, fill, bar_height))
 
        # Carrying top right
        self._draw_text(f"Carrying: {carrying}/3", (self.screen_w - 210, 10), COLORS.text)

        # Draw small colored squares for carried books
        box_size = 20
        box_y = 28
        box_start_x = self.screen_w - 210
        for i in range(len(self.threebooks)):
            book = self.threebooks[i]
            box_rect = pygame.Rect(box_start_x + i * (box_size + 6), box_y, box_size, box_size)
            pygame.draw.rect(self.screen, book.color, box_rect)
            pygame.draw.rect(self.screen, pygame.Color("#000000"), box_rect, 2)