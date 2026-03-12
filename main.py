import pygame

from Source_Code.game import Game


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Library Lunatic")
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()

    clock = pygame.time.Clock()
    game = Game()

    while game.running:
        dt = clock.tick(60) / 1000.0
        dt = min(dt, 0.05)

        for event in pygame.event.get():
            game.handle_event(event)

        game.update(dt)
        game.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()