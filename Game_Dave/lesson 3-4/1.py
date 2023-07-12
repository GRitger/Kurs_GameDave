import random
import math

import pygame
def draw(screen: pygame.Surface):
    #font = pygame.font.Font('C://WINDOWS//Fonts//segoeuil.ttf', 36)
    #text = font.render('Hello!', True, (12, 34, 56))
    #text_x = w // 2 - text.get_width() // 2
    #text_y = h // 2 - text.get_height() // 2
    #screen.blit(text, (text_x, text_y))
    #rect = pygame.Rect( w //2, h//2,70,30)
    #screen.fill((34, 56, 67), (w //2, h//2, 70, 30))
    #for _ in range(10):
        #screen.fill((255, 56, 89), (random.random()* w, random.random() * h, 3, 3))
    #pygame.draw.rect(screen, (255, 53, 89),(0, 0, 80, 90))
    pygame.draw.circle(screen, (222, 33, 56), (w //2, h//2), 100, 50)
    #pygame.draw.ellipse(screen, (222, 33, 56), (45, 67, 100, 50))
    #pygame.draw.ellipse(screen, (222, 33, 56), (45, 67, 100, 50))
    #pygame.draw.arc(screen, (255, 255, 255), (350, 360, 90, 90), 0, math.pi, 6)

if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(25, 60, 10)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 20, hsv[3])
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
       pass
    pygame.quit()