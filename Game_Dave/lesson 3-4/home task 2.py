import pygame
import sys
def draw(screen: pygame.Surface, x1, y1, R1, G1, B1):
    pygame.draw.rect(screen, (R1, G1, B1), (x1, y1, 40, 40))

if __name__ == '__main__':
    kvadrat = input()
    for i in kvadrat:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()
    kvadrat = int(kvadrat)
    if (kvadrat < 0):
        print("Неправильный формат ввода")
        sys.exit()
    x=0
    y=0
    pygame.init()
    kv = kvadrat // 4
    if (kvadrat % 4 != 0 ):
        kv = kv +1
    size = 200, 50 * kv

    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)
    for i in range(1, kvadrat + 1):
        R,G,B = input().split()
        for j in R:
            if( j == '.'):
                print("Неправильный формат ввода")
                sys.exit()
        for j in R:
            if( j == '.'):
                print("Неправильный формат ввода")
                sys.exit()
        for j in B:
            if (j == '.'):
                print("Неправильный формат ввода")
                sys.exit()
        R = int(R)
        if (R > 255 or R < 0):
            print("Неправильный формат ввода")
            sys.exit()
        G = int(G)
        if (G > 255 or G < 0):
            print("Неправильный формат ввода")
            sys.exit()
        B = int(B)
        if (B > 255 or B < 0):
            print("Неправильный формат ввода")
            sys.exit()

        draw(screen, x, y, R, G, B)
        x = x +50
        if (i % 4 == 0):
            y = y + 50
            x = 0

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()