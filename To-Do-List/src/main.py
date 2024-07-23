import pygame

pygame.init()

from textbar import TextBar
from main_panel import Panel
from path import get_path

FILE_PATH_LIST = get_path("src", "file.txt")
FILE_PATH_NUM = get_path("src", "num.txt")
FILE_PATH_CLICKED = get_path("src", "clicked.txt")

FONT = get_path("assets", "font.ttf")

class App:
    def __init__(self):
        self.width, self.height = 700, 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (150, 100, 100)
        self.text_bar = TextBar(50, 525, FONT)
        self.task_counter = 0
        self.list = []
        self.moving = None
        self.initial_pos = (0, 0)
        self.caption = pygame.display.set_caption("To-Do-List")

    def add_btn_clicked(self):

        if not self.text_bar.string == "":

            text = self.text_bar.string
            task = Panel(50, (25 + (self.task_counter * 75)), FONT, text, 0, False)
            self.list.append(task)
            self.text_bar.string = ""
            self.task_counter += 1

    def load_tasks(self):

        list_task = self.read(FILE_PATH_LIST)
        list_num = self.read(FILE_PATH_NUM)
        list_clicked = self.read(FILE_PATH_CLICKED)

        if len(list_task) != len(list_num) != len(list_clicked):
            print("ERROR")
            return
        
        for i in range(len(list_task)):
            task_text = list_task[i].strip()
            priority_num = int(list_num[i].strip())
            task_clicked = eval(list_clicked[i].strip())
            task = Panel(50, (50 + (i * 75)), FONT, task_text, priority_num, task_clicked)
            self.list.append(task)
            self.task_counter += 1

    def update_positions(self):

        for i, task in enumerate(self.list):
            task.y = (50 + (i * 75))
            task.delete_btn_rect.y = task.y + 5
            task.priority_btn_rect.y = task.y + (25//2)
            task.ticked_btn_rect.y = (task.y + (25//2))

    def update_priority(self):
        
        for i in range(len(self.list)):
            for j in range(i + 1, len(self.list)):
                if self.list[i].priority_num < self.list[j].priority_num:
                    self.list[i], self.list[j] = self.list[j], self.list[i]

    def write(self):

        open(FILE_PATH_LIST, "w").close()
        open(FILE_PATH_NUM, "w").close()
        open(FILE_PATH_CLICKED, "w").close()

        file_list = open(FILE_PATH_LIST, "w")
        file_num = open(FILE_PATH_NUM, "w")
        file_clicked = open(FILE_PATH_CLICKED, "w")

        for task in self.list:
            file_list.write(task.string + "\n")
            file_num.write(str(task.priority_num) + "\n")
            file_clicked.write(str(task.task_ticked) + "\n")

        file_list.close()
        file_num.close()
        file_clicked.close()

    def read(self, path):

        file = open(path, "r")

        list = file.readlines()

        return list

    def main_function(self):

        self.load_tasks()

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                    self.write()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    for task in self.list:
                        if task.delete_btn_rect.collidepoint(pos):
                            self.list.remove(task)
                            self.task_counter -= 1

                        if task.priority_btn_rect.collidepoint(pos):
                            task.update_priority_num()

                        if task.ticked_btn_rect.collidepoint(pos):
                            task.task_ticked = not task.task_ticked
                            task.priority_num = 0

                    if self.text_bar.rect.collidepoint(pos):
                        self.text_bar.color = (0, 0, 0)
                        self.writing = True
                    else:
                        self.text_bar.color = self.text_bar.color_main
                        self.writing = False

                    if self.text_bar.add_btn_rect.collidepoint(pos):
                        self.add_btn_clicked()

                if event.type == pygame.KEYDOWN:

                    if self.writing:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_bar.string = self.text_bar.string[:-1]

                        elif event.key == pygame.K_RETURN:
                            self.add_btn_clicked()
                        
                        else:
                            self.text_bar.string += event.unicode

            self.draw()

    def draw(self):

        self.win.fill(self.color)

        self.text_bar.draw(self.win)

        for task in self.list:
            task.draw(self.win)

        self.update_priority()
        self.update_positions()

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()