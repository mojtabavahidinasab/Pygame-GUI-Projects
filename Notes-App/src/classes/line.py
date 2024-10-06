import pygame, random

class Line:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font('Notes-App/font.ttf', 20)
        self.color = (0, 0, 0)
        self.rect = None

    def render(self, win):

        self.text_to_display = self.font.render(format(self.text), True, self.color)

        self.rect = self.text_to_display.get_rect(topleft = (self.x, self.y))
    
        win.blit(self.text_to_display, self.rect)