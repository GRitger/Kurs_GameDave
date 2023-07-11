import pygame
import sys
def draw(screen: pygame.Surface):
    w = 0
    h = 0
    for i in range(1,clet * clet+1):
        for j in range(1, clet+1):
            if ((i+j) % 2 != 0):
                pygame.draw.rect(screen, (255, 255, 255), (w, h, kl, kl))
            w = w + kl
        h = h + kl
        w=0

if __name__ == '__main__':
    picsl1, clet1 = input().split()
    for i in picsl1:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()

    for i in clet1:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()

    picsl = int(picsl1)
    clet = int(clet1)
    if (picsl % clet != 0):
        print("Неправильный формат ввода")
        sys.exit()

    pygame.init()
    kl= picsl // clet

    size = picsl, picsl
    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()