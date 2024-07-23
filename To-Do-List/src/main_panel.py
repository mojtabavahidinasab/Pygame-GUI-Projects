import pygame

from path import get_path

class Panel:
    def __init__(self, x, y, font, string, priority_num, task_ticked):
        self.x = x
        self.y = y
        self.width = 600
        self.height = 50
        self.font = font
        self.size = 35
        self.font_to_use = pygame.font.Font(self.font, self.size)
        self.string = string
        self.color_main = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.delete_btn = pygame.transform.scale(pygame.image.load(get_path("assets", "delete.png")), (40, 40)).convert_alpha()
        self.clicked_btn = pygame.transform.scale(pygame.image.load(get_path("assets", "verified.png")), (20, 20)).convert_alpha()
        self.delete_btn_rect = pygame.Rect((self.x + self.width - 45), (self.y + 5), 40, 40)
        self.priority_btn_rect = pygame.Rect((self.x + self.width + 25/2), (self.y + 25//2), 25, 25)
        self.priority_list = [(0, 0, 200), (0, 200, 0), (200, 0, 0)]
        self.priority_num = priority_num
        self.ticked_btn_rect = pygame.Rect((self.x - 25 - 25/2), (self.y + 25//2), 25, 25)
        self.task_ticked = task_ticked

    def draw(self, win):
        
        pygame.draw.rect(win, self.color_main, pygame.Rect(self.x, self.y, self.width, self.height), 4, 4, 4, 4)
        pygame.draw.rect(win, self.color_main, pygame.Rect(self.x + 2, self.y + 2, self.width - 4, self.height - 4))

        win.blit(self.delete_btn, ((self.x + self.width - 45), (self.y + 5)))

        pygame.draw.rect(win, self.priority_list[self.priority_num], pygame.Rect((self.x + self.width + 25/2), (self.y + 25//2), 25, 25))
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect((self.x + self.width + 25/2 - 1), (self.y + 25//2 - 1), 27, 27), 2, 2, 2, 2)

        pygame.draw.rect(win, (200, 200, 200), pygame.Rect((self.x - 25 - 25/2), (self.y + 25//2), 25, 25))
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect((self.x - 25 - 25//2 - 1), (self.y + 25//2 - 1), 27, 27), 2, 2, 2, 2)

        self.font_to_use.set_strikethrough(self.task_ticked)

        text = self.font_to_use.render(format(self.string), True, (0, 0, 0))
        rect = text.get_rect(center = (self.x + self.width//2, self.y + self.height//2))

        win.blit(text, rect)

        if self.task_ticked:
            win.blit(self.clicked_btn, (self.ticked_btn_rect.x + 5//2, self.ticked_btn_rect.y + 5//2))

    def update_priority_num(self):

        if self.priority_num < len(self.priority_list) - 1:
            self.priority_num += 1

        elif self.priority_num >= len(self.priority_list) - 1:
            self.priority_num = 0