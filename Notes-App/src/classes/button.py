import pygame

class Button:
    def __init__(self, x, y, width, height, color, border_radius, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border_radius = border_radius
        self.text = text
        self.font = pygame.font.Font('Notes-App/font.ttf', self.height//2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):

        if self.border_radius == 0:    
            pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        else:
            pygame.draw.rect(win, self.color, pygame.Rect(self.x - self.border_radius//2, self.y - self.border_radius//2, self.width + self.border_radius, self.height + self.border_radius), self.border_radius, self.border_radius, self.border_radius, self.border_radius)

            pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        text_ = self.font.render(format(self.text), True, (255, 255, 255))
        rect = text_.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text_, rect)