from dataclasses import dataclass, field
import pygame



@dataclass 
class Palette:
    bg: tuple[int, int, int] = (22, 24, 28)
    panel: pygame.Color = field(default_factory=lambda: pygame.Color("#2a303c"))
    # Sprites
    player: tuple[int, int, int] = (136, 192, 208)
    wall: pygame.Color = field(default_factory=lambda: pygame.Color("#4c566a"))
    hazard: pygame.Color = field(default_factory=lambda: pygame.Color("#bc424e"))

    # Text
    text: pygame.Color = field(default_factory=lambda: pygame.Color("#d8dee9"))
    subtle: pygame.Color = field(default_factory=lambda: pygame.Color("#a3adbf"))

    # Books theres one color per shelf/book type
    shelf_red: pygame.Color = field(default_factory=lambda: pygame.Color("#ee4343"))
    shelf_green: pygame.Color = field(default_factory=lambda: pygame.Color("#1E7A1E"))
    shelf_blue: pygame.Color = field(default_factory=lambda: pygame.Color("#4169E1"))
    shelf_yellow: pygame.Color = field(default_factory=lambda: pygame.Color("#FFF275"))
    shelf_purple: pygame.Color = field(default_factory=lambda: pygame.Color("#C77DFF"))
    shelf_orange: pygame.Color = field(default_factory=lambda: pygame.Color("#FF8C42"))

    shelf_brown: pygame.Color = field(default_factory=lambda: pygame.Color("#C4A484"))

    # Shelves matched to book color
    book_red: pygame.Color = field(default_factory=lambda: pygame.Color("#ee4343"))
    book_green: pygame.Color = field(default_factory=lambda: pygame.Color("#1E7A1E"))
    book_blue: pygame.Color = field(default_factory=lambda: pygame.Color("#4169E1"))
    book_yellow: pygame.Color = field(default_factory=lambda: pygame.Color("#FFF275"))
    book_purple: pygame.Color = field(default_factory=lambda: pygame.Color("#C77DFF"))
    book_orange: pygame.Color = field(default_factory=lambda: pygame.Color("#FF8C42"))

    # HUD accents idea for future maybe red timer when low, green when ok
    hud_timer_ok:  pygame.Color = field(default_factory=lambda: pygame.Color("#a3be8c"))
    hud_timer_low: pygame.Color = field(default_factory=lambda: pygame.Color("#bf616a"))
 
 

COLORS = Palette()

# Book color registry used to map a string tag book color, shelf color
BOOK_TYPES = {
    "red":   (COLORS.book_red, COLORS.shelf_red),
    "green": (COLORS.book_green, COLORS.shelf_green),
    "blue": (COLORS.book_blue, COLORS.shelf_blue), 
    "yellow": (COLORS.book_yellow, COLORS.shelf_yellow),
    "purple": (COLORS.book_purple, COLORS.shelf_purple),
    "orange": (COLORS.book_orange, COLORS.shelf_orange), 
}