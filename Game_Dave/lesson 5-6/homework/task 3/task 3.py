import pygame

from KrestaAndNull import KrestaAndNull

if __name__ == '__main__':
    screen = pygame.display.set_mode((600, 600))
    board = KrestaAndNull(5, 7)
    board.setka(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos, screen)
        screen.fill((0, 0, 0))
        pygame.display.flip()