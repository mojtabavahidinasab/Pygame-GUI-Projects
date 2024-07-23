import pygame

from path import get_path

class TextBar:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.width = 600
        self.height = 50
        self.font = font
        self.size = 35
        self.font_to_use = pygame.font.Font(self.font, self.size)
        self.string = ""
        self.color_main = (255, 255, 255)
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.add_btn = pygame.transform.scale(pygame.image.load(get_path("assets", "add.png")), (40, 40)).convert_alpha()
        self.add_btn_rect = pygame.Rect((self.x + self.width - 45), (self.y + 5), 40, 40)
        self.writing = False

    def draw(self, win):

        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 4, 4, 4, 4)
        pygame.draw.rect(win, self.color_main, pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4))

        win.blit(self.add_btn, ((self.x + self.width - 45), (self.y + 5)))

        text = self.font_to_use.render(format(self.string), True, (0, 0, 0))
        rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text, rect)

