import os
import sys
from random import randrange, choice
import pygame

def load_image(name, colorkey=None) -> pygame.Surface:
    pygame.init()
    # fullname = os.path.join('data', name)
    # fullname = os.path.abspath(fullname)
    # # если файл не существует, то выходим
    # print(fullname)
    # if not os.path.isfile(fullname):
    #     print(f"Файл с изображением '{fullname}' не найден")
    #     sys.exit()
    image = pygame.image.load(name)
    if colorkey is not None:
        # image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
    return image

class Mario(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1).subsurface(0, 0, 97, 84), (80, 80))
    image_2 = pygame.transform.scale(load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1).subsurface(100, 0, 82, 84), (80, 80))
    image_3 = pygame.transform.scale(load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1).subsurface(190, 0, 100, 84), (80, 80))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.ag = (-90, 0, 90, 180)
        self.count = 0
        self.image = pygame.transform.rotate(Mario.image, self.ag[self.count % 4])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 310
        self.tuple_img = (Mario.image, Mario.image_2, Mario.image_3)

    def update(self, *args) -> None:

        if self.rect.x == 0 and self.count == 0 and self.rect.y < (h - 80):
            self.rect = self.rect.move(0, 100 / fps)
        elif self.count == 1 and self.rect.x < (w - 80):
            self.rect = self.rect.move(100 / fps, 0)
        elif self.count == 2 and self.rect.y > (0):
                    self.rect = self.rect.move(0, - 100 / fps)
        elif self.count == 3 and self.rect.x > (0):
                        self.rect = self.rect.move(-100 / fps, 0)
        elif self.count == 4:
            self.count=0
        else:
            self.count +=1
            self.image = pygame.transform.rotate(Mario.image, self.ag[self.count % 4])
        #self.image = self.tuple_img[self.count % 3]
        #self.count += 1

if __name__ == '__main__':
    size = w, h = (620, 620)
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((0, 0, 0))
    image = load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1)
    #img_1 = image.subsurface((100, 0, 100, 100))
    #img_2 = pygame.transform.scale(image, (100, 100))

    all_sprite = pygame.sprite.Group()
    Mario(all_sprite)
    clock = pygame.time.Clock()
    fps = 50
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprite.draw(screen)
        all_sprite.update(event)
        clock.tick(fps)
        pygame.display.flip()