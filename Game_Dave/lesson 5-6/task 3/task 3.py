import pygame

from PlayingField import PlayingField

if __name__ == '__main__':
    screen = pygame.display.set_mode((600, 600))
    board = PlayingField(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()