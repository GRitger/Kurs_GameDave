from random import choice

import pygame
import os, sys

SIZE_SP = 50
FPS = 10
LEVEL = 1


def load_image(name, colorkey=None) -> pygame.Surface:
    pygame.init()
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        # image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
    return image


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None
        self.pos = None
        self.sheet = None
        self.frames = []

    def get_event(self, event):
        pass

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))


class Pacman(Sprite):
    columns = 3
    rows = 1
    img = pygame.transform.scale(load_image("pacman_hero.png", -1), ((SIZE_SP - 5) * 3, SIZE_SP - 5))

    def __init__(self, x, y):
        super().__init__(hero_group)
        self.sheet = Pacman.img
        self.frames = []
        self.cut_sheet(self.sheet, Pacman.columns, Pacman.rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.pos = [x // SIZE_SP, y // SIZE_SP]

    def update(self, *args) -> None:
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def move(self, x, y):
        self.rect= self.rect.move(x, y)

    def rotate(self, movement):
        pass


def load_level(filename):
    filename = 'data/' + filename
    with open(filename, 'r') as mapfile:
        level_map = [line.strip() for line in mapfile]
    maxW = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(maxW, '.')), level_map))


def generate_level(level):
    pacman, x, y, count = None, None, None, 0
    for y in range(len((level))):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Dot(x * SIZE_SP, y * SIZE_SP)
                count += 1
            elif level[y][x] == '#':
                Tile(x * SIZE_SP, y * SIZE_SP)
            elif level[y][x] == '@':
                pacman = Pacman(x * SIZE_SP, y * SIZE_SP)
                Dot(x * SIZE_SP, y * SIZE_SP)
                level[y][x] = "."
                count += 1
            elif level[y][x] == '&':
                ghost =  Ghost(x * SIZE_SP, y * SIZE_SP)
                Dot(x * SIZE_SP, y * SIZE_SP)
                level[y][x] = "."
                count += 1
    return pacman, x, y, count, ghost


