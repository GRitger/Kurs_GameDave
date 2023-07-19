import math
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
    image = pygame.transform.scale(
        load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1).subsurface(0, 0, 97,
                                                                                                            84),
        (80, 80))
    image_2 = pygame.transform.scale(
        load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1).subsurface(100, 0, 82,
                                                                                                            84),
        (80, 80))
    image_3 = pygame.transform.scale(
        load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1).subsurface(190, 0, 100,
                                                                                                            84),
        (80, 80))

    def __init__(self, *groups):
        super().__init__(*groups)
        self.posx = 310
        self.posy = 310
        self.ygol1 = 0
        self.ygol = 0
        self.raz = 0
        self.gepotinyz = 0.0
        #self.ag = (-90, 0, 90, 180)
        self.count = 0
        #self.image = pygame.transform.rotate(Mario.image, self.ag[self.count % 4])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.tuple_img = (Mario.image, Mario.image_2, Mario.image_3)

    def update(self, *args) -> None:
        self.posx = posx
        self.posy = posy
        self.gepotinyz = (((self.rect.x - self.posx) * (self.rect.x - self.posx)) + (self.rect.y - self.posy) * (self.rect.y - self.posy)) ** 0.5

        if posx- self.rect.x != 0:
            self.ygol = -(((math.atan( (posy - self.rect.y)  / (posx- self.rect.x))) * 180) / math.pi)
        if posx- self.rect.x < 0:
            self.ygol = 180 + self.ygol
        self.image = pygame.transform.rotate(Mario.image, self.ygol)
        self.ygol1 = self.ygol

        if self.gepotinyz <= 200 / fps:
            self.rect = self.rect.move(self.rect.x - self.posx , self.rect.y - self.posy)
            pass
        else:
            self.raz = self.gepotinyz // (200 / fps)
            self.rect = self.rect.move((self.posx - self.rect.x ) // self.raz, ( self.posy - self.rect.y) // self.raz)

        # self.image = self.tuple_img[self.count % 3]
        # self.count += 1


if __name__ == '__main__':
    size = w, h = (620, 620)
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((0, 0, 0))
    image = load_image('C:/Users/WARS/PycharmProjects/Kurs_GameDave/Game_Dave/data/mario_2.png', -1)
    # img_1 = image.subsurface((100, 0, 100, 100))
    # img_2 = pygame.transform.scale(image, (100, 100))

    all_sprite = pygame.sprite.Group()
    Mario(all_sprite)
    clock = pygame.time.Clock()
    fps = 40
    #!all_sprite.pos = 0, 0
    posx = 0
    posy = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                posx = event.pos[0] -80
                posy = event.pos[1]
        screen.fill((0, 0, 0))
        all_sprite.draw(screen)
        #pos = 100, 100
        all_sprite.update(posx, posy)
        clock.tick(fps)
        pygame.display.flip()