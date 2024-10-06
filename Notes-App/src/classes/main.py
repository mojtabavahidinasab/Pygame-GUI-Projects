import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import *

pygame.init()

from line import Line
from cursor import Cursor
from menu import Menu

root = tk.Tk()

root.withdraw()

class App:
    def __init__(self):
        self.width, self.height = 1000, 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (255, 255, 255)
        self.lines = []
        self.counter = 0
        self.current_line = None
        self.typing = False
        self.cursor = Cursor(0, 0, 0)
        self.border = 40
        self.time = None
        self.menu = Menu(0, 0)
        self.fast_backspace = False

    def update_line(self):

        self.current_line = self.lines[self.counter]

    def line_array(self, num, size):

        for i in range(num):

            line = Line(10, (50 + ((size + 2) * i)), f"{i + 1} ")
            self.lines.append(line)

        self.current_line = self.lines[self.counter]
    
    def cursor_(self):

        self.cursor.x = self.current_line.rect.x + self.current_line.rect.width
        self.cursor.y = self.current_line.rect.y
        self.cursor.final_y = self.current_line.rect.y + self.current_line.rect.height

    def change_line_after_completion(self, line):

        if self.typing:
            if line.rect.x + line.rect.width >= 980:
                self.counter += 1

    def update_border(self):

        if self.counter <= 8:
            self.border = 40

        elif self.counter >= 9:
            self.border = 50

    def save(self):

        filetypes = (('Text Files', '*.txt'),
                     ('All Files', '*.*')
                    )
        
        file = asksaveasfilename(filetypes=filetypes, defaultextension='.txt')
        
        path = file

        list_ = []

        for idx, line in enumerate(self.lines):

            if idx <= 8:
                list_.append(line.text[2:])
            else:
                list_.append(line.text[3:])

        with open(path, 'w') as file_:
            file_.write('\n'.join(list_))

    def open_file(self):

        for idx, line in enumerate(self.lines):
            line.text = f"{idx + 1} "

        filetypes = (('Text Files', '*.txt'),
                     ('All Files', '*.*')
                    )

        filename = filedialog.askopenfilename(
            title='Select a File',
            filetypes=filetypes
        )

        if filename == '':
            path = None
        else:
            path = filename

        list_ = []

        if path is not None:
            
            with open(path, 'r') as file:
                list_ = file.readlines()

            for i in range(len(list_)):
                text = list_[i]

                self.lines[i].text += text[:-1]

            self.counter = len(list_) - 1

    def draw_lines(self):

        for i in range(self.counter + 1):
            self.lines[i].render(self.win)

    def main_function(self):
        
        self.line_array(250, 20)

        Running = True
        while Running:

            self.time = pygame.time.get_ticks()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    btn_list = self.menu.btn_list

                    if btn_list[0].rect.collidepoint(pos):

                        for idx, line in enumerate(self.lines):
                            line.text = f"{idx + 1} "

                        self.counter = 0

                    if btn_list[1].rect.collidepoint(pos):
                        self.open_file()

                    if btn_list[2].rect.collidepoint(pos):
                        self.save()

                    #if btn_list[3].rect.collidepoint(pos):
                        #print("Open settings menu")
 
                if event.type == pygame.MOUSEWHEEL:
                    offset = event.y * 5

                    for line in self.lines:
                        line.y += offset 
                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        if self.counter < len(self.lines) - 1:
                            self.counter += 1
                        
                    elif event.key == pygame.K_BACKSPACE:

                        self.typing = False
                
                        if(self.current_line.rect.x + self.current_line.rect.width <= self.border + 3):
                            if self.counter > 0:
                                self.counter -= 1

                        else:
                            self.current_line.text = self.current_line.text[:-1]

                    elif event.key == pygame.K_UP:
                        if self.counter > 0:
                            self.counter -= 1

                    elif event.key == pygame.K_DOWN:
                        if self.counter < len(self.lines) - 1:
                            self.counter += 1

                    elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        print("copy")

                    elif event.key == pygame.K_v and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        print("paste")

                    elif event.key == pygame.K_LEFT:
                        self.cursor.x -= 20

                    elif event.key == pygame.K_RIGHT:
                        if not self.cursor.x == self.current_line.rect.x + self.current_line.rect.width:
                            self.cursor.x += 20

                    else:
                        self.typing = True
                        self.current_line.text += event.unicode

            keys = pygame.key.get_pressed()

            if self.fast_backspace:
                if keys[pygame.K_BACKSPACE]:
                    self.current_line.text = self.current_line.text[:-1]

            self.draw()

    def draw(self):

        self.win.fill(self.color)

        self.update_line()

        self.update_border()

        self.draw_lines()

        self.cursor_()

        self.cursor.draw(self.win)
        self.cursor.blink(self.time)

        self.change_line_after_completion(self.current_line)

        self.menu.draw(self.win)

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()