import pygame
from time import sleep


class BaseElement:
    def __init__(self, x, y, szx, szy, color, win, border=3, border_color=None):
        self.x, self.y = x, y
        self.szx, self.szy = szx, szy
        self.color = color
        self.win = win
        self.border = border
        if border_color is None:
            self.border_color = color
        else:
            self.border_color = border_color

    def draw(self):
        pygame.draw.rect(self.win, self.color,
                         [self.x + self.border - 1, self.y + self.border - 1, self.szx - 2 * self.border + 2,
                          self.szy - 2 * self.border + 2])
        pygame.draw.rect(self.win, self.border_color, [self.x, self.y, self.szx, self.szy], self.border)
        pygame.display.update()

    def active(self):
        x, y = pygame.mouse.get_pos()
        return x in range(self.x, self.x + self.szx) and y in range(self.y, self.y + self.szy)


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((600, 450))
    box = BaseElement(10, 40, 300, 50, (244, 243, 8), win, border_color=(0, 255, 66))
    box.draw()
    while True:
        for i in pygame.event.get():
            pass
        print(box.active())

