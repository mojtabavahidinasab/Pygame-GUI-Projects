import pygame

class Label:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.text = ""
        self.color_success = (0, 240, 0)
        self.color_warning = (240, 0, 0)
        self.font = pygame.font.SysFont('monospace', 50)
        self.success = False

    def draw(self, win):

        if self.success:
            color = self.color_success
        else:
            color = self.color_warning

        text = self.font.render(format(self.text), True, color)
        rect = text.get_rect(center = (self.x, self.y))
        win.blit(text, rect)
    