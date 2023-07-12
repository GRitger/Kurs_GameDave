import pygame

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

print("r- нарисовать квадрат")
print("k- нарисовать круг")
print("c- очитстить холст")

# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h, rad = 0, 0, 0, 0, 0
drawing = False  # режим рисования выключен
f = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            f = 1
            color = input("введите цветна выбор: white, green, red, blue: ")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            f = 2
            color = input("введите цветна выбор: white, green, red, blue: ")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            f = 0
        if f == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                # Запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # Сохраняем нарисованное (на втором холсте)
                screen2.blit(screen, (0, 0))
                drawing = False
                x1, y1, w, h = 0, 0, 0, 0
            if drawing and event.type == pygame.MOUSEMOTION:
                # Запоминаем текущие размеры
                #w, h = event.pos[0] - x1, event.pos[1] - y1
                w, h = event.pos[0], event.pos[1]
            # Рисуем на экране сохраненное на втором холсте
            screen.fill(pygame.Color('black'))
            screen.blit(screen2, (0, 0))
            if drawing:  # и, если надо, текущий прямоугольник
                sx = min(x1, w)
                sy = min(y1, h)
                dx = max(x1, w)
                dy = max(y1, h)
                pygame.draw.rect(screen, (pygame.Color(color)), ((sx, sy), (dx-sx, dy-sy)), 5)
            pygame.display.flip()
        elif f == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                # Запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # Сохраняем нарисованное (на втором холсте)
                screen2.blit(screen, (0, 0))
                drawing = False
                x1, y1, w, h, rad = 0, 0, 0, 0, 0
            if drawing and event.type == pygame.MOUSEMOTION:
                # Запоминаем текущие размеры
                #w, h = event.pos[0] - x1, event.pos[1] - y1
                x, y = event.pos[0], event.pos[1]
                rad = (((x1 - x) * (x1 - x)) + ((y1 - y) * (y1 - y))) ** 0.5
                rad = int(rad)
                # Рисуем на экране сохраненное на втором холсте
            screen.fill(pygame.Color('black'))
            screen.blit(screen2, (0, 0))
            if drawing:  # и, если надо, текущий прямоугольник
                pygame.draw.circle(screen, (pygame.Color(color)), (x1, y1), rad, 5)
            pygame.display.flip()
        else:
            screen.fill(pygame.Color('black'))
            screen2.fill(pygame.Color('black'))
            pygame.display.flip()











        #if event.type == pygame.MOUSEBUTTONDOWN:
            #drawing = True  # включаем режим рисования
            # Запоминаем координаты одного угла
           # x1, y1 = event.pos
       #if event.type == pygame.MOUSEBUTTONUP:
            # Сохраняем нарисованное (на втором холсте)
          #  screen2.blit(screen, (0, 0))
          # drawing = False
           # x1, y1, w, h = 0, 0, 0, 0
    #   if event.type == pygame.MOUSEMOTION:
            # Запоминаем текущие размеры
       #     w, h = event.pos[0] - x1, event.pos[1] - y1
    # Рисуем на экране сохраненное на втором холсте
  #  screen.fill(pygame.Color('black'))
  #  screen.blit(screen2, (0, 0))
  #  if drawing:  # и, если надо, текущий прямоугольник
    #    pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
   # pygame.display.flip()
pygame.quit()