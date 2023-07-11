import pygame
import random

def draw(screen: pygame.Surface):

    for i in range(5500):
        pygame.draw.rect(screen,(random.randint(0,255), random.randint(0,255),random.randint(0,255)), (random.randint(0,600), random.randint(0,600), 1, 1))

if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()