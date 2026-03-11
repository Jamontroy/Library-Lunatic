from dataclasses import dataclass


@dataclass
class Palette:
    bg: tuple[int, int, int] = (22, 24, 28)
    player: tuple[int, int, int] = (136, 192, 208)


COLORS = Palette()