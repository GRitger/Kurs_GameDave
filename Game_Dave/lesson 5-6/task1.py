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
    x = 0
    v = 30  # пикс в сек
    fps = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    screen.fill(pygame.Color('blue'))
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                text = font.render(event.unicode, False,
                                   (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
                screen.blit(text, (random.randrange(10, width - 10), random.randrange(10, height - 10)))

        clock.tick(fps)

        # обновление экрана
        pygame.display.flip()
    pygame.quit()