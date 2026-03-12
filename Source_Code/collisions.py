import pygame

from .player import Player
from .bookshelves import Bookshelves

class Collisions: 

    def player_shelf_col(self, player: pygame.Rect, bookshelf: pygame.Rect) -> None:
        if not player.rect.colliderect(bookshelf):
            return

        dx_left = player.rect.right - bookshelf.left
        dx_right = bookshelf.right - player.rect.left
        dy_top = player.rect.bottom - bookshelf.top
        dy_bottom = bookshelf.bottom - player.rect.top

        min_overlap = min(dx_left, dx_right, dy_top, dy_bottom)

        if min_overlap == dx_left:
            player.rect.right = bookshelf.left
            player.velocity.x = 0
        elif min_overlap == dx_right:
            player.rect.left = bookshelf.right
            player.velocity.x = 0
        elif min_overlap == dy_top:
            player.rect.bottom = bookshelf.top
            player.velocity.y = 0
        elif min_overlap == dy_bottom:
            player.rect.top = bookshelf.bottom
            player.velocity.y = 0

        player.pos.update(player.rect.center)

    def update(self, player: Player, bookshelves: Bookshelves) -> None:
        self.player_shelf_col(player, bookshelves.bkshlf1)
        self.player_shelf_col(player, bookshelves.bkshlf2)
        self.player_shelf_col(player, bookshelves.bkshlf3)
        self.player_shelf_col(player, bookshelves.bkshlf4)
        self.player_shelf_col(player, bookshelves.bkshlf5)
        self.player_shelf_col(player, bookshelves.bkshlf6)
        self.player_shelf_col(player, bookshelves.bkshlf7)
        self.player_shelf_col(player, bookshelves.bkshlf8)
        self.player_shelf_col(player, bookshelves.bkshlf9)
        self.player_shelf_col(player, bookshelves.bkshlf10)
        self.player_shelf_col(player, bookshelves.bkshlf11)
        self.player_shelf_col(player, bookshelves.bkshlf12)
