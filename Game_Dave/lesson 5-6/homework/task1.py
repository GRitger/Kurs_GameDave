import pygame
import random

def drow(screen, nowpisitioncirclX,nowpisitioncirclY ):
    for i in range(len(nowpisitioncirclX)):
        pygame.draw.circle(screen, (255,255,255), (nowpisitioncirclX[i], nowpisitioncirclY[i]), 25 )

if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    nowpisitioncirclX = []
    nowpisitioncirclY = []
    napravlencirclX = []
    napravlencirclY = []
    time = []
    running = True
    fps = 30
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)
    screen.fill(pygame.Color('black'))
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                nowpisitioncirclX.append(width  // 2)
                nowpisitioncirclY.append(height // 2)
                napravlencirclX.append(random.randint(-1, 1))
                napravlencirclY.append(random.randint(-1, 1))
                v = random.randrange(1, 40)  # пикс в сек
                time.append(v)

        if len(nowpisitioncirclX) != 0:
            screen.fill(pygame.Color('black'))
            drow(screen, nowpisitioncirclX,nowpisitioncirclY )
            t = clock.tick
            for i in range(len(nowpisitioncirclX)):
                while napravlencirclX[i] == 0 and napravlencirclY[i] == 0:
                    napravlencirclX.append(random.randint(-1, 1))
                    napravlencirclY.append(random.randint(-1, 1))
                nowpisitioncirclX[i] = (nowpisitioncirclX[i] + napravlencirclX[i] * time[i]) % width
                nowpisitioncirclY[i] = (nowpisitioncirclY[i] + napravlencirclY[i] * time[i]) % height

        clock.tick(fps)
        # обновление экрана
        pygame.display.flip()
    pygame.quit()