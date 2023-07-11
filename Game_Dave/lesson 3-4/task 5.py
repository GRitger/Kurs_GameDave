import pygame
import sys
def draw(screen: pygame.Surface):
    pygame.draw.rect(screen,(255,0,0), (150 - w//2, 150 - w // 2 , w ,w))
    pygame.draw.polygon(screen, (255, 5, 140), [[150 - w//2, 150 - w // 2], [ 150 , (150 - w // 2)-((w*w- (w//2)*(w//2))**0.5)], [150 +w , (150 - w // 2)-((w*w- (w//2)*(w//2))**0.5)], [150 + w//2, 150 - w // 2 ]])
    pygame.draw.polygon(screen, (255, 150,20), [[150 + w//2, 150 - w // 2 ], [150 +w , (150 - w // 2)-((w*w- (w//2)*(w//2))**0.5)], [150 +w , (150 - w // 2)-((w*w- (w//2)*(w//2))**0.5) +w], [150 + w//2, 150 + w // 2 ]])


if __name__ == '__main__':
    w1, hue1 = input().split()
    for i in w1:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()

    for i in hue1:
        if( i == '.'):
            print("Неправильный формат ввода")
            sys.exit()

    w = int(w1)
    hue = int(hue1)
    if ((w % 4 != 0) or (w > 100) or (hue >= 360)):
        print("Неправильный формат ввода")
        sys.exit()

    color = pygame.Color(255, 0, 0)
    #hsv = color.hsva
    #color.hsva = (hsv[0] + hue, hsv[1] + 100, hsv[2]+100, hsv[3])
    #pygame.init()

    size = 300, 300
    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()