class Dot(Sprite):
    dot = pygame.transform.scale(load_image("dot.png", -1), (SIZE_SP, SIZE_SP))
    apple = pygame.transform.scale(load_image("apple.png", -1), (SIZE_SP // 2, SIZE_SP // 2))
    strawberry = pygame.transform.scale(load_image("strawberry.png", -1), (SIZE_SP // 2, SIZE_SP // 2))

    elem = (dot, apple, strawberry)

    def __init__(self, x, y):
        super().__init__(dot_group)
        self.image = choice(Dot.elem)
        self.rect = self.image.get_rect(center=(SIZE_SP // 2, SIZE_SP // 2))
        self.rect = self.rect.move(x, y)

    def update(self) -> None:
        global SCORE
        if pygame.sprite.spritecollideany(self, hero_group):
            SCORE += 1
            self.kill()


class Ghost(Sprite):
    columns = 6
    rows = 1

    pink = pygame.transform.scale(load_image("ghost_pink.png", -1), ((SIZE_SP - 8) * 6, (SIZE_SP - 8)))
    red = pygame.transform.scale(load_image("ghost_red.png", -1), ((SIZE_SP - 8) * 6, (SIZE_SP - 8)))
    blue = pygame.transform.scale(load_image("ghost_blue.png", -1), ((SIZE_SP - 8) * 6, (SIZE_SP - 8)))
    orange = pygame.transform.scale(load_image("ghost_orange.png", -1), ((SIZE_SP - 8) * 6, (SIZE_SP - 8)))
    ghost_color = (pink, red, blue, orange)

    def __init__(self, x, y):
        super().__init__(ghost_group)
        sheet = choice(Ghost.ghost_color)
        self.frames = []
        self.cut_sheet(sheet, Ghost.columns, Ghost.rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.pos = [x // SIZE_SP, y // SIZE_SP]
        


    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
    
    def move(self, x, y):
        self.rect= self.rect.move(x, y)


class Tile(Sprite):
    tile = pygame.transform.scale(load_image("tile.png"), (SIZE_SP - 5, SIZE_SP - 5))

    def __init__(self, x, y):
        super().__init__(block_group)
        self.image = Tile.tile
        self.rect = self.image.get_rect().move(x, y)


def start_screen():
    intro_text = [
        "Pac-man", " ",
        "Режим: 1. Бесконечный\t2. Стандартный",
        "3. Рейтинг",
        "4. Настройки"
    ]

    for line in intro_text:
        print(line)

    while True:
        text = input()
        if text == '1':
            return 1
        if text == '2':
            return 2
        if text == '3':
            return 3
        if text == '4':
            return 4
        print('введите корректные данные')


def terminate():
    pygame.quit()
    sys.exit


def start_game_inf():
    pass

def conflict(ghost, hero):
    x, y =  hero.pos
    x = x * 50 + 20
    y = y * 50 + 20
    conf = ghost.rect.collidepoint(x, y)
    return conf

def mov( ghost, level_map, bydnapravlenie, napravlen, napravlenie ):
    x, y = ghost.pos
    if level_map[y][ x-1 ] == '.':
        napravlenie.append("Left")
    if level_map[y][ x+1 ] == '.': 
        napravlenie.append("Right")
    if level_map[y-1][x] == '.':
        napravlenie.append("Up")
    if level_map[y+1][x] == '.':
        napravlenie.append("Down")
    if len(napravlenie) > 1:
        bydnapravlenie= choice(napravlenie)
        while bydnapravlenie == napravlen:
            bydnapravlenie= choice(napravlenie)
    else:
        bydnapravlenie = napravlen    
    if bydnapravlenie == "Left":
        napravlen = "Right"
    elif bydnapravlenie == "Right":
        napravlen = "Left"
    elif bydnapravlenie == "Up":
        napravlen = "Down"
    elif bydnapravlenie == "Down":
        napravlen = "Up"

    if bydnapravlenie == "Left":
        ghost.move(-50, 0)
        ghost.pos[0] -=1
    elif bydnapravlenie == "Right":
        ghost.move(50, 0)
        ghost.pos[0] +=1
    elif bydnapravlenie == "Up":
        ghost.move(0, -50)
        ghost.pos[1] -=1
    elif bydnapravlenie == "Down":
        ghost.move(0, 50)
        ghost.pos[1] +=1
    napravlenie.clear()
    return napravlen

def move(hero, movement, level_map):
    x, y = hero.pos
    if movement == "Left" and level_map[y][x-1] == '.':
        hero.pos[0] -=1
        hero.move(-50, 0)    
        #print("left")
    elif movement == "Down"and level_map[y+1][x] == '.':
        hero.pos[1] +=1
        hero.move(0, 50) 
        #print("Down")
        #Pacman(hero_group, x * SIZE_SP, y * SIZE_SP)
    elif movement == "Right"and level_map[y][x+1] == '.':
        hero.pos[0] +=1
        hero.move(50, 0)
        #print("Right")
    elif movement == "Up"and level_map[y-1][x] == '.':
        hero.pos[1] -=1
        hero.move(0, -50)
        #print("Up")

def start_game():
    level_map = load_level("level_1.map")
    hero, max_x, max_y, count, ghost = generate_level(level_map)

    screen = pygame.display.set_mode(((max_x + 1) * SIZE_SP, (max_y + 1) * SIZE_SP))

    #Pnmacman(hero_group, x // SIZE_SP, y // SIZE_SP)
    game = True
    pause = False
    clock = pygame.time.Clock()
    bydnapravlenie = ""
    napravlen = ""
    napravlenie = []
    # SCORE = 0

    while game:
        text = my_font.render(f'SCORE: {SCORE}', False, pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:                
                movement = "Left"
                move(hero, movement, level_map)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                movement = "Down"
                move(hero, movement, level_map)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                movement = "Right"
                move(hero, movement, level_map)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                movement = "Up"
                move(hero, movement, level_map)

        screen.fill(0)
        dot_group.draw(screen)
        dot_group.update()
        napravlen = mov(ghost, level_map, bydnapravlenie, napravlen, napravlenie)
        ghost_group.draw(screen)
        ghost_group.update()
        conf = conflict(ghost, hero)
        hero_group.draw(screen)
        hero_group.update()
        block_group.draw(screen )
        screen.blit(text, (max_x * SIZE_SP - text.get_width() + 10, 10))
        pygame.display.flip()
        if conf:
            print("Game over")
        clock.tick(FPS)


def rating_screen():
    pass


def setting_screen():
    pass


if __name__ == '__main__':
    pygame.init()
    SCORE = 0

    my_font = pygame.font.SysFont(None, 30)

    mode = start_screen()
    print(f"mode = {mode}")

    ghost_group = pygame.sprite.Group()
    hero_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    dot_group = pygame.sprite.Group()

    gost = Ghost
    pacm = Pacman

    if mode == 1:
        start_game_inf()
    elif mode == 2:
        start_game()
    elif mode == 3:
        rating_screen()
    elif mode == 4:
        setting_screen()