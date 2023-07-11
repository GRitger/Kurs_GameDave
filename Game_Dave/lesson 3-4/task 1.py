import pygame
import math
def draw(screen: pygame.Surface):
    font = pygame.font.Font('C://WINDOWS//Fonts//segoeuil.ttf', 36)
    text = font.render("Lesson 3. Snowman", True, pygame.Color("Red"))
    #text = font.render("Lesson 3. Snowman", True, (0, 255, 0))
    text_x = w // 2 - text.get_width() // 2
    text_y = h // 20 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    rb=140
    pygame.draw.circle(screen, (0, 0, 0), (w //2, h - rb), rb, 5)
    pygame.draw.circle(screen, (0, 0, 0), (w //2, h - rb*2 - rb//2+5), rb//2, 5)
    pygame.draw.line(screen, (0, 0, 0), ( w //2 -  rb //0.75, h//1.85), (w //2-rb, h - rb), 5)
    pygame.draw.line(screen, (0, 0, 0), (w // 2 + rb // 0.75, h // 1.85), (w // 2 + rb, h - rb), 5)
    pygame.draw.circle(screen, (0, 0, 0), (w //2+20, h - rb*2 - rb//2-15), 3 )
    pygame.draw.circle(screen, (0, 0, 0), (w //2-20, h - rb*2 - rb//2-15), 3 )
    pygame.draw.polygon(screen, (255, 102, 0), [(w //2, h - rb*2 - rb//2), (w //2+15, h - rb*2 - rb//2+10), (w //2-15, h - rb*2 - rb//2+10)])
    pygame.draw.arc(screen, (0, 0, 0), (w //2.18, h/2.38, 50, 50), math.pi, 2*math.pi,3)


if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(255, 255, 255)
    hsv = color.hsva
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()