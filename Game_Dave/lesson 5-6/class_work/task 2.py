import random
import sys

import pygame


def draw():
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width, random.random() * height, 1, 1))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    x = width // 2
    y = height // 2
    v = 30  # пикс в сек
    fps = 60
    clock = pygame.time.Clock()
    # font = pygame.font.SysFont(None, 40)
    screen.fill(pygame.Color('blue'))
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 10
                if event.key == pygame.K_UP:
                    y -= 10
                if event.key == pygame.K_RIGHT:
                    x += 10
                if event.key == pygame.K_DOWN:
                    y += 10

        screen.fill(pygame.Color('blue'))
        pygame.draw.circle(screen, pygame.Color('orange'), (x % width, y % height), 30)

        clock.tick(fps)

        # обновление экрана
        pygame.display.flip()
    pygame.quit()