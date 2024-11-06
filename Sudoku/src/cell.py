import pygame


class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.width = self.height = 50
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont('monospace', self.width//2)
        self.is_final = False

    def draw(self, win):

        pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 2, 2, 2)

        if self.val is not None:

            text = self.font.render(format(self.val), True, (0, 0, 0))
            rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

            win.blit(text, rect)