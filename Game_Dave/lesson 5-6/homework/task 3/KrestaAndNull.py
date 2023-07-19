import pygame
class KrestaAndNull:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.field = [[0] * w for _ in range(h)]  # [[0] * w] * h
        self.player = 3

        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def setka (self, screen):
        for i in range(self.h):
            for j in range(self.w):
                rect = ((j * self.cell_size + self.left, i * self.cell_size + self.top),
                        (self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                pygame.display.flip()
    def render(self, screen, pos):
        i = pos[0]
        j = pos[1]
        if self.player == 0:
            pygame.draw.line(screen, (255, 255, 255), (j * self.cell_size + self.left + self.cell_size //2,
            i  * self.cell_size + self.top + self.cell_size //4),
            (j * self.cell_size + self.left + self.cell_size // 2, i * self.cell_size + self.top + ((self.cell_size //4)*3)))

            pygame.draw.line(screen, (255, 255, 255), (j * self.cell_size + self.top + self.cell_size // 4,
            i * self.cell_size + self.left + self.cell_size // 2),
            (j * self.cell_size + self.top + ((self.cell_size // 4)*3), i * self.cell_size + self.left + self.cell_size // 2))
            self.player = 1

        elif self.player == 1:
            pygame.draw.circle( screen, (255, 255, 255), (j * self.cell_size + self.top + self.cell_size //2,
            i * self.cell_size + self.left + self.cell_size //2 ), self.cell_size // 3, 3)
            self.player = 0



    def get_click(self, pos, screen):
        cell = self.get_cell(pos)
        if cell:
            self.render(screen, pos)
        else:
            print('ERROR')

    def get_cell(self, pos):
        # size = 1
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None
        return x, y