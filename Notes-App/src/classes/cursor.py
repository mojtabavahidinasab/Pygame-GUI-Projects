import pygame

class Cursor:
    def __init__(self, x, y, final_y):
        self.x = x
        self.y = y
        self.final_y = final_y
        self.color = (0, 0, 0)
        self.visible = True
        self.time_since_last_blinked = 0

    def draw(self, win):

        if self.visible:
            pygame.draw.line(win, self.color, (self.x, self.y), (self.x, self.final_y))

    def blink(self, time):

        blink_duration = 500

        if(time - self.time_since_last_blinked >= blink_duration):
            self.visible = not self.visible
            self.time_since_last_blinked = time