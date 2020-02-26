import pygame
from time import sleep


class BaseElement:
    def __init__(self, x, y, szx, szy, color, win, border=3, border_color=None, active_color=None,
                 active_border_color=None):
        self.x, self.y = x, y
        self.szx, self.szy = szx, szy
        self.color = color
        self.win = win
        self.border = border

        if border_color is None:
            self.border_color = color
        else:
            self.border_color = border_color

        self.active = False

        if active_color is None:
            self.active_color = self.color
        else:
            self.active_color = active_color

        if active_border_color is None:
            self.active_border_color = self.border_color
        else:
            self.active_border_color = active_border_color

    def click(self):
        if self.mouse_on():
            if self.active:
                self.active = False
            else:
                self.active = True
        else:
            self.active = False

    def draw(self):
        global color, border_color
        if self.active:
            color, border_color = self.active_color, self.active_border_color
        else:
            color, border_color = self.color, self.border_color

        pygame.draw.rect(self.win, color,
                         [self.x + self.border - 1, self.y + self.border - 1,
                          self.szx - 2 * self.border + 2,
                          self.szy - 2 * self.border + 2])
        pygame.draw.rect(self.win, border_color, [self.x, self.y, self.szx, self.szy],
                         self.border)
        pygame.display.update()

    def mouse_on(self):
        x, y = pygame.mouse.get_pos()
        return x in range(self.x, self.x + self.szx) and y in range(self.y, self.y + self.szy)


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((600, 450))
    box = BaseElement(10, 40, 300, 50, (244, 243, 8), win, border_color=(0, 255, 66),
                      active_color=(0, 0, 0), active_border_color=(255, 0, 0))

    while True:
        box.draw()
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                box.click()
