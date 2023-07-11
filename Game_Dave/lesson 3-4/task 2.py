import pygame

def draw(screen: pygame.Surface):
    pygame.draw.rect(screen, (0, 255, 0), ( 50, 50, 500, 500))
    pygame.draw.rect(screen, (46, 117, 40), ( 500, 100, 50, 450))
    pygame.draw.rect(screen, (46, 117, 40), ( 100, 500, 450, 50))
    pygame.draw.rect(screen, color, ( 500, 50, 50, 50))
    pygame.draw.rect(screen, color, (50, 500, 50, 50))

if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 20, hsv[3])
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()