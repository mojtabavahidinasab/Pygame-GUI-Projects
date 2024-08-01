import pygame

class Card:
    def __init__(self, x, y, width, height, string):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.string = string
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont('monospace', 20)
        self.color_main = (200, 200, 200)
        self.color_hover = (100, 100, 100)

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 1, self.y - 1, self.width + 2, self.height + 2), 2, 2, 2, 2)
        pygame.draw.rect(win, self.color_main, pygame.Rect(self.x, self.y, self.width, self.height))

        text = self.font.render(format(self.string), True, (0, 0, 0))
        rect = text.get_rect(center = (self. x + self.width//2, self.y + self.height//2))

        win.blit(text, rect)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.color_main = self.color_hover
        else:
            self.color_main = (200, 200, 200)
