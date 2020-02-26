import pygame


class TextField:
    def __init__(self, x, y, szx, szy, color, win, border=3, border_color=None, placeholder='write text here',
                 text_color=(0, 0, 0)):
        super().__init__(x, y, szx, szy, color, win, border=border, border_color=border_color)
        self.placeholder = placeholder
        self.text_color = text_color
        self.s = ''

    def add_text(self, text):
        self.s += text

    def delete_text(self, n):
        self.s = self.s[:-n + 1:]

    def draw(self):
        super().draw()
        font = pygame.font.Font(None, 32)
        txt_surface = font.render(self.text, True, self.color)
