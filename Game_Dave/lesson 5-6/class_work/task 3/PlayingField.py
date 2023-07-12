import pygame
class PlayingField:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.field = [[0] * w for _ in range(h)]  # [[0] * w] * h

        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.h):
            for j in range(self.w):
                rect = ((j * self.cell_size + self.left, i * self.cell_size + self.top),
                        (self.cell_size, self.cell_size))
                rect2 = ((j * self.cell_size + self.left + 1, i * self.cell_size + self.top + 1),
                        (self.cell_size - 2, self.cell_size - 2))
                c = [(0, 0, 0), (255, 0, 0), (0, 0, 255)]
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                pygame.draw.rect(screen, c[self.field[i][j]], rect2, 0)

    def get_click(self, pos):
        cell = self.get_cell(pos)
        if cell:
            self.field[cell[1]][cell[0]] += 1
            self.field[cell[1]][cell[0]] %= 3
        else:
            print('ERROR')

    def get_cell(self, pos):
        # size = 1
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None
        return x, y