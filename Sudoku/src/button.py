import pygame

class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width, self.height = 200, 50
        self.text = text
        self.font = pygame.font.SysFont('monospace', 25)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, win):

        pygame.draw.rect(win, (255, 255, 255), self.rect)
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x - 2, self.y - 2, self.width + 4, self.height + 4), 2, 2, 2, 2)

        text = self.font.render(format(self.text), True, (0, 0, 0))
        rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text, rect)