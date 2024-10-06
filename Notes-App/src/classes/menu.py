import pygame
from button import Button

class Menu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.new_btn = Button(x, y, 100, 30, (100, 100, 100), 2, "New")
        self.open_btn = Button(x + 105, y, 100, 30, (100, 100, 100), 2, "Open")
        self.save_btn = Button(x + 210, y, 100, 30, (100, 100, 100), 2, "Save")
        #self.settings_btn = Button(x + 315, y, 100, 30, (100, 100, 100), 2, "Settings")
        self.btn_list = [self.new_btn, self.open_btn, self.save_btn]

    def draw(self, win):

        for button in self.btn_list:
            button.draw(win)