import pygame

class Textbar:
    def __init__(self, x, y, width, height, show_line, size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (200, 200, 200)
        self.color_bg = (200, 200, 200)
        self.str = ""
        self.size = size
        self.font = pygame.font.SysFont('monospace', self.size)
        self.show_line = show_line
    
    def draw(self, win):

        pygame.draw.rect(win, self.color_bg, pygame.Rect(self.x - 1, self.y - 1, self.width + 2, self.height + 2), 2, 2, 2, 2)
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        text = self.font.render(format(self.str), True, (0, 0, 0))
        rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text, rect)

        if self.show_line:
            pygame.draw.line(win, (0, 0, 0), (rect.x + rect.width, rect.y), (rect.x + rect.width, rect.y + rect.height))