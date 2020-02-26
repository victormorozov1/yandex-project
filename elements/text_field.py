import pygame
from elements.base_element import BaseElement
from time import sleep


class TextField(BaseElement):
    def __init__(self, x, y, szx, szy, color, win, border=3, border_color=(188, 188, 188),
                 placeholder='write text here',
                 text_color=(0, 0, 0), active_color=None,
                 active_border_color=(155, 155, 155)):
        super().__init__(x, y, szx, szy, color, win, border=border, border_color=border_color,
                         active_color=active_color, active_border_color=active_border_color)
        self.placeholder = placeholder
        self.text_color = text_color
        self.text = ''
        self.written_words = []

    def add_text(self, text):
        self.text += text

    def delete_text(self):
        self.text = self.text[:-1:]

    def draw(self):
        global text
        super().draw()
        font = pygame.font.Font(None, self.szy - self.border * 2)
        text = self.text
        if text == '':
            text = self.placeholder
        text_surface = font.render(text, True, self.text_color)
        self.win.blit(text_surface, (self.x + self.border, self.y + self.border))

        pygame.display.update()

    def key_down(self, key):
        if self.active:
            if key == 8:
                self.delete_text()
            elif key == 13:
                self.written_words.append(self.text)
                self.text = ''
                self.active = False
            else:
                self.add_text(chr(key))


if __name__ == '__main__':
    FPS = 20

    pygame.init()
    win = pygame.display.set_mode((600, 450))
    text_field = TextField(10, 10, 400, 50, (255, 255, 255), win, text_color=(50, 50, 50))

    clock = pygame.time.Clock()

    while True:
        text_field.draw()
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                text_field.click()
            if i.type == pygame.KEYDOWN:
                text_field.key_down(i.key)
        clock.tick(FPS)
