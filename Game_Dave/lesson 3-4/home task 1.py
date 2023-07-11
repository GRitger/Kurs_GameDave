import pygame
import sys
def draw(screen: pygame.Surface):
    cvt = 0
    radis= picsl
    for i in range(col):
        if (cvt == 0):
            pygame.draw.circle(screen, (255, 0, 0), (pc // 2, pc // 2), radis, picsl)
            cvt = cvt + 1
            radis = radis + picsl
        elif (cvt == 1):
            pygame.draw.circle(screen, (0, 255, 0), (pc // 2, pc // 2), radis, picsl)
            cvt = cvt + 1
            radis = radis + picsl
        else:
                pygame.draw.circle(screen, (0, 0, 255), (pc // 2, pc // 2), radis, picsl)
                cvt = 0
                radis = radis + picsl

if __name__ == '__main__':
    picsl1, col1 = input().split()
    for i in picsl1:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()

    for i in col1:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()

    picsl = int(picsl1)
    col = int(col1)
    if ( picsl < 0 or col < 0):
        print("Неправильный формат ввода")
        sys.exit()
    pygame.init()
    pc = 2 * (picsl *col)
    size = pc, pc
    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()