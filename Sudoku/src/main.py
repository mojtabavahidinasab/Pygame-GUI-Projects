import pygame, time

pygame.init()

from functions import make_grid, make_panel, SolveBoard, ValidPositionObject
from board import board
from button import Button
from label import Label

CELL_WIDTH = 50

class App:
    def __init__(self):
        self.width, self.height = 700, 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.color = (220, 220, 220)
        self.grid = make_grid((self.width - (CELL_WIDTH * 9))//2, (self.height - (CELL_WIDTH * 9))//2, CELL_WIDTH, board)
        self.panel = make_panel((self.grid[0][0].x), 650, CELL_WIDTH)
        self.current_cell = None
        self.current_row = 0
        self.current_col = 0
        self.solved = board if SolveBoard(board, 0, 0) else None
        self.button = Button((self.width - 200)//2, 725, "Check")
        self.label = Label((self.width//2), (50))
        self.checked = False
        self.solve_button = Button((self.width - 200)//2, 100, "Solve")

    def solve(self):

        for i in range(9):
            for j in range(9):
                self.grid[i][j].val = self.solved[i][j]

    def check(self):

        solved = False

        grid = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if self.grid[i][j].val is None:
                    grid[i][j] = 0
                else:
                    grid[i][j] = self.grid[i][j].val

        if grid == self.solved:
            solved = True
        else:
            solved = False

        if solved:
            self.label.text = "The Board is Solved!"
            self.label.success = True
        else:
            self.label.text = "Incorrect"
            self.label.success = False

    def main_function(self):

        Running = True
        while Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    for i, row in enumerate(self.grid):
                        for j, cell in enumerate(row):
                            if cell.rect.collidepoint(pos):

                                if not cell.is_final:

                                    self.current_cell = cell
                                    cell.color = (200, 200, 200)
                                    self.current_row = i
                                    self.current_col = j
                                else:
                                    pass

                            else:
                                cell.color = (255, 255, 255)

                    for cell in self.panel:
                        if cell.rect.collidepoint(pos):
                            if self.current_cell:
                                self.current_cell.val = cell.val
                                
                    if self.button.rect.collidepoint(pos):
                        self.check()
                        self.checked = True
                    else:
                        self.checked = False

                    if self.solve_button.rect.collidepoint(pos):
                        self.solve()

            self.draw()

    def draw(self):

        self.win.fill(self.color)

        for row in self.grid:
            for cell in row:
                cell.draw(self.win)

        for cell in self.panel:
            cell.draw(self.win)

        self.button.draw(self.win)
        self.solve_button.draw(self.win)

        if self.checked:
            self.label.draw(self.win)

        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    App().main_function